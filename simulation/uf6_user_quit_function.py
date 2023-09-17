import random

from .remove_user import remove_user
from .user_record import *

def uf6_user_quit_function(env_vars, sys_rec, user_list):
    paid_invalid_user_indices = []
    will_reorg = [] 

    # generate a list of indices with all of the PAID INVALID users
    if len(paid_invalid_user_indices) == 0:
        for i in range(len(user_list)):
            if user_list[i].cur_status == CurrentStatusEnum.PAID_INVALID:
                paid_invalid_user_indices.append(i)
   
    evaluate_for_quit = []
    # for each user with PAID_INVALID status
    for i in paid_invalid_user_indices:
        # if their primary role is LOW_MORALE
        if user_list[i].pri_role == PrimaryRoleEnum.LOW_MORALE:
            # use the low morale quit probability to determine if they are going to be evaluated for the quit list 
            random_number = random.uniform(0, 1)
            # member does not immediately quit:
            if random_number >= env_vars.low_morale_quit_prob:
                # they quit, so...
                
                # 1. increment sbg_reorg_cnt for all other members in the same subgroup
                increment_other_group_member_sbg_reorg_cnt(user_list, i)
                
                # 2. if their secondary role is independent, they reorg, remove from paid-invalid list
                if user_list[i].sec_role == SecondaryRoleEnum.INDEPENDENT:
                    # mark user to be removed from paid_invalid_user_indices:
                    will_reorg.append(i)

                # 3. if their secondary role is dependent, add them to the "evaluate for quit" list
                elif user_list[i].sec_role == SecondaryRoleEnum.DEPENDENT:
                    evaluate_for_quit.append(i)
            # member quits:
            else:
                # remove user
                remove_user(user_list, i, "member quits in user quit function due to low morale.")
                # increment quit count
                sys_rec.quit_cnt += 1 
        elif user_list[i].pri_role == PrimaryRoleEnum.UNITY:
            # increment sbg_reorg_cnt for all other users in the same group
            increment_other_group_member_sbg_reorg_cnt(user_list, i)
            # member will reorg
            will_reorg.append(i)
        else:
            assert user_list[i].pri_role != PrimaryRoleEnum.DEFECTOR, "ERROR: a defector somehow reached uf6."
    
    # evaluate quit list
    for i in evaluate_for_quit:
        if user_list[i].sbg_reorg_cnt >= 2:
            # add to reorg list
            will_reorg.append(i)
        else:
            # remove user
            remove_user(user_list, i, "removed in uf6 quit function")
            # increment quit count
            sys_rec.quit_cnt += 1

    # will_reorg will be returned.
    return (will_reorg, paid_invalid_user_indices)

# This is a helper function that runs when we need to increment the sbg_reorg_cnt for
# all the other members in the same subgroup as the member at user_list[index].
def increment_other_group_member_sbg_reorg_cnt(user_list, index):
    if not isinstance(user_list, list):
        raise TypeError("user_list is not of type list")
    if not isinstance(index, int):
        raise TypeError("index is not of type int")
    if not (0 <= index < len(user_list)):
        raise ValueError("index is not within the bounds of user_list")
    
    # get the subgroup number of the user
    sbg_num = user_list[index].cur_sbg_num

    # iterate through every user in the list
    for j in range(len(user_list)):
        # get current user's subgroup number
        other_sbg_num = user_list[j].cur_sbg_num
        # if the subgroup number is the same, AND it's a different user
        if (sbg_num == other_sbg_num) and (index != j):
            # increment sbg_reorg_cnt by 1.
            user_list[j].sbg_reorg_cnt += 1
           



