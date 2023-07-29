
class EnvironmentVariables:

    def __init__(self):
        self._total_member_cnt = 0            # EV1: How many members are in the group?
        self._monthly_premium = 0             # EV2: Monthly premium
        self._chance_of_claim = 25            # EV3: What is the chance of a claim each month? (allowed values: 25 - 75)
        self._perc_honest_defectors = 10      # EV4: What is the percentage of honest defectors? (allowed values: 10 - 45)
        self._member_cnt_defectors = 0        # TODO: no description
        self._perc_low_morale = 10            # EV5: What is the percentage of low-morale members? (allowed values: 10 - 30)
        self._member_cnt_low_morale = 0       # TODO: no description
        self._perc_independent = 20           # EV6: What is the percentage of members who are unwilling to act alone? (allowed values: 20 - 80)
        self._member_cnt_dependent = 0        # TODO: no description
        self._dependent_thres = 2             # EV7: What is the member threshold needed for dependent members to defect? (allowed values: 2, 3)
        self._low_morale_quit_prob = 1/3      # EV9: Probability a low-morale member will quit if forced to reorg (Must be 1/3)
                                                                        
        self._cov_req = self._total_member_cnt * self._monthly_premium  # EV10: Coverage Requirement. (must be total_member_cnt * monthly_premium)

    @property
    def total_member_cnt(self):
        return self._total_member_cnt
    
    @total_member_cnt.setter
    def total_member_cnt(self, cnt):
        self._total_member_cnt = cnt
        self._cov_req = self._total_member_cnt * self._monthly_premium

    @property
    def monthly_premium(self):
        return self._monthly_premium

    @monthly_premium.setter
    def monthly_premium(self, premium):
        self._monthly_premium = premium
        self._cov_req = self._total_member_cnt * self._monthly_premium

    @property
    def chance_of_claim(self):
        return self._chance_of_claim

    @chance_of_claim.setter
    def chance_of_claim(self, chance):
        if 25 <= chance <= 75:
            self._chance_of_claim = chance
        else:
            raise ValueError("Chance of claim must be between 25 and 75")

    @property
    def perc_honest_defectors(self):
        return self._perc_honest_defectors

    @perc_honest_defectors.setter
    def perc_honest_defectors(self, perc):
        if 10 <= perc <= 45:
            self._perc_honest_defectors = perc
        else:
            raise ValueError("Percent honest defectors must be between 10 and 45")

    @property
    def member_cnt_defectors(self):
        return self._member_cnt_defectors

    @member_cnt_defectors.setter
    def member_cnt_defectors(self, cnt):
        self._member_cnt_defectors = cnt

    @property
    def perc_low_morale(self):
        return self._perc_low_morale

    @perc_low_morale.setter
    def perc_low_morale(self, perc):
        if 10 <= perc <= 30:
            self._perc_low_morale = perc
        else:
            raise ValueError("Percentage of low morale members must be between 10 and 30")

    @property
    def member_cnt_low_morale(self):
        return self._member_cnt_low_morale

    @member_cnt_low_morale.setter
    def member_cnt_low_morale(self, cnt):
        self._member_cnt_low_morale = cnt

    @property
    def perc_independent(self):
        return self._perc_independent

    @perc_independent.setter
    def perc_independent(self, perc):
        if 20 <= perc <= 80:
            self._perc_independent = perc
        else:
            raise ValueError("Percentage of independent members must be between 20 and 80")

    @property
    def member_cnt_dependent(self):
        return self._member_cnt_dependent

    @member_cnt_dependent.setter
    def member_cnt_dependent(self, cnt):
        self._member_cnt_dependent = cnt

    @property
    def dependent_thres(self):
        return self._dependent_thres

    @dependent_thres.setter
    def dependent_thres(self, thres):
        if thres in [2, 3]:
            self._dependent_thres = thres
        else:
            raise ValueError("Dependent threshold must be 2 or 3")

    @property
    def low_morale_quit_prob(self):
        return self._low_morale_quit_prob

    @low_morale_quit_prob.setter
    def low_morale_quit_prob(self, prob):
        if prob == 1/3:
            self._low_morale_quit_prob = prob
        else:
            raise ValueError("Low morale quit probability must be 1/3")

    @property
    def cov_req(self):
        return self._cov_req

