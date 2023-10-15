from .user_record import *

import random

def remove_user(user_list, index, reason = "No reason provided."):
    """
    removes a user from the user list. This involves altering the subgroup information
    of other users who are effected.

    :param user_list: takes in the list of users in this simulation run
    :param index: at what index user should be removed
    :param reason: reason user was removed (optional)
    """
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
    """
    Tests for equality with a margin of error

    :param a: floating point number 1
    :param b: floating point number 2
    :param epsilon: margin of error allowed
    :return: |a - b| < epsilon
    """
    return abs(a - b) < epsilon

def evaluate_probability(prob) -> bool:
    """
    evaluates a probability between 0 and 1. For example, if 0.5 is passed, it will
    return true 50% of the time and false 50% of the time.

    :param prob: probability to evaluate
    """

    #if not (0 <= prob <= 1):
    #    raise ValueError(f"attempting to run evaluate_probability on a probability outside of [0, 1]: prob={prob}")
    
    if prob <= 0:
        return False
    elif 1 <= prob:
        return True

    return random.uniform(0, 1) < prob
        

