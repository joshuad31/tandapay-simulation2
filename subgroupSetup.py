import math

def subgroupSetup(total_member_cnt, user_list)
    assert isinstance(total_member_cnt, int), "total_member_cnt must be an integer!"
    assert isinstance(user_list, list), "user_list must be a list!"

    # step 2 calculations (number of 5-member groups)
    num_five_member_groups = total_member_cnt / 5
    num_five_member_groups /= 2.3333
    num_five_member_groups = round(num_five_member_groups)
    num_five_member_groups *= 5

    # step 3 calculations (remaining members)
    num_remaining_members = total_member_cnt - num_five_member_groups2
    
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
    if num_remaining_members == 1
        num_five_member_groups -= 1
        num_six_member_groups += 1
    elif num_remaining_members == 2
        num_five_member_groups -= 1
        num_seven_member_groups += 1
    elif num_remaining_members == 3
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


#### TODO: delete function below; function was only pasted here for reference while writing replacement function

def subgroup_setup(self):
    # ============================== Subgroup Setup ========================================
    step1_ev1 = self._total
    step2 = self._total / 5
    step3 = round(step2 / 2.3333)
    step4 = step3 * 5
    step5 = step1_ev1 - step4
    step6 = step5 / 6
    step7 = round(step6 / 2)
    step8 = step7 * 6
    step9 = step5 - step8
    step10 = step9 / 7
    step11 = int(step10 / 2)
    step12 = step11 * 7
    step13 = step9 - step12
    step14 = int(step13 / 4)
    step15 = step13 % 4
    if step15 == 1:
        step3 -= 1
        step7 += 1
    elif step15 == 2:
        step3 -= 1
        step11 += 1
    elif step15 == 3:
        step3 -= 1
        step14 += 2

    # Assigning number to the group, condition checking for group == 4
    group_num = 1
    group_mem_count = 0
    temp_val_four = step14 * 4
    offset = 0
    for i in range(temp_val_four):
        self.usr[i + offset]['orig_sbg_num'] = group_num
        self.usr[i + offset]['remaining_orig_sbg'] = 4
        self.usr[i + offset]['cur_sbg_num'] = group_num
        self.usr[i + offset]['members_cur_sbg'] = 4
        group_mem_count += 1
        if group_mem_count == 4:
            group_num += 1
            group_mem_count = 0
    offset += temp_val_four

    # condition checking for group == 5
    temp_val_five = step3 * 5
    for i in range(temp_val_five):
        self.usr[i + offset]['orig_sbg_num'] = group_num
        self.usr[i + offset]['remaining_orig_sbg'] = 5
        self.usr[i + offset]['cur_sbg_num'] = group_num
        self.usr[i + offset]['members_cur_sbg'] = 5
        group_mem_count += 1
        if group_mem_count == 5:
            group_num += 1
            group_mem_count = 0
    offset += temp_val_five

    # condition checking for group == 6
    temp_val_six = step7 * 6
    for i in range(temp_val_six):
        self.usr[i + offset]['orig_sbg_num'] = group_num
        self.usr[i + offset]['remaining_orig_sbg'] = 6
        self.usr[i + offset]['cur_sbg_num'] = group_num
        self.usr[i + offset]['members_cur_sbg'] = 6
        group_mem_count += 1
        if group_mem_count == 6:
            group_num += 1
            group_mem_count = 0
    offset += temp_val_six

    # condition checking for group == 7
    temp_val_seven = step11 * 7
    for i in range(temp_val_seven):
        self.usr[i + offset]['orig_sbg_num'] = group_num
        self.usr[i + offset]['remaining_orig_sbg'] = 7
        self.usr[i + offset]['cur_sbg_num'] = group_num
        self.usr[i + offset]['members_cur_sbg'] = 7
        group_mem_count += 1
        if group_mem_count == 7:
            group_num += 1
            group_mem_count = 0

    checksum = offset + temp_val_seven
    if checksum != self._total:
        raise ValueError(f"Initial group checksum failed: checksum:{checksum} != EV1:{self._total}")
    logger.debug({"D": temp_val_four, "A": temp_val_five, "B": temp_val_six, "C": temp_val_seven})

    logger.debug(
        f'Group4 members: {step14}, Group5 members: {step3}, Group6 members: {step7}, '
        f'Group7 members: {step11}, Total group: {step14 * 4 + step3 * 5 + step7 * 6 + step11 * 7}')
    return temp_val_four
