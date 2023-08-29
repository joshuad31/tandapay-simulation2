from system_record import System_Record
from user_record import *

def sf4_invalidate_subgroups(sys_rec, user_list):
    test_user = -1
    for i in range(len(user_list)):
        user = user_list[i]
        
        if user.sbg_status != ValidityEnum.VALID:
            continue

        # 1. if members_cur_sbg = 1, 2, or 3
        if 1 <= user.members_cur_sbg <= 3:
            user.sbg_status = ValidityEnum.INVALID
            sys_rec.valid_remaining -= 1
            user.cur_status = CurrentStatusEnum.PAID_INVALID
            sys_rec.invalid_cnt += 1
            user.invalid_refund = sys_rec.first_premium_calc
            user.first_premium_calc = 0
            test_user = i 

    return test_user
    # Calculate individual shortfall -- this step should happen because invalid_cnt has a setter which will automatically calculate this variable.

