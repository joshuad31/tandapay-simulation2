

def queueing_function(user_list):
    for user in user_list:
        queuing_length = len(user.prior_month_premium_list)

        # When Queuing = None or list has only 1 element
        if queuing_length == 1:
            if user.prior_month_premium_list[0] is not None:
                user.wallet_no_claim_refund = user.prior_month_premium_list[0]
            
            user.prior_month_premium_list[0] = user.cur_month_premium

        # When Queuing = 2
        elif queuing_length == 2:
            if user.prior_month_premium_list[1] is not None:
                user.wallet_no_claim_refund = user.prior_month_premium_list[1]
            
            user.prior_month_premium_list[1] = user.prior_month_premium_list[0]
            user.prior_month_premium_list[0] = user.cur_month_premium

        # When Queuing = 3
        elif queuing_length == 3:
            if user.prior_month_premium_list[2] is not None:
                user.wallet_no_claim_refund = user.prior_month_premium_list[2]
            
            user.prior_month_premium_list[2] = user.prior_month_premium_list[1]
            user.prior_month_premium_list[1] = user.prior_month_premium_list[0]
            user.prior_month_premium_list[0] = user.cur_month_premium

        # When Queuing = 4
        elif queuing_length == 4:
            if user.prior_month_premium_list[3] is not None:
                user.wallet_no_claim_refund = user.prior_month_premium_list[3]

            user.prior_month_premium_list[3] = user.prior_month_premium_list[2]
            user.prior_month_premium_list[2] = user.prior_month_premium_list[1]
            user.prior_month_premium_list[1] = user.prior_month_premium_list[0]
            user.prior_month_premium_list[0] = user.cur_month_premium
