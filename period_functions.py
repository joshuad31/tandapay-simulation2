from utility import is_approx_equal
from user_record import *

def rsa_calculate_premiums(env_vars, sys_rec, user_list, period):
    if period == 0:
        for user in user_list:
            # the first premium calculation will be equal to the total coverage requirement
            # divided by the number of valid users. This is because the coverage requirement
            # is the total amount of money the insurance protocol needs to pay out, and the
            # number of valid users is basically the number of people paying. So, we distribute
            # the burden of paying cov_req equally amongst all members this way
            sys_rec.first_premium_calc = env_vars.cov_req / sys_rec.valid_remaining
            
            # for period 1 only, assign second_premium_calculation to first_premium_calculation
            user.second_premium_calc_list[period] = sys_rec.first_premium_calc             
    else:
        for user in user_list:
            # see explanation in comment above
            sys_rec.first_premium_calc = env_vars.cov_req / sys_rec.valid_remaining
            
            # second_premium_calc will be assigned to first_premium_calc + debt_to_savings (previous period)
            # - claim_refund - invalid_refund.
            user.second_premium_calc_list[period] = 0
            user.second_premium_calc_list[period] += sys_rec.first_premium_calc
            
            # move debt_to_savings_account from last period into second_premium_calc
            # reset debt_to_savings_account to zero.
            user.second_premium_calc_list[period] += user.debt_to_savings_account_list[period - 1]
            user.debt_to_savings_account_list[period - 1] = 0
            
            user.second_premium_calc_list[period] -= user.claim_refund
            user.second_premium_calc_list[period] -= user.invalid_refund

def rsb_payback_debt(env_vars, sys_rec, user_list, period):
    for user in user_list:
        user.premium_balance = sys_rec.shortfall_credit_individual + sys_rec.first_premium_calc

def rsc_calculate_shortfall(env_vars, sys_rec, user_list, period):
    # calculate shortfall_debt_total
    sys_rec.shortfall_debt_total = sys_rec.defection_shortfall
    sys_rec.shortfall_debt_total += sys_rec.skip_shortfall
    sys_rec.shortfall_debt_total += sys_rec.invalid_shortfall

    # calculate shortfall_debt_individual
    sys_rec.shortfall_debt_individual = sys_rec.shortfall_debt_total
    sys_rec.shortfall_debt_individual /= sys_rec.valid_remaining

    # calculate shortfall_credit_total
    sys_rec.shortfall_credit_total = sys_rec.skip_shortfall + sys_rec.invalid_shortfall
#    print(f"RSC: total_shortfall {sys_rec.shortfall_credit_total} = skip_shortfall {sys_rec.skip_shortfall} + invalid_shortfall {sys_rec.invalid_shortfall}")

    # calculate shortfall_credit_individual
    sys_rec.shortfall_credit_individual = sys_rec.shortfall_credit_total / sys_rec.valid_remaining
#    print(f"RSC: individual_shortfall {sys_rec.shortfall_credit_individual} = total_shortfall {sys_rec.shortfall_credit_total} / valid_remaining {sys_rec.valid_remaining}")

    # will sum the current month's balance for all users, for an error check at the end
    premium_balance_sum = 0
    
    # iterate through each user
    for user in user_list:
        # skip invalid users
        if user.sbg_status != ValidityEnum.VALID:
            continue
        
        # for each user, add individual shortfall to their "debt to savings account" for this period
        user.debt_to_savings_account_list[period] = sys_rec.shortfall_debt_individual
       
        # check for fatal error. This would cause them to get money without a claim.
#        if user.credit_to_savings_account < user.debt_to_savings_account_list[period]:
#            raise ValueError(f"Fatal Error: Credit to savings account ({user.credit_to_savings_account}) is less than debt to savings account ({user.debt_to_savings_account_list[period]})!")

        # update current month's balance
        user.premium_balance += sys_rec.shortfall_credit_individual

        # add to the sum
        premium_balance_sum += user.premium_balance
   
    # finally, make sure the sum of current month balances is equal to cov_req. If not, there is an error
    # NOTE: Due to the arithmetic being performed, sometimes there is a floating point error here. Hence approx equal function
    if not is_approx_equal(premium_balance_sum, env_vars.cov_req, 0.01):
        raise ValueError(f"Fatal Error: The sum of current month balances {premium_balance_sum} does not equal cov_req {env_vars.cov_req}! valid_remaining = {sys_rec.valid_remaining}, user[0].premium_balance = {user_list[0].premium_balance}")
            

