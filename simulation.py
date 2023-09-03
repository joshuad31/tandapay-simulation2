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
from simulation_results import *
from csv_builder import CSV_Builder
from config_helper import INI_Handler

from collections import deque
import pdb

def exec_simulation(env_vars, pricing_vars, func = None):
    # initialize user_list
    user_list = [User_Record(env_vars) for _ in range(env_vars.total_member_cnt)]

    # perform subgroup setup
    data = subgroup_setup(len(user_list), user_list)
    num_four_member_groups = data[0]

    # initialize system record:
    sys_rec = System_Record(env_vars.total_member_cnt)

    # assign roles
    role_assignment(env_vars, user_list, num_four_member_groups * 4)

    # run the simulation, return the simulation_results
    return base_simulation(env_vars, sys_rec, pricing_vars, user_list, func)

def base_simulation(env_vars, sys_rec, pricing_vars, user_list, func = None):
    period = 0
    last_three_quit_cnt = deque()
    last_three_skipped_cnt = deque()

    simulation_results = Simulation_Results()
    simulation_results.total_member_count = env_vars.total_member_cnt
    
    while True:
        rsa_calculate_premiums(env_vars, sys_rec, user_list, period) 

        if period == 0:
            uf1_determine_defectors(env_vars, sys_rec, user_list)
            # set number of defectors in simulation_results. This value should not change as the simulation runs,
            # so it's straightforward to just store this in the simulation_results now
        else:
            uf2_pricing_function(env_vars, sys_rec, pricing_vars, user_list, period)
        
        rsb_payback_debt(env_vars, sys_rec, user_list, period)

        sf4_invalidate_subgroups(sys_rec, user_list)

        uf6_user_quit_function(env_vars, sys_rec, user_list)
        
        rsc_calculate_shortfall(env_vars, sys_rec, user_list, period)

        sf8_determine_claims(env_vars, user_list)

        sf7_reorganization_of_users(env_vars, sys_rec, user_list)

        queueing_function(user_list)

        # keep track of last 3 skipped/quit cnt so that we can terminate 
        # the simulation if they are 0 for three periods in a row.
        last_three_quit_cnt.append(sys_rec.quit_cnt)
        last_three_skipped_cnt.append(sys_rec.skipped_cnt)
       
        if func is not None:
            func(period, env_vars, sys_rec, pricing_vars, user_list)
        
        take_snapshot(simulation_results, sys_rec, not (period == 1))
        # advance period logic:
        
        # win condition: valid_remaining below 50% of original total_member_cnt.
        # if this happens, win no matter what, so we don't even have to do the
        # advance period logic to advance to the next period.
        if (sys_rec.valid_remaining / env_vars.total_member_cnt) < 0.50:
            simulation_results.result = ResultsEnum.WIN_A
            #take_snapshot(simulation_results, sys_rec)
            return simulation_results

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
                        simulation_results.result = ResultsEnum.DRAW_A
                        #take_snapshot(simulation_results, sys_rec)
                        return simulation_results
                    # if it wasn't a draw, then it's a loss in this case.
                    else:
                        simulation_results.result = ResultsEnum.LOSS_A 
                        #take_snapshot(simulation_results, sys_rec)
                        return simulation_results
                    
                last_three_quit_cnt.popleft()
                last_three_skipped_cnt.popleft()
        else:
            # win condition: If we're in the final period and valid_remaining is
            # below 55 percent of total_member_cnt
            if (sys_rec.valid_remaining / env_vars.total_member_cnt) < 0.55:
                simulation_results.result = ResultsEnum.WIN_B
                #take_snapshot(simulation_results, sys_rec)
                return simulation_results

            # draw condition: If we're in the final period and valid_remaining is
            # less than 65 percent, but not less than 55 percent of total_member_cnt
            elif (sys_rec.valid_remaining / env_vars.total_member_cnt) < 0.65:
                simulation_results.result = ResultsEnum.DRAW_B
                #take_snapshot(simulation_results, sys_rec)
                return simulation_results
            
            # loss condition: Reached the final period with valid_remaining still above 65% of total_member_cnt
            else:
                simulation_results.result = ResultsEnum.LOSS_B
                #take_snapshot(simulation_results, sys_rec)
                return simulation_results
            
            # always end the simulation in the final period.
            break

        sys_rec = System_Record(sys_rec.valid_remaining)  

def take_snapshot(simulation_results, sys_rec, add_skipped = True):
    simulation_results.defectors += sys_rec.defected_cnt

    if add_skipped:
        simulation_results.skipped += sys_rec.skipped_cnt
   
    simulation_results.invalid += sys_rec.invalid_cnt
    simulation_results.quit += sys_rec.quit_cnt

if __name__ == "__main__":
    ini_handler = INI_Handler("config/settings_cli.ini")

    env_vars = ini_handler.read_environment_variables()
    pricing_vars = ini_handler.read_pricing_variables()

    simulation_results = exec_simulation(env_vars, pricing_vars, CSV_Builder().record)
    print(f"{ResultsEnum.get_result_str(simulation_results.result)}")



