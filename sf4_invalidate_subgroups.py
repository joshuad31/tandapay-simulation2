from system_record import System_Record
from user_record import *

def sf4_invalidate_subgroups(sys_rec, user_list, invalid_indices = []):
    
    if len(invalid_indices) > 0:
        print("Warning: non empty invalid_indices[] array passed to sf4! resetting to empty.")
        invalid_indices = []

    for i in range(len(user_list)):
        user = user_list[i]
        # 1. if members_cur_sbg = 1, 2, or 3
        if 1 <= user.members_cur_sbg <= 3:
            user.sbg_status = ValidityEnum.INVALID
            user.cur_status = CurrentStatusEnum.PAID_INVALID
            sys_rec.invalid_cnt += 1
            sys_rec.valid_remaining -= 1
            invalid_indices.append(i)

        # 2. set wallet_reorg_refund to cur_month_1st_calc
        user.wallet_reorg_refund = sys_rec.cur_month_1st_calc
        
        # 3. THIS STEP is incorrect and nolonger makes sense. User nolonger has this variable
        # user.cur_month_1st_calc = 0

    # Calculate individual shortfall -- this step should happen because invalid_cnt has a setter which will automatically calculate this variable.

    return invalid_indices
