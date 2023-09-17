

def queueing_function(user_list):
    for user in user_list:
        queueing_length = len(user.prior_month_premium_list)

        # When Queuing = None or list has only 1 element
        if queueing_length == 1:
            if user.prior_month_premium_list[0] is not None:
                user.claim_refund = user.prior_month_premium_list[0]

            user.prior_month_premium_list[0] = user.cur_month_premium

        # When Queuing = 2
        elif queueing_length == 2:
            if user.prior_month_premium_list[1] is not None:
                user.claim_refund = user.prior_month_premium_list[1]
            
            user.prior_month_premium_list[1] = user.prior_month_premium_list[0]
            user.prior_month_premium_list[0] = user.cur_month_premium

        # When Queuing = 3
        elif queueing_length == 3:
            if user.prior_month_premium_list[2] is not None:
                user.claim_refund = user.prior_month_premium_list[2]
            
            user.prior_month_premium_list[2] = user.prior_month_premium_list[1]
            user.prior_month_premium_list[1] = user.prior_month_premium_list[0]
            user.prior_month_premium_list[0] = user.cur_month_premium

        # When Queuing = 4
        elif queueing_length == 4:
            if user.prior_month_premium_list[3] is not None:
                user.claim_refund = user.prior_month_premium_list[3]

            user.prior_month_premium_list[3] = user.prior_month_premium_list[2]
            user.prior_month_premium_list[2] = user.prior_month_premium_list[1]
            user.prior_month_premium_list[1] = user.prior_month_premium_list[0]
            user.prior_month_premium_list[0] = user.cur_month_premium
