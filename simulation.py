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

# import necessary data structures
from environment_variables import Environment_Variables
from system_record import System_Record
from pricing_variables import Pricing_Variables
from user_record import User_Record

from collections import deque
import pdb

def run_simulation(env_vars, sys_rec, pricing_vars, user_list):
    period = 0
    last_three_quit_cnt = deque()
    last_three_skipped_cnt = deque()

    while True:
        RSA(env_vars, sys_rec, user_list, period)

        if period == 0:
            uf1_determine_defectors(env_vars, sys_rec, user_list)
        else:
            uf2_pricing_function(env_vars, sys_rec, pricing_vars, user_list, period)
        
        RSB(env_vars, sys_rec, user_list, period)
        
        sf4_invalidate_subgroups(sys_rec, user_list)

        uf6_user_quit_function(env_vars, sys_rec, user_list)

        sf8_determine_claims(env_vars, user_list)

        sf7_reorganization_of_users(env_vars, sys_rec, user_list)
        
        # keep track of last 3 skipped/quit cnt so that we can terminate 
        # the simulation if they are 0 for three periods in a row.
        last_three_quit_cnt.append(sys_rec.quit_cnt)
        last_three_skipped_cnt.append(sys_rec.skipped_cnt)
        print(f"period {period}: quit_cnt = {sys_rec.quit_cnt}")
        print(f"period {period}: skipped_cnt = {sys_rec.skipped_cnt}")

        period += 1
        if period < 9:
            if len(last_three_quit_cnt) == 3:
                nonzero = False
                for i, j in zip(last_three_quit_cnt, last_three_skipped_cnt):
                    if (i + j) != 0:
                        nonzero = True
                        break

                if not nonzero:
                    print("Simulation terminated since last three quit/skipped counts are 0")
                    break
                
                last_three_quit_cnt.popleft()
                last_three_skipped_cnt.popleft()
        else:
            print("Simulation reached 10th period and successfully terminated.")
            break

        sys_rec = System_Record(sys_rec.valid_remaining)  

def test_simulation():
    # initialize a list of users
    user_list = [User_Record(100, 0) for _ in range(100)]
    
    # subgroup setup for all the users
    data = subgroup_setup(len(user_list), user_list)
    num_four_member_groups = data[0]

    # initialize environment variables
    env_vars = Environment_Variables()
    env_vars.total_member_cnt = len(user_list)

    # initialize system record
    sys_record = System_Record(env_vars.total_member_cnt)

    # assign roles
    role_assignment(env_vars, user_list, num_four_member_groups * 4)

    # execute simulation with these values
    run_simulation(env_vars, sys_record, Pricing_Variables(), user_list)

test_simulation()
