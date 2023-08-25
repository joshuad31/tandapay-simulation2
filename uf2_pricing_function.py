from environment_variables import Environment_Variables
from pricing_variables import Pricing_Variables
from system_record import System_Record
from user_record import *
from utility import remove_user
import random

def uf2_pricing_function(env_vars, sys_rec, pricing_vars, user_list, current_period):
    # Calculate the pricing slope:
    ph_leave_delta = pricing_vars.ph_leave_ceiling - pricing_vars.ph_leave_floor
    prem_inc_delta = pricing_vars.prem_inc_ceiling - pricing_vars.prem_inc_floor
    pricing_slope = ph_leave_delta / prem_inc_delta
    
    leave_list = []

    # iterate through all of the active users
    for user_index in range(len(user_list)):
        user = user_list[user_index]
        # if this user is not an active user (e.g. sbg status != VALID), skip them
        if user.sbg_status != ValidityEnum.VALID:
            continue
        
        # Determine if this user is a qualifying user or if they should be skipped
        cm_sec_calc = user.second_premium_calc_list[current_period]
        threshold = pricing_vars.prem_inc_floor * (env_vars.cov_req / env_vars.total_member_cnt)
        # skip this user because they are not qualifying
        if cm_sec_calc < threshold:
            continue
        
        # 1. IF total_value_refund_periodx (current period) is equal to zero
        if user.total_value_refund_list[current_period] == 0:
            # 1a. iterate through the previous periods in order of Most Recent -> Least Recent
            matching = -1
            for i in range(current_period - 1, -1, -1):
                if user.total_value_refund_list[i] == 0:
                    matching = i
                    break
            
            # there should definitely be a match, so if there is not, raise an error
            if matching == -1:
                raise ValueError("In uf2, matching = -1 after trying to find most recent previous month where total refund value == 0")
        
            # 1b. Calculate the one month increase percentage:
            pm_sec_calc = user.second_premium_calc_list[matching]
            one_month_increase_percentage = (cm_sec_calc / pm_sec_calc) - 1
            
            #print(f"one month increase percentage (with -1): f{one_month_increase_percentage}")

            # 1c. one_month_increase_percentage should not exceed prem_inc_ceiling
            one_month_increase_percentage = min(one_month_increase_percentage, pricing_vars.prem_inc_ceiling)

            # 1d. IF one_month_increase_percentage >= prem_inc_floor
            if one_month_increase_percentage >= pricing_vars.prem_inc_floor:
                # 1d-1. calculate pricing_vars.ph_skip_percentage (broke down a messy arithmetic operation into multiple):
                pricing_vars.ph_skip_percentage = 0
                pricing_vars.ph_skip_percentage += pricing_slope * one_month_increase_percentage
                pricing_vars.ph_skip_percentage -= pricing_slope * pricing_vars.prem_inc_floor
                pricing_vars.ph_skip_percentage += pricing_vars.ph_leave_floor
                
                # 1d-2. generate a random number between 0 and 1
                random_number = random.uniform(0, 1)

                # 1d-3. if random_number < pricing_vars.ph_skip_percentage, add user to the "leave list"
                if random_number < pricing_vars.ph_skip_percentage:
                    leave_list.append(user_index)
            
            # 1e. ELSE evaluate user for cumulative_increase_percentage. ONLY run in periods 5 - 10
            elif cumulative_increase_percentage(env_vars, pricing_vars, user, current_period):
                leave_list.append(user_index)
        # 2. ELSE IF total_value_refund (current period) is NOT equal to 0
        elif user.total_value_refund_list[current_period] != 0:
            # 2a. if current_month_sec_calc is less than or equal to 0, continue to next user
            if user.second_premium_calc_list[current_period] <= 0:
                continue
            
            # evaluate user for cumulative_increase_percentage
            if user.second_premium_calc_list[current_period] >= threshold:
                if cumulative_increase_percentage(env_vars, pricing_vars, user, current_period):
                    leave_list.append(user_index)

        
            # 2b. else, continue to the next user (no code needed).

    # 3. Evaluate leave list
    for i in leave_list:
        sys_rec.valid_remaining -= 1
        sys_rec.skipped_cnt += 1
        remove_user(user_list, i, "User was in leave list in uf2.")

    # 4. since sys_rec.skipped_cnt uses a setter, it will calculate skip_shortfall automatically
    # when skipped_cnt is updated. Therefore, no code is needed here.

def cumulative_increase_percentage(env_vars, pricing_vars, user, current_period, LOWER_PERIOD = 4, UPPER_PERIOD = 9, NUM_MONTHS_TO_AVG = 3):
    # run only if the period is 5-10
    if not (LOWER_PERIOD <= current_period <= UPPER_PERIOD):
        return False
    
    # 1. calculate average for current_month_sec_calc for last 3 periods
    debug_total_iterations = 0
    average = 0
    for i in range(current_period, current_period - NUM_MONTHS_TO_AVG, -1):
        average += user.second_premium_calc_list[i]
        debug_total_iterations += 1

    assert debug_total_iterations == NUM_MONTHS_TO_AVG, f"loop iterated more than {NUM_MONTHS_TO_AVG} times!"
    average /= NUM_MONTHS_TO_AVG

    # 2. cumulative_increase_percentage = (average / (cov_req / total_member_cnt)) - 1
    cumulative_increase_percentage = (average / (env_vars.cov_req / env_vars.total_member_cnt)) - 1
    
    if cumulative_increase_percentage > pricing_vars.prem_inc_cum:
        random_number = random.uniform(0, 1)
        if random_number < pricing_vars.ph_leave_cum:
            return True
        else:
            user.cur_status = CurrentStatusEnum.PAID
            return False
