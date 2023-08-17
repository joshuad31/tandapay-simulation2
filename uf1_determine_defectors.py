from role_assignment import *
from subgroup_setup import *

from environment_variables import Environemnt_Variables
from system_record import System_Record
from user_record import *
from utility import remove_user

def uf1_determine_defectors(env_vars, sys_record, user_list):
    if not isinstance(env_vars, Environemnt_Variables):
        raise TypeError("in UF1, env_vars is not of type Environemnt_Variables!")
    if not isinstance(sys_record, System_Record):
        raise TypeError("in UF1, sys_record is not of type System_Record!")
    if not isinstance(user_list, list):
        raise TypeError("in UF1, user_list is not a list!")
    if not env_vars.total_member_cnt == len(user_list):
        raise ValueError("total_member_cnt != len(user_list)!")
    
    # this will keep track of the number of defectors in each subgroup. It will be
    # key-value pairs (subgroup number, number of defectors)
    defector_count = {} 

    # this will keep track of the indices of all defectors so they can be iterated through in the future
    defector_indices = []

    # 1. iterate through each user in user_list
    for i in range(env_vars.total_member_cnt):
        # if the current user is a defector
        if user_list[i].pri_role == PrimaryRoleEnum.DEFECTOR:
            # if this subgroup isn't already in the dictionary, add it
            if user_list[i].cur_sbg_num not in defector_count:
                defector_count[user_list[i].cur_sbg_num] = 0
            # increment the number of defectors in their subgroup number by 1
            defector_count[user_list[i].cur_sbg_num] += 1
            # mark them as a defector for later iteration
            defector_indices.append(i) 

    # 2. iterate through each defector in user_list
    for i in range(env_vars.total_member_cnt):
        # first, get the current user's subgroup
        current_user_subgroup = user_list[i].cur_sbg_num
        
        # if there are no defectors in this subgroup, contine
        if current_user_subgroup not in defector_count:
            continue

        # get the number of defectors in that group from the map made earlier
        num_defectors_in_group = defector_count[current_user_subgroup]
        # update defector_cnt value for this user, to reflect the number of defectors in their group
        user_list[i].defector_cnt = num_defectors_in_group

    # 3. iterate through all defectors
    for i in defector_indices:
        # get current defector
        current_user = user_list[i]
        # 3a. If their secondary role is 'independent', they have defected.
        if current_user.sec_role == SecondaryRoleEnum.INDEPENDENT:
            # finalize defection
            sys_record.valid_remaining -= 1
            sys_record.defected_cnt += 1
            sys_record.skipped_cnt += 1

            remove_user(user_list, i, "3a. Primary role was defector, secondary role was independent.")
        
        if (current_user.sec_role == SecondaryRoleEnum.DEPENDENT):
            # 4a. If their secondary role is 'Dependent' and defector_cnt >= dependent_thres, finalize defection
            if (current_user.defector_cnt >= env_vars.dependent_thres):
                sys_record.valid_remaining -= 1
                sys_record.defected_cnt += 1
                sys_record.skipped_cnt += 1
                remove_user(user_list, i, "4a. Primary role was defector, secondary role was dependent, defector_cnt >= dependent_thres.")
            # 4b. If their secondary role is 'Dependent' and defector_cnt < dependent_thres, change their primary role to "low morale" and current status to "paid"
            else:
                current_user.pri_role = PrimaryRoleEnum.LOW_MORALE
                current_user.cur_status = CurrentStatusEnum.PAID

    # 5. If primary role = "Low-Morale" or "Unity" update cur_status to "PAID"
    for user in user_list:
        # the only three options are DEFECTOR, LOW_MORALE, and UNITY. So if it's not DEFECTOR, it's one of the other two.
        if (user.pri_role != PrimaryRoleEnum.DEFECTOR):
            user.cur_status = CurrentStatusEnum.PAID

    
    # 6. Calculate defection_shortfall = defected_cnt * cur_month_1st_calc --- This should be done in the setter for SystemVariable.
    # An assertion to ensure that the number is correct should suffice
    assert (sys_record.defection_shortfall == sys_record.defected_cnt * sys_record.cur_month_1st_calc), "something went wrong with the defection_shortfall calculation in UF1."

    # 7. same thing as 6 except calculates skip shortfall
    assert (sys_record.skip_shortfall == sys_record.skipped_cnt * sys_record.cur_month_1st_calc), "something went wrong with the skip_shortfall calculation in UF1."


#def remove_user(user_list, index, reason = "No reason provided."):
#    if not isinstance(index, int):
#        raise TypeError("Index must be an integer.")
#    if not isinstance(user_list, list):
#        raise TypeError("user_list must be a list.")
#    if not 0 <= index < len(user_list):
#        raise IndexError("Index out of bounds for user_list!")
#    #TODO: investigate if the reason parameter is needed
#    
#    for user in user_list:
#        if user.cur_sbg_num == user_list[index].cur_sbg_num:
#            user.members_cur_sbg -= 1
#        if user.orig_sbg_num == user_list[index].orig_sbg_num:
#            user.remaining_orig_sbg -= 1
#
#    user_list[index].cur_sbg_num = 0
#    user_list[index].members_cur_sbg = 0
#    user_list[index].sbg_status = ValidityEnum.NR 
#    user_list[index].cur_status = CurrentStatusEnum.NR 
#    user_list[index].payable = PayableEnum.NR
#    print(reason)

def test_uf1_determine_defectors(debugPrint = True):
    
    # Create a list of 100 distinct User_Record objects
    user_list = [User_Record(100, 0) for _ in range(100)]

    # subgroup setup for all the users
    data = subgroup_setup(len(user_list), user_list)
    
    # number of members in 4-member groups
    num_four_member_groups = data[0]
    
    # set up environment variables
    env_vars = Environemnt_Variables()
    env_vars.total_member_cnt = len(user_list)
    
    sys_record = System_Record(env_vars.total_member_cnt) 

    # assign roles
    role_assignment(env_vars, user_list, num_four_member_groups * 4) 
   
    # print out the results after role_assignment
#    for i in range(len(user_list)):
#        print("User " + str(i) + ": Primary = " + str(user_list[i].pri_role) + " | Secondary = " + str(user_list[i].sec_role))

    uf1_determine_defectors(env_vars, sys_record, user_list) 

    print(f"SR9 Defection Shortfall: {sys_record.defection_shortfall}")
    print(f"SR10 Skip Shortfall: {sys_record.skip_shortfall}")

    print(f"SR3 Defected Cnt: {sys_record.defected_cnt}")
    print(f"SR5 Skipped Cnt: {sys_record.skipped_cnt}")

test_uf1_determine_defectors()
