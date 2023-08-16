
def sf8_determine_claims(env_vars, user_list):
    probability = random.uniform(0, 1)
    if probability < env_vars.chance_of_claim:
        for user in user_list:
            if user.cur_status == CurrentStatusEnum.PAID:
                self.cur_month_premium += self.cur_month_balance
                self.cur_month_balance = 0
    else:
        for user in user_list:
            if user.cur_status == CurrentStatusEnum.PAID:
                user.wallet_claim_award += user.cur_month_balance
                user.cur_month_balance = 0
