from user_record import *

import random

def remove_user(user_list, index, reason = "No reason provided."):
    if not isinstance(index, int):
        raise TypeError("Index must be an integer.")
    if not isinstance(user_list, list):
        raise TypeError("user_list must be a list.")
    if not 0 <= index < len(user_list):
        raise IndexError("Index out of bounds for user_list!")
    #TODO: investigate if the reason parameter is needed
    
    for user in user_list:
        if user.cur_sbg_num == user_list[index].cur_sbg_num:
            user.members_cur_sbg -= 1
        if user.orig_sbg_num == user_list[index].orig_sbg_num:
            user.remaining_orig_sbg -= 1

    user_list[index].cur_sbg_num = 0
    user_list[index].members_cur_sbg = 0
    user_list[index].sbg_status = ValidityEnum.NR 
    user_list[index].cur_status = CurrentStatusEnum.NR 
    user_list[index].payable = PayableEnum.NR
    #print(reason)

def is_approx_equal(a, b, epsilon):
    return abs(a - b) < epsilon

def evaluate_probability(prob) -> bool:
    #if not (0 <= prob <= 1):
    #    raise ValueError(f"attempting to run evaluate_probability on a probability outside of [0, 1]: prob={prob}")
    
    if prob <= 0:
        return False
    elif 1 <= prob:
        return True

    return random.uniform(0, 1) < prob
        

