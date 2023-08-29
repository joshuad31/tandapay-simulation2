# import all primary functions
from uf1_determine_defectors import uf1_determine_defectors
from uf2_pricing_function import uf2_pricing_function
from sf4_invalidate_subgroups import sf4_invalidate_subgroups
from uf6_user_quit_function import uf6_user_quit_function
from sf7_reorganization_of_users import sf7_reorganization_of_users
from sf8_determine_claims import sf8_determine_claims

# import secondary functions
from role_assignment import role_assignment
from subgroup_setup import subgroup_setup
from period_functions import *
from queueing import *

# import necessary data structures
from environment_variables import Environment_Variables
from system_record import System_Record
from pricing_variables import Pricing_Variables
from user_record import User_Record

from diagnostics import *

from collections import deque
import pdb

class ResultsEnum(Enum):
    WIN = 0
    LOSS = 1
    DRAW = 2

def print_user_info(user_list, index: int, label):
    if index == -1:
        return

    print(f"----------[printing user info: {label}]----------")
    print(f"sbg status = {user_list[index].sbg_status}")
    print(f"invalid_refund = {user_list[index].invalid_refund}")
    print(f"----------[printing user info: {label}]----------")

def print_vars(env_vars, sys_rec, pricing_vars, user_list, label):
    print(f"----------[printing variables: {label}]----------")
    print(f"number of defector/skipped/invalid/quit: {sys_rec.defected_cnt}/{sys_rec.skipped_cnt}/{sys_rec.invalid_cnt}/{sys_rec.quit_cnt}")
    print(f"defector/skipped/invalid shortfall: {sys_rec.defection_shortfall}/{sys_rec.skip_shortfall}/{sys_rec.invalid_shortfall}")
    print(f"valid_remaining: {sys_rec.valid_remaining}")

    sum_valid = 0
    for user in user_list:
        if user.sbg_status == ValidityEnum.VALID:
            sum_valid += 1

    print(f"number of users marked as valid: {sum_valid}")

    print(f"----------[finished printing:  {label}]----------\n")

def run_simulation(env_vars, sys_rec, pricing_vars, user_list, diagnostics_object = Diagnostics()):
    period = 0
    last_three_quit_cnt = deque()
    last_three_skipped_cnt = deque()

    while True:
#        pdb.set_trace()
        rsa_calculate_premiums(env_vars, sys_rec, user_list, period) 
#        print_vars(env_vars, sys_rec, pricing_vars, user_list, "after RSA")        

        if period == 0:
            uf1_determine_defectors(env_vars, sys_rec, user_list)
#            print_vars(env_vars, sys_rec, pricing_vars, user_list, "after UF1")
        else:
            uf2_pricing_function(env_vars, sys_rec, pricing_vars, user_list, period, diagnostics_object)
#            print_user_info(user_list, tracking, "after SF2")
#            print_vars(env_vars, sys_rec, pricing_vars, user_list, "after UF2")        
        
        rsb_payback_debt(env_vars, sys_rec, user_list, period)
#        print_vars(env_vars, sys_rec, pricing_vars, user_list, "after RSB")        

        sf4_invalidate_subgroups(sys_rec, user_list)
#        print_vars(env_vars, sys_rec, pricing_vars, user_list, "after SF4")        
#        print_user_info(user_list, tracking, "after SF4")

        uf6_user_quit_function(env_vars, sys_rec, user_list)
#        print_vars(env_vars, sys_rec, pricing_vars, user_list, "after UF6")        
        
        rsc_calculate_shortfall(env_vars, sys_rec, user_list, period)
#        print_vars(env_vars, sys_rec, pricing_vars, user_list, "after RSC")        

        sf8_determine_claims(env_vars, user_list)
#        print_vars(env_vars, sys_rec, pricing_vars, user_list, "after SF8")        

        sf7_reorganization_of_users(env_vars, sys_rec, user_list)
#        print_user_info(user_list, tracking, "after SF7")
#        print_vars(env_vars, sys_rec, pricing_vars, user_list, "after SF7")        

        queueing_function(user_list)

        # keep track of last 3 skipped/quit cnt so that we can terminate 
        # the simulation if they are 0 for three periods in a row.
        last_three_quit_cnt.append(sys_rec.quit_cnt)
        last_three_skipped_cnt.append(sys_rec.skipped_cnt)
