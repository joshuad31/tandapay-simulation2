

def RSA(env_vars, sys_rec, user_list, period):
    # calculate current month's first calculation
    cur_month_first_calc = env_vars.cov_req / sys_rec.valid_remaining
    
    # perform operations for period 1
    if period == 0:
        # iterate through each user
        for i, user in enumerate(user_list):
            # skip user if user is not active
            if user.sbg_status != ValidityEnum.VALID
                continue
           
            # set user's cur_month_first_calc value
            user.cur_month_first_calc = cur_month_first_calc
            # for this period only: current month second calc = current month 1st calc   
            user.cur_month_second_calc_list[period] = cur_month_first_calc
    # perform operations for period 2+
    else:
        # iterate through each user
        for i, user in enumerate(user_list):
            # skip if user is not active
            if user.sbg_status != ValidityEnum.VALID:
                continue
            
            # set user's cur_month_first_calc value
            user.cur_month_first_calc = cur_month_first_calc
            # calculate credit to saving's account
            user.credit_to_savings_account = env_vars.cov_req / env_vars.total_member_cnt

            # determine wallet balance
            user.wallet_balance = cur_month_first_calc
            user.wallet_balance += debit_to_savings_account_list[period - 1]
            user.wallet_balance -= user.wallet_no_claim_refund
            user.wallet_balance -= user.wallet_reorg_refund
            
            # set current month second calculation for this period to wallet balance
            user.cur_month_second_calc_list[period] = user.wallet_balance
            # reset wallet balance to 0
            user.wallet_balance = 0

            # determine total_value_refund_period for this period to keep historical record moving forward
            user.total_value_refund_list[period] = user.wallet_no_claim_refund + user.wallet_reorg_refund

            # clean up of values
            user.wallet_reorg_refund = 0
            user.wallet_no_claim_refund = 0


def RSB(env_vars, sys_rec, user_list, period):
    # perform operations for period 1
    if period == 0:
        # iterate through active users
        for i, user in enumerate(user_list):
            # skip inactive user
            if user.sbg_status != ValidityEnum.VALID:
                continue

            # update current month balance
            user.cur_month_balance += cur_month_first_calc

    # perform operations for periods 2+
    else:
        # iterates through active users
        for i, user in enumerate(user_list):
            # skip inactive user
            if user.sbg_status != ValidityEnum.VALID:
                continue
            
            # if current month balance exceeds current month's first calculation:
            if user.cur_month_balance > user.cur_month_first_calc:
                # set to (cur month second calc [cur period]) - (debit to savings account [prev period])
                user.cur_month_balance = user.cur_month_second_calc_list[period]
                user.cur_month_balance -= user.debit_to_savings_account_list[period - 1]
                # set current period debit to savings account to 0
                user.debit_to_savings_account_list[period] = 0
            else:
                # otherwise, set current month balance to this period's current month second calculation 
                user.cur_month_balance = user.cur_month_second_calc_list[period]



#########################################################################









            
