import math

from enum import Enum
from userRecord import UserRecord

# subgroupSetup method. Documentation can be found at: https://www.notion.so/Subgroup-Setup-7e7852c10715423699fc522ca9e6536a
def subgroupSetup(total_member_cnt, user_list)
    assert isinstance(total_member_cnt, int), "total_member_cnt must be an integer!"
    assert isinstance(user_list, list), "user_list must be a list!"

    # step 2 calculations (number of 5-member groups)
    num_five_member_groups = total_member_cnt / 5
    num_five_member_groups /= 2.3333
    num_five_member_groups = round(num_five_member_groups)
    num_five_member_groups *= 5

    # step 3 calculations (remaining members)
    num_remaining_members = total_member_cnt - num_five_member_groups
    
    # step 4 calculations (number of 6-member groups)
    num_six_member_groups = num_remaining_members / 6
    num_six_member_groups /= 2
    num_six_member_groups = round(num_six_member_groups)
    num_six_member_groups *= 6

    # step 5 calculations (remaining members 2)
    num_remaining_members -= num_six_member_groups

    # step 6 calculations (number of 7-member groups)
    num_seven_member_groups = num_remaining_members / 7
    num_seven_member_groups /= 2
    num_seven_member_groups = math.floor(num_seven_member_groups)
    num_seven_member_groups *= 7

    # step 7 calculations (remaining members 3)
    num_remaining_members -= num_seven_member_groups

    # step 8 calculations (number of 4-member groups)
    num_four_member_groups = num_remaining_members / 4
    num_four_member_groups = math.floor(num_four_member_groups)
    num_remaining_members = num_remaining_members % 4

    # step 9 adjustments
    if num_remaining_members == 1:
        num_five_member_groups -= 1
        num_six_member_groups += 1
    elif num_remaining_members == 2:
        num_five_member_groups -= 1
        num_seven_member_groups += 1
    elif num_remaining_members == 3:
        num_five_member_groups -= 1
        num_four_member_groups += 2

    # step 10, assigning users to groups
        # Convert the number of groups from count of members to count of groups
    num_four_member_groups //= 4
    num_five_member_groups //= 5
    num_six_member_groups //= 6
    num_seven_member_groups //= 7

    # Initialize group number
    group_num = 1

    # Start assigning users to groups of size 4, then 5, etc.
    i = 0
    for num_groups, group_size in [(num_four_member_groups, 4), (num_five_member_groups, 5), 
                                   (num_six_member_groups, 6), (num_seven_member_groups, 7)]:
        for _ in range(num_groups):
            for _ in range(group_size):
                user = user_list[i]
                user.orig_sbg_num = group_num
                user.remaining_orig_sbg = group_size
                user.cur_sbg_num = group_num
                user.members_cur_sbg = group_size
                i += 1  # move to the next user
            group_num += 1

# unit test for subgroupSetup function
def test_subgroupSetup():
    # create a list of 100 userRecord objects
    user_list = [UserRecord() for _ in range(100)]

    # call your function with the user_list
    subgroupSetup(len(user_list), user_list)

    # check the users are correctly assigned to groups and the properties are set correctly
    group_num = 1
    group_size = 4
    for i, user in enumerate(user_list):
        if i % group_size == 0 and i > 0:
            group_num += 1
            if group_num <= num_four_member_groups:
                group_size = 4
            elif group_num <= num_four_member_groups + num_five_member_groups:
                group_size = 5
            elif group_num <= num_four_member_groups + num_five_member_groups + num_six_member_groups:
                group_size = 6
            else:
                group_size = 7
        assert user.orig_sbg_num == group_num, f"User at index {i} is in wrong group"
        assert user.remaining_orig_sbg == group_size, f"User at index {i} has wrong remaining group size"
        assert user.cur_sbg_num == group_num, f"User at index {i} has wrong current group number"
        assert user.members_cur_sbg == group_size, f"User at index {i} has wrong current group size"

    print("All tests passed!")


