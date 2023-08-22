
from utility import is_approx_equal
from user_record import *

def RSA(env_vars, sys_rec, user_list, period):
    # calculate current month's first calculation
    cur_month_first_calc = env_vars.cov_req / sys_rec.valid_remaining
    print(f"cov_req: {env_vars.cov_req} / valid_remaining: {sys_rec.valid_remaining}")
    print(f"current month first calc: {cur_month_first_calc}")

    # perform operations for period 1
    if period == 0:
        # iterate through each user
        for i, user in enumerate(user_list):
            # skip user if user is not active
            if user.sbg_status != ValidityEnum.VALID:
                continue
           
            # set user's cur_month_first_calc value
            sys_rec.cur_month_1st_calc = cur_month_first_calc
            # for this period only: current month second calc = current month 1st calc   
            user.cur_month_second_calc_list[period] = cur_month_first_calc
#            print(f"Setting cur_month_second_list[{period}] = {cur_month_first_calc}")
            
    # perform operations for period 2+
    else:
        # iterate through each user
        for i, user in enumerate(user_list):
            # skip if user is not active
            if user.sbg_status != ValidityEnum.VALID:
                continue
            
            # set user's cur_month_first_calc value
            sys_rec.cur_month_1st_calc = cur_month_first_calc
            
# NOTE: this was moved to user_record.py to be calculated once and kept as a constant.
# calculate credit to saving's account
#            user.credit_to_savings_account = env_vars.cov_req / env_vars.total_member_cnt

            # determine wallet balance
            user.wallet_balance = cur_month_first_calc
            user.wallet_balance += user.debit_to_savings_account_list[period - 1]
            user.wallet_balance -= user.wallet_no_claim_refund
            user.wallet_balance -= user.wallet_reorg_refund

            # set current month second calculation for this period to wallet balance
            user.cur_month_second_calc_list[period] = user.wallet_balance
            print(f"Setting cur_month_second_list[{period}] = {user.wallet_balance} = {cur_month_first_calc} + {user.debit_to_savings_account_list[period - 1]} - {user.wallet_no_claim_refund} - {user.wallet_reorg_refund}")
            # reset wallet balance to 0
            user.wallet_balance = 0

            # determine total_value_refund_period for this period to keep historical record moving forward
            user.total_value_refund_list[period] = user.wallet_no_claim_refund + user.wallet_reorg_refund

            # clean up of values
            user.wallet_reorg_refund = 0
            user.wallet_no_claim_refund = 0


def RSB(env_vars, sys_rec, user_list, period):
    # perform operations for period 1
    if period == 0:
        # iterate through active users
        for i, user in enumerate(user_list):
            # skip inactive user
            if user.sbg_status != ValidityEnum.VALID:
                continue

            # update current month balance
            user.cur_month_balance += sys_rec.cur_month_1st_calc

    # perform operations for periods 2+
    else:
        # iterates through active users
        for i, user in enumerate(user_list):
            # skip inactive user
            if user.sbg_status != ValidityEnum.VALID:
                continue
            
            # if current month balance exceeds current month's first calculation:
            if user.cur_month_balance > sys_rec.cur_month_1st_calc:
                # set to (cur month second calc [cur period]) - (debit to savings account [prev period])
                user.cur_month_balance = user.cur_month_second_calc_list[period]
                user.cur_month_balance -= user.debit_to_savings_account_list[period - 1]
                # set current period debit to savings account to 0
                user.debit_to_savings_account_list[period] = 0
            else:
                # otherwise, set current month balance to this period's current month second calculation 
                user.cur_month_balance = user.cur_month_second_calc_list[period]


