import math

from enum import Enum
from user_record import User_Record

# subgroup_setup method. Documentation can be found at: https://www.notion.so/Subgroup-Setup-7e7852c10715423699fc522ca9e6536a
def subgroup_setup(total_member_cnt, user_list):
    assert isinstance(total_member_cnt, int), "total_member_cnt must be an integer!"
    assert isinstance(user_list, list), "user_list must be a list!"

    # step 2 calculations (number of 5-member groups)
    num_five_member_groups = total_member_cnt / 5
    num_five_member_groups = round(num_five_member_groups / 2.3333)
    num_members_in_five_member_group = num_five_member_groups * 5

    # step 3 calculations (remaining members)
    num_remaining_members = total_member_cnt - num_members_in_five_member_group
    
    # step 4 calculations (number of 6-member groups)
    num_six_member_groups = num_remaining_members / 6
    num_six_member_groups = round(num_six_member_groups / 2)
    num_members_in_six_member_group = num_six_member_groups * 6

    # step 5 calculations (remaining members 2)
    num_remaining_members -= num_members_in_six_member_group

    # step 6 calculations (number of 7-member groups)
    num_seven_member_groups = num_remaining_members / 7
    num_seven_member_groups = math.floor(num_seven_member_groups / 2)
    num_members_in_seven_member_group = num_seven_member_groups * 7

    # step 7 calculations (remaining members 3)
    num_remaining_members -= num_members_in_seven_member_group

    # step 8 calculations (number of 4-member groups)
    num_four_member_groups = num_remaining_members / 4
    num_four_member_groups = math.floor(num_four_member_groups)
    num_members_in_four_member_group = num_four_member_groups * 4
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
    
    # Initialize group number
    i = 0
    group_num = 1
    for num_groups, group_size in [(num_four_member_groups, 4), (num_five_member_groups, 5),
                                   (num_six_member_groups, 6) , (num_seven_member_groups, 7)]:
        for _ in range(num_groups):
            for _ in range(group_size):
                assert i < total_member_cnt, "i is greater than total_member_cnt"
                assert i < len(user_list), "i < total_member_cnt, but i >= len(user_list). len(user_list) should equal total_member_cnt"

                user = user_list[i]

                user.orig_sbg_num = group_num
                user.cur_sbg_num = group_num
                
                user.remaining_orig_sbg = group_size
                user.members_cur_sbg = group_size
                
                user_list[i] = user
                i += 1
            group_num += 1    

    return (num_four_member_groups, num_five_member_groups, num_six_member_groups, num_seven_member_groups)

# unit test for subgroup_setup function
def test_subgroup_setup_basic_print():
    # create a list of 100 userRecord objects
    user_list = [User_Record(100, 0) for _ in range(100)]

    # call your function with the user_list
    print("number of users: " + str(len(user_list)))
    data = subgroup_setup(len(user_list), user_list)

    num_four_member_groups = data[0]
    num_five_member_groups = data[1]
    num_six_member_groups = data[2]
    num_seven_member_groups = data[3]
    
    print("num_four_member_groups: " + str(num_four_member_groups))
    print("num_five_member_groups: " + str(num_five_member_groups))
    print("num_six_member_groups: " + str(num_six_member_groups))
    print("num_seven_member_groups: " + str(num_seven_member_groups))
    
    for i in range(len(user_list)):
        print("user " + str(i) + ": " + str(user_list[i].orig_sbg_num))
        

def test_subgroup_setup():
    # Create a list of 100 distinct User_Record objects
    user_list = [User_Record(100, 0) for _ in range(100)]

    # Call your function with the user_list
    data = subgroup_setup(len(user_list), user_list)

    num_four_member_groups = data[0]
    num_five_member_groups = data[1]
    num_six_member_groups = data[2]
    num_seven_member_groups = data[3]

    # Ensure that the correct number of groups have been created
    assert len(set(user.orig_sbg_num for user in user_list)) == num_four_member_groups + num_five_member_groups + num_six_member_groups + num_seven_member_groups

    # Ensure that each user is correctly assigned to their group
    for i in range(len(user_list)):
        group_size = user_list[i].remaining_orig_sbg
        assert group_size in [4, 5, 6, 7], "Group size is not correct"
        assert sum(user.orig_sbg_num == user_list[i].orig_sbg_num for user in user_list) == group_size, "User has been assigned to wrong group size"

    print("All tests passed!")

#test_subgroup_setup_basic_print()
#test_subgroup_setup()
