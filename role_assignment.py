import random

from subgroup_setup import subgroup_setup
from environment_variables import Environment_Variables

from user_record import User_Record
from user_record import PrimaryRoleEnum
from user_record import SecondaryRoleEnum

def role_assignment(env_vars, user_list, num_members_in_four_member_group):
# Check validity of parameters passed to the function
    assert isinstance(env_vars, Environment_Variables), "env_vars must be of type EnvironmentVariables!"
    assert isinstance(user_list, list), "user_list must be a list!"
    assert isinstance(num_members_in_four_member_group, int), "num_members_in_four_member_group must be an int!"
    assert (env_vars.total_member_cnt == len(user_list)), "Error: total_member_cnt not equal to length of user_list!"

# Primary Role Assignment

    # This will result in a list of indices between 0 and total_member_cnt (which should be the size of user_list)
    # the size of the list will be member_cnt_defectors, basically allowing us to assign the users at each index
    # to the "defector" role, and thus we have randomly selected member_cnt_defectors defectors in user_list.
#    print(f"total member count: {env_vars.total_member_cnt}")
    defector_indices = random.sample(range(env_vars.total_member_cnt), env_vars.member_cnt_defectors)
    
    # This will store all of the indices that were not selected as defector indices, so that we can effectively
    # iterate over all defectors and all non-defectors independently later.
    non_defector_indices = [i for i in range(env_vars.total_member_cnt) if i not in defector_indices]

    # now, randomly sample users to be low-morale from the non_defector indices
    low_morale_indices = random.sample(non_defector_indices, env_vars.member_cnt_low_morale)
    
    # all indices that were not selected for low_morale, and thus also not selected for being a defector,
    # since low_morale were selected only from the list of non-defector indices
    unity_indices = [i for i in non_defector_indices if i not in low_morale_indices]
    
    # check to make sure the correct number were selected
    assert (len(unity_indices) == env_vars.member_cnt_unity), "Error: member_cnt_unity != len(unity_indices)"

    # assign each user's primary role
    for i in range(env_vars.total_member_cnt):
        if i in defector_indices:
            user_list[i].pri_role = PrimaryRoleEnum.DEFECTOR
        elif i in low_morale_indices:
            user_list[i].pri_role = PrimaryRoleEnum.LOW_MORALE
        elif i in unity_indices:
            user_list[i].pri_role = PrimaryRoleEnum.UNITY
        else:
            raise ValueError("Error: `i` selected that is not in defector_indices, low_morale_indices, or unity_indices.")

# Secondary Role Assignment
    
    # create a list with the indices for all dependent members
    dependent_indices = []
    if (env_vars.member_cnt_independent > 0):
        dependent_indices = random.sample(range(num_members_in_four_member_group, env_vars.total_member_cnt), env_vars.member_cnt_dependent - num_members_in_four_member_group)
    
    # ensure that it's the correct size
    assert ((env_vars.member_cnt_dependent - num_members_in_four_member_group) == len(dependent_indices)), f"length of dependent_indices {len(dependent_indices)} doesn't equal member_cnt_dependent {env_vars.member_cnt_dependent}."

    # Mark all users as dependent if they are in a four member group or 
    for i in range(env_vars.total_member_cnt):
        if (i < num_members_in_four_member_group) or (i in dependent_indices):
            user_list[i].sec_role = SecondaryRoleEnum.DEPENDENT 
        else:
            user_list[i].sec_role = SecondaryRoleEnum.INDEPENDENT

        if (i < num_members_in_four_member_group):
            assert (user_list[i].members_cur_sbg == 4), "In secondary role assignment, `i` should be a user in a 4-member subgroup, but user_list[i]'s members_cur_sbg variable is not equal to 4."

def test_role_assignment(b_printAllRoles):
    assert isinstance(b_printAllRoles, bool), "b_printAllRoles must be True or False!"

    # Create a list of 100 distinct User_Record objects
    user_list = [User_Record(100, 0) for _ in range(100)]

    # Call your function with the user_list
    data = subgroup_setup(len(user_list), user_list)

    num_four_member_groups = data[0]

    env_vars = EnvironmentVariables()
    env_vars.total_member_cnt = len(user_list)

    role_assignment(env_vars, user_list, num_four_member_groups * 4) 

    if(b_printAllRoles):
        for i in range(len(user_list)):
            print("User " + str(i) + ": Primary = " + str(user_list[i].pri_role) + " | Secondary = " + str(user_list[i].sec_role))

    num_unity = 0
    num_defectors = 0
    num_low_morale = 0

    num_dependent = 0
    num_independent = 0
    for i in range(len(user_list)):
        if user_list[i].pri_role == PrimaryRoleEnum.UNITY:
            num_unity += 1
        elif user_list[i].pri_role == PrimaryRoleEnum.DEFECTOR:
            num_defectors += 1
        elif user_list[i].pri_role == PrimaryRoleEnum.LOW_MORALE:
            num_low_morale += 1
        else:
            print("User " + str(i) + " has invalid primary role: " + str(user_list[i].pri_role))

        if user_list[i].sec_role == SecondaryRoleEnum.DEPENDENT:
            num_dependent += 1
        elif user_list[i].sec_role == SecondaryRoleEnum.INDEPENDENT:
            num_independent += 1
        else:
            print("User " + str(i) + " has invalid secondary role: " + str(user_list[i].sec_role))

    assert (num_unity == env_vars.member_cnt_unity), f"num_unity != env_vars.member_cnt_unity! num_unity: {num_unity}, env_vars.member_cnt_unity: {env_vars.member_cnt_unity}"
    assert (num_defectors == env_vars.member_cnt_defectors), f"num_defectors != env_vars.member_cnt_defectors! num_defectors: {num_defectors}, env_vars.member_cnt_defectors: {env_vars.member_cnt_defectors}"
    assert (num_low_morale == env_vars.member_cnt_low_morale), f"num_low_morale != env_vars.member_cnt_low_morale! num_low_morale: {num_low_morale}, env_vars.member_cnt_low_morale: {env_vars.member_cnt_low_morale}"
    assert (num_dependent == env_vars.member_cnt_dependent), f"num_dependent != env_vars.member_cnt_dependent! num_dependent: {num_dependent}, env_vars.member_cnt_dependent: {env_vars.member_cnt_dependent}"
    assert (num_independent == env_vars.member_cnt_independent), f"num_independent != env_vars.member_cnt_independent! num_independent: {num_independent}, env_vars.member_cnt_independent: {env_vars.member_cnt_independent}"

    print("passed all tests!")