def RSC(env_vars, sys_rec, user_list, period):
    if period == 0:
        # calculate total_shortfall_period_one_claim
        sys_rec.total_shortfall_period_one_claim = sys_rec.defection_shortfall
        sys_rec.total_shortfall_period_one_claim += sys_rec.skip_shortfall
        sys_rec.total_shortfall_period_one_claim += sys_rec.invalid_shortfall
        print(f"total_shortfall_period_one_claim = {sys_rec.total_shortfall_period_one_claim}")


        # calculate individual_shortfall_period_one_claim
        sys_rec.individual_shortfall_period_one_claim = sys_rec.total_shortfall_period_one_claim
        sys_rec.individual_shortfall_period_one_claim /= sys_rec.valid_remaining
        print(f"individual_shortfall_period_one_claim = {sys_rec.individual_shortfall_period_one_claim}")

        # calculate cur_month_total_shortfall
        sys_rec.cur_month_total_shortfall = sys_rec.skip_shortfall + sys_rec.invalid_shortfall
        print(f"cur_month_total_shortfall = {sys_rec.cur_month_total_shortfall}")

        # calculate cur_month_individual_shortfall
        sys_rec.cur_month_individual_shortfall = sys_rec.cur_month_total_shortfall / sys_rec.valid_remaining

        # will sum the current month's balance for all users, for an error check at the end
        cur_month_balance_sum = 0
        
        # iterate through each user
        for user in user_list:
            # skip invalid users
            if user.sbg_status != ValidityEnum.VALID:
                continue
            
            # for each user, add individual shortfall to their "debit to savings account" for this period
            user.debit_to_savings_account_list[period] += sys_rec.individual_shortfall_period_one_claim
           
            # check for fatal error. This would cause them to get money without a claim.
            if user.credit_to_savings_account < user.debit_to_savings_account_list[period]:
                raise ValueError(f"Fatal Error: Credit to savings account ({user.credit_to_savings_account}) is less than debit to savings account ({user.debit_to_savings_account_list[period]})!")

            # update current month's balance
            user.cur_month_balance += sys_rec.cur_month_individual_shortfall
            print(f"cur_month_individual_shortfall: {sys_rec.cur_month_individual_shortfall}")

            # add to the sum
            cur_month_balance_sum += user.cur_month_balance
       
        # finally, make sure the sum of current month balances is equal to cov_req. If not, there is an error
        # NOTE: Due to the arithmetic being performed, sometimes there is a floating point error here. Hence approx equal function
        if not is_approx_equal(cur_month_balance_sum, env_vars.cov_req, 0.01):
            raise ValueError(f"Fatal Error: The sum of current month balances {cur_month_balance_sum} does not equal cov_req {env_vars.cov_req}!")
    else:
        # calculate cur_month_total_shortfall
        sys_rec.cur_month_total_shortfall = sys_rec.skip_shortfall + sys_rec.invalid_shortfall
        print(f"total_shortfall {sys_rec.cur_month_total_shortfall} = skip_shortfall {sys_rec.skip_shortfall} + invalid_shortfall {sys_rec.invalid_shortfall}")

        # calculate cur_month_individual_shortfall
        sys_rec.cur_month_individual_shortfall = sys_rec.cur_month_total_shortfall / sys_rec.valid_remaining
        print(f"individual_shortfall {sys_rec.cur_month_individual_shortfall} = total_shortfall {sys_rec.cur_month_total_shortfall} / valid_remaining {sys_rec.valid_remaining}")

        # will sum the current month's balance for all users, for an error check at the end
        cur_month_balance_sum = 0
        
        # iterate through each user
        for user in user_list:
            # skip invalid users
            if user.sbg_status != ValidityEnum.VALID:
                continue
           
            # set user's debit to savings account equal to this month's individual shortfall
            user.debit_to_savings_account_list[period] = sys_rec.cur_month_individual_shortfall
          
            # check for fatal error. This would cause them to get money without a claim.
            if user.credit_to_savings_account < user.debit_to_savings_account_list[period]:
                raise ValueError("Fatal Error: Credit to savings account is less than debit to savings account!")

            # update current month's balance
            user.cur_month_balance += sys_rec.cur_month_individual_shortfall

            # add to the sum
            cur_month_balance_sum += user.cur_month_balance
            print(f"cur_month_balance = {user.cur_month_balance}")

        # finally, make sure the sum of current month balances is equal to cov_req. If not, there is an error
        # NOTE: Due to the arithmetic being performed, sometimes there is a floating point error here. Hence approx_equal function
        if not is_approx_equal(cur_month_balance_sum, env_vars.cov_req, 0.01):
            raise ValueError(f"Fatal Error: The sum of current month balances {cur_month_balance_sum} does not equal cov_req {env_vars.cov_req}!")
# Assuming ValidityEnum.VALID is defined elsewhere in the original code.

def RSAB(env_vars, sys_rec, user_list, period):
    # Shared variable
    cur_month_first_calc = env_vars.cov_req / sys_rec.valid_remaining

    # Iterate through each user
    for i, user in enumerate(user_list):
        # Skip if user is not active
        if user.sbg_status != ValidityEnum.VALID:
            continue

        # Period 1 operations
        if period == 0:
            sys_rec.cur_month_1st_calc = cur_month_first_calc
            user.cur_month_second_calc_list[period] = cur_month_first_calc
            user.cur_month_balance += cur_month_first_calc

        # Period 2+ operations
        else:
            sys_rec.cur_month_1st_calc = cur_month_first_calc

            user.wallet_balance = (cur_month_first_calc + 
                                   user.debit_to_savings_account_list[period - 1] - 
                                   user.wallet_no_claim_refund - 
                                   user.wallet_reorg_refund)
            
            user.cur_month_second_calc_list[period] = user.wallet_balance
            user.wallet_balance = 0
            user.total_value_refund_list[period] = user.wallet_no_claim_refund + user.wallet_reorg_refund

            if user.cur_month_balance > sys_rec.cur_month_1st_calc:
                user.cur_month_balance = (user.cur_month_second_calc_list[period] - 
                                          user.debit_to_savings_account_list[period - 1])
                user.debit_to_savings_account_list[period] = 0
            else:
                user.cur_month_balance = user.cur_month_second_calc_list[period]

            user.wallet_reorg_refund = 0
            user.wallet_no_claim_refund = 0

#########################################################################


