from .user_record import *

import random
import heapq
import pdb

class group_data:
    """
    encapsulates a group object. used for sf7 combining algorithm
    """
    def __init__(self, group_num, group_size, indices = []):
        self.group_num = group_num
        self.group_size = group_size
        self.indices = indices


    def __str__(self):
        return f"({self.group_num}, {self.group_size}, {self.indices})"

    def __repr__(self):
        return f"({self.group_num}, {self.group_size}, {self.indices})"

def combine_size(group_list, group_size, potential_sizes, reorged = None):
    """
    helper function for sf7 combining algorithm. Combines members in a group of
    size group_size with groups in potential sizes, prioritizing groups of size
    potential_sizes[i] over potential_sizes[i+1].

    :param group_list: list of all the groups
    :param group_size: size to combine
    :param potential_sizes: list of sizes to combine with, ordered from greatest to least priority
    :param reorged: Do not use this parameter. Used for the array that stores reorged users

    :return: altered group list
    """
    # store all of the members who were reorged into larger groups
    if reorged is None:
        reorged = []

    # group_size_indices[group_size][...indices of groups of that size...]
    group_size_indices = [set() for _ in range(8)]
    
    # list of tuples of groups to be combined. (i, j) means that groups
    # group_list[i] and group_list[j] are to be combined
    to_combine = []

    # build the group_size_indices list
    for i, group in enumerate(group_list):
        #print(f"group.group_size = {group.group_size}")
        group_size_indices[group.group_size].add(i)

    # if the set has elements, that means there are groups of this size to be processed
    while group_size_indices[group_size]:
        # pop a group off out of the set to be processed
        i = group_size_indices[group_size].pop()   

        # try to combine it with another group of one of the sizes in potential_sizes.
        # potential sizes is ordered from 1st priority -> last priority
        for other_size in potential_sizes:
            # if there are no groups of other_size to combine it with, continue to the next size
            if not group_size_indices[other_size]:
                continue
             
            # otherwise, select another group to combine it with
            j = group_size_indices[other_size].pop()
            
            # now, because of the pop statements, both groups have been removed from the pool.
            # and we can simply add them to the list to be combined.
            to_combine.append((i, j))

            # do this to track which members were in a group smaller than 4 members, and were
            # reorged into a larger group
            reorged.append(i)

            # break out so we don't accidentally combine the same group twice
            break

    # combine the groups, delete the old ones, and add the new one to the group_list

#    print(f"group_list: {group_list}")
#    print(f"to_combine: {to_combine}")
    to_remove = []
    to_append = []
    for groups in to_combine:
        group1 = groups[0]
        group2 = groups[1]
        new_group = combine_groups(group_list[group1], group_list[group2])
        
#        to_remove.append(group1)
#        to_remove.append(group2)
        group_list[group1] = None
        group_list[group2] = None
        to_append.append(new_group)
        #del group_list[group1]
        #del group_list[group2]
        #group_list.append(new_group)

    for g in to_append:
        group_list.append(g)

    group_list = [elem for elem in group_list if elem is not None]

#    print(f"group_list at end: {group_list}")
    return group_list

def combine_groups(group1, group2):
    new_num = 0
    new_size = group1.group_size + group2.group_size
    new_indices = group1.indices + group2.indices

    if new_size > 7:
        print(f"GROUP OF SIZE GREATER THAN 7 BEING CREATED:")
        print(f"group1: {group1}\ngroup2: {group2}")
        print(f"NEW SIZE: {new_size}")

    if group1.group_size == group2.group_size:
        new_num = random.choice([group1.group_num, group2.group_num])
    elif group1.group_size > group2.group_size:
        new_num = group1.group_num
    else:
        new_num = group2.group_num

    return group_data(new_num, new_size, new_indices)

# Unit test:
def test_combine_size():
    groups = [
        group_data(1, 3, [0, 1, 2]),
        group_data(2, 4, [3, 4, 5, 6]),
        group_data(3, 2, [7, 8]),
        group_data(4, 2, [9, 10]),
        group_data(5, 4, [11, 12, 13, 14])
    ]

    pdb.set_trace()
    groups = combine_size(groups, 3, [2, 3, 4])
    groups = combine_size(groups, 2, [3, 4, 5])
    groups = combine_size(groups, 1, [4, 5, 6])

    for group in groups:
        print(f"Group {group.group_num} of size {group.group_size} with indices: {group.indices}")

def sf7_reorganization_of_users(env_vars, sys_rec, user_list, tracking = -1):
    """
    system function 7 implementation. reorganizes users who are in an invalid group size.

    :param env_vars: takes in the simulation environment variables
    :param sys_rec: takes in simulation's system record
    :param user_list: takes in simulation's user list
    :param tracking: unused optional parameter, leave this field blank
    """
    groups = [None] * len(user_list)
    for i, user in enumerate(user_list):
        # skip invalid user
        if user.sbg_status == ValidityEnum.NR:
            continue
        
        # build the groups list 
        if groups[user.cur_sbg_num] == None:
            groups[user.cur_sbg_num] = group_data(user.cur_sbg_num, user.members_cur_sbg, [i])
        else:
            groups[user.cur_sbg_num].indices.append(i)
    
    # filter the list to only have valid groups, no "none" elements
    groups = [x for x in groups if x is not None]

#    breakpoint()

    # perform the reorganization operation
    groups = combine_size(groups, 3, [2, 3, 4])
    groups = combine_size(groups, 2, [3, 4, 5])
    groups = combine_size(groups, 1, [4, 5, 6])
    
    # extrapolate data from reorganized groups back into users

    for group in groups:
#        print(f"group: {group}")
        for i in group.indices:
            if tracking == i:
                print(f"tracked user: group = {group}, members_cur_sbg = {user_list[i].members_cur_sbg}")

            # if this is true, that means they reorged. Perform
            # the following operations only for users who have reorged...
            if user_list[i].members_cur_sbg < 4:
                # set their status to reorg
                user_list[i].cur_status = CurrentStatusEnum.REORG
                # increment their reorged_cnt variable (number of times this user in particular has reorged)
                user_list[i].reorged_cnt += 1
                # increment system reorged_cnt (total number of times users have reorged)
                sys_rec.reorged_cnt += 1
                # increment valid_remaining
                sys_rec.valid_remaining += 1
            
            # perform these operations for every user in the subgroup
            user_list[i].cur_sbg_num = group.group_num
            user_list[i].members_cur_sbg = group.group_size
            user_list[i].sbg_status = ValidityEnum.VALID
            