#def RSC(env_vars, sys_rec, user_list, period):
#    if period == 0:
#        # calculate shortfall_debt_total
#        sys_rec.shortfall_debt_total = sys_rec.defection_shortfall
#        sys_rec.shortfall_debt_total += sys_rec.skip_shortfall
#        sys_rec.shortfall_debt_total += sys_rec.invalid_shortfall
#
#        # calculate shortfall_debt_individual
#        sys_rec.shortfall_debt_individual = sys_rec.shortfall_debt_total
#        sys_rec.shortfall_debt_individual /= sys_rec.valid_remaining
#
#        # calculate shortfall_credit_total
#        sys_rec.shortfall_credit_total = sys_rec.skip_shortfall + sys_rec.invalid_shortfall
#        print(f"RSC: total_shortfall {sys_rec.shortfall_credit_total} = skip_shortfall {sys_rec.skip_shortfall} + invalid_shortfall {sys_rec.invalid_shortfall}")
#
#        # calculate shortfall_credit_individual
#        sys_rec.shortfall_credit_individual = sys_rec.shortfall_credit_total / sys_rec.valid_remaining
#        print(f"RSC: individual_shortfall {sys_rec.shortfall_credit_individual} = total_shortfall {sys_rec.shortfall_credit_total} / valid_remaining {sys_rec.valid_remaining}")
#
#        # will sum the current month's balance for all users, for an error check at the end
#        premium_balance_sum = 0
#        
#        # iterate through each user
#        for user in user_list:
#            # skip invalid users
#            if user.sbg_status != ValidityEnum.VALID:
#                continue
#            
#            # for each user, add individual shortfall to their "debt to savings account" for this period
#            user.debt_to_savings_account_list[period] += sys_rec.shortfall_debt_individual
#           
#            # check for fatal error. This would cause them to get money without a claim.
#            if user.credit_to_savings_account < user.debt_to_savings_account_list[period]:
#                raise ValueError(f"Fatal Error: Credit to savings account ({user.credit_to_savings_account}) is less than debt to savings account ({user.debt_to_savings_account_list[period]})!")
#
#            # update current month's balance
#            user.premium_balance += sys_rec.shortfall_credit_individual
#
#            # add to the sum
#            premium_balance_sum += user.premium_balance
#       
#        # finally, make sure the sum of current month balances is equal to cov_req. If not, there is an error
#        # NOTE: Due to the arithmetic being performed, sometimes there is a floating point error here. Hence approx equal function
#        if not is_approx_equal(premium_balance_sum, env_vars.cov_req, 0.01):
#            raise ValueError(f"Fatal Error: The sum of current month balances {premium_balance_sum} does not equal cov_req {env_vars.cov_req}! valid_remaining = {sys_rec.valid_remaining}, user[0].premium_balance = {user_list[0].premium_balance}")
#    else:
#        # calculate shortfall_credit_total
#        sys_rec.shortfall_credit_total = sys_rec.skip_shortfall + sys_rec.invalid_shortfall
#        print(f"RSC: total_shortfall {sys_rec.shortfall_credit_total} = skip_shortfall {sys_rec.skip_shortfall} + invalid_shortfall {sys_rec.invalid_shortfall}")
#
#        # calculate shortfall_credit_individual
#        sys_rec.shortfall_credit_individual = sys_rec.shortfall_credit_total / sys_rec.valid_remaining
#        print(f"RSC: individual_shortfall {sys_rec.shortfall_credit_individual} = total_shortfall {sys_rec.shortfall_credit_total} / valid_remaining {sys_rec.valid_remaining}")
#
#        # will sum the current month's balance for all users, for an error check at the end
#        premium_balance_sum = 0
#        
#        # iterate through each user
#        for user in user_list:
#            # skip invalid users
#            if user.sbg_status != ValidityEnum.VALID:
#                continue
#           
#            # set user's debt to savings account equal to this month's individual shortfall
#            user.debt_to_savings_account_list[period] = sys_rec.shortfall_credit_individual
#          
#            # check for fatal error. This would cause them to get money without a claim.
#            if user.credit_to_savings_account < user.debt_to_savings_account_list[period]:
#                raise ValueError("Fatal Error: Credit to savings account is less than debt to savings account!")
#
#            # update current month's balance
#            user.premium_balance += sys_rec.shortfall_credit_individual
#
#            # add to the sum
#            premium_balance_sum += user.premium_balance
#
#        # finally, make sure the sum of current month balances is equal to cov_req. If not, there is an error
#        # NOTE: Due to the arithmetic being performed, sometimes there is a floating point error here. Hence approx_equal function
#        if not is_approx_equal(premium_balance_sum, env_vars.cov_req, 0.01):
#            raise ValueError(f"Fatal Error: The sum of current month balances {premium_balance_sum} does not equal cov_req {env_vars.cov_req}! valid_remaining = {sys_rec.valid_remaining}, user[0].premium_balance = {user_list[0].premium_balance}")
## Assuming ValidityEnum.VALID is defined elsewhere in the original code.
#
#def RSAB(env_vars, sys_rec, user_list, period):
#    # Shared variable
#    first_premium_calc = env_vars.cov_req / sys_rec.valid_remaining
#
#    # Iterate through each user
#    for i, user in enumerate(user_list):
#        # Skip if user is not active
#        if user.sbg_status != ValidityEnum.VALID:
#            continue
#
#        # Period 1 operations
#        if period == 0:
#            sys_rec.first_premium_calc = first_premium_calc
#            user.second_premium_calc_list[period] = first_premium_calc
#            user.premium_balance += first_premium_calc
#
#        # Period 2+ operations
#        else:
#            sys_rec.first_premium_calc = first_premium_calc
#
#            user.wallet_balance = (first_premium_calc + 
#                                   user.debt_to_savings_account_list[period - 1] - 
#                                   user.claim_refund - 
#                                   user.invalid_refund)
#            
#            user.second_premium_calc_list[period] = user.wallet_balance
#            user.wallet_balance = 0
#            user.total_value_refund_list[period] = user.claim_refund + user.invalid_refund
#
#            if user.premium_balance > sys_rec.first_premium_calc:
#                user.premium_balance = (user.second_premium_calc_list[period] - 
#                                          user.debt_to_savings_account_list[period - 1])
#                user.debt_to_savings_account_list[period] = 0
#            else:
#                user.premium_balance = user.second_premium_calc_list[period]
#
#            user.invalid_refund = 0
#            user.claim_refund = 0
#
##########################################################################
#
#