#        print(f"period {period}: quit_cnt = {sys_rec.quit_cnt}")
#        print(f"period {period}: skipped_cnt = {sys_rec.skipped_cnt}")

        

        # advance period logic:
        
        # win condition: valid_remaining below 50% of original total_member_cnt.
        # if this happens, win no matter what, so we don't even have to do the
        # advance period logic to advance to the next period.
        if (sys_rec.valid_remaining / env_vars.total_member_cnt) < 0.50:
            return ResultsEnum.WIN
            #print("WIN: valid_remaining below 50% of total_member_cnt")
            #break

        period += 1
        if period < 9:
            if len(last_three_quit_cnt) == 3:
                nonzero = False
                for i, j in zip(last_three_quit_cnt, last_three_skipped_cnt):
                    if (i + j) != 0:
                        nonzero = True
                        break

                if not nonzero:
                    # draw condition: 3 periods in a row where nobody quits or leaves and
                    # valid_remaining is less than 60% of total_member_cnt
                    if (sys_rec.valid_remaining / env_vars.total_member_cnt) < 0.60:
                        return ResultsEnum.DRAW
                        #print("DRAW: 3 periods in a row where nobody quits or leaves, and valid_remaining below 60% of total_member_cnt")
                    else:
                        return ResultsEnum.LOSS
                        #print("LOSS: 3 periods in a row where nobody quits or leaves, and valid_remaining above 60% of total_member_cnt")
                    
                    # end simulation no matter what if this happens
                    #break

                last_three_quit_cnt.popleft()
                last_three_skipped_cnt.popleft()
        else:
            # win condition: If we're in the final period and valid_remaining is
            # below 55 percent of total_member_cnt
            if (sys_rec.valid_remaining / env_vars.total_member_cnt) < 0.55:
                return ResultsEnum.WIN
                #print("WIN: final period completed with valid_remaining below 55% of total_member_cnt")

            # draw condition: If we're in the final period and valid_remaining is
            # less than 65 percent, but not less than 55 percent of total_member_cnt
            elif (sys_rec.valid_remaining / env_vars.total_member_cnt) < 0.65:
                return ResultsEnum.DRAW
                #print("DRAW: final period completed with valid_remaining below 65% of total_member_cnt")
            
            # loss condition: Reached the final period with valid_remaining still above 65% of total_member_cnt
            else:
                return ResultsEnum.LOSS
                #print("LOSS: reached final period with valid_remaining above 65% of total_member_cnt")
            
            # always end the simulation in the final period.
            break

        sys_rec = System_Record(sys_rec.valid_remaining)  
        #print("\n---------------------------------------\n")

def test_simulation(shouldPrint = False):
    # initialize a list of users
    num_users = 100
    
    # initialize environment variables
    env_vars = Environment_Variables()
    env_vars.total_member_cnt = num_users 

    user_list = [User_Record(env_vars) for _ in range(100)]
    
    # subgroup setup for all the users
    data = subgroup_setup(len(user_list), user_list)
    num_four_member_groups = data[0]

    # initialize system record
    sys_record = System_Record(env_vars.total_member_cnt)

    # assign roles
    role_assignment(env_vars, user_list, num_four_member_groups * 4)

    result = run_simulation(env_vars, sys_record, Pricing_Variables(), user_list)
   
    if not shouldPrint:
        return result

    if result == ResultsEnum.WIN:
        print("win")
    elif result == ResultsEnum.DRAW:
        print("draw")
    else:
        print("loss")
   
    return result

def test_multiple():
    num_wins = 0
    num_draws = 0
    num_losses = 0
    
    for i in range(1000):
        result = test_simulation()
        
        if result == ResultsEnum.WIN:
            num_wins += 1
        elif result == ResultsEnum.DRAW:
            num_draws += 1
        else:
            num_losses += 1
    
    print(f"wins/draws/losses/total: {num_wins}/{num_draws}/{num_losses}/{num_wins + num_draws + num_losses}")

