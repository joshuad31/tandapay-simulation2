

class EnvironmentVariables:
    def __init__(self):
        total_member_cnt = 0            # EV1: how many members are in the group?
        monthly_premium = 0             # EV2: Monthly Premium
        chance_of_claim = 25            # EV3: What is the chance of a claim each month (allowed values: 25 - 75)
        perc_honest_defectors = 10      # EV4: what is the percentage of honest defectors?
        member_cnt_defectors = 0        # TODO: no description
        perc_low_morale = 10            # EV5: What is the percentage of low-morale members?
        member_cnt_low_morale = 0       # TODO: no description
        perc_independent = 20           # EV6: What is the percentage of members who are unwilling to act alone? (allowed values: 20 - 80)
        member_cnt_dependent = 0        # TODO: no description
        dependent_thres = 2             # What is the member threshold needed for dependent members to defect? (allowed values: 2, 3)
        low_morale_quit_prob = 1/3      # EV9: Probability a low-morale member will quit if forced to reorg (must be 1/3)
        
        cov_req = total_member_cnt * monthly_premium    # EV10: Coverage Requirement
   
    def set_total_member_cnt(self, cnt):
        self.total_member_cnt = cnt
        self.cov_req = self.total_member_cnt * self.monthly_premium

    def set_monthly_premium(self, premium):
        self.monthly_premium = premium
        self.cov_req = self.total_member_cnt * self.monthly_premium

    def set_chance_of_claim(self, chance):
        if 25 <= chance <= 75:
            self.chance_of_claim = chance
        else:
            raise ValueError("chance of claim must be between 25 and 75")

    def set_perc_honest_defectors(self, perc):
        self.perc_honest_defectors = perc

    def set_member_cnt_defectors(self, cnt):
        self.member_cnt_defectors = cnt

    def set_perc_low_morale(self, perc):
        self.perc_low_morale = perc

    def set_member_cnt_low_morale(self, cnt):
        self.member_cnt_low_morale = cnt

    def set_perc_independent(self, perc):
        if 20 <= perc <= 80:
            self.perc_independent = perc
        else:
            raise ValueError("percentage of independent members must be between 20 and 80")

    def set_member_cnt_dependent(self, cnt):
        self.member_cnt_dependent = cnt

    def set_dependent_thres(self, thres):
        if thres in [2, 3]:
            self.dependent_thres = thres
        else:
            raise ValueError("dependent threshold must be 2 or 3")

    def set_low_morale_quit_prob(self, prob):
        if prob == 1/3:
            self.low_morale_quit_prob = prob
        else:
            raise ValueError("low morale quit probability must be 1/3")


