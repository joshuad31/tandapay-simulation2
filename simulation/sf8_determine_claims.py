import random

from .user_record import *

def sf8_determine_claims(env_vars, user_list):
    probability = random.uniform(0, 1)
    if probability < env_vars.chance_of_claim:
        for user in user_list:
            if user.cur_status == CurrentStatusEnum.PAID:
                user.cur_month_premium += user.premium_balance
                user.premium_balance = 0
    else:
        for user in user_list:
            if user.cur_status == CurrentStatusEnum.PAID:
                user.wallet_claim_award += user.premium_balance
                user.premium_balance = 0
