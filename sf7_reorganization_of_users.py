

def sf7_reorganization_of_users(env_vars, sys_rec, user_list):
    paid_invalid_user_indices = []

    # subgroup info list. Contains the following info: (start index, group_size)
    # start index will be the first user in user_list with this subgroup. They should be stored
    # consecutively, so if a group of size 3 has start index i=10, the other 2 users are at i=11, i=12.
    # this list's index is the subgroup number. So, subgroup_info[10] gets the 10th group.
    subgroup_info = [None] * user_list[-1].cur_sbg_num + 1

    # generate a list of indices with all of the PAID INVALID users
    for i in range(len(user_list)):
        # build a list of paid invalid users
        if user_list[i].cur_status == CurrentStatusEnum.PAID_INVALID:
            paid_invalid_user_indices.append(i)
        
        # store info about the user's subgroup
        cur_sbg = user_list[i].cur_sbg_num;
        if subgroup_info[cur_sbg] == None:
            subgroup_info[cur_sbg] = (i, user_list[i].members_cur_sbg)


    for i in range(len(subgroup_info))

