
class EnvironmentVariables:
    def __init__(self):
        self._total_member_cnt = 0            # EV1: How many members are in the group?
        self._monthly_premium = 0             # EV2: Monthly premium
        self._chance_of_claim = 25            # EV3: What is the chance of a claim each month? (allowed values: 25 - 75)
        self._perc_honest_defectors = 10      # EV4: What is the percentage of honest defectors? (allowed values: 10 - 45)
        self._perc_low_morale = 10            # EV5: What is the percentage of low-morale members? (allowed values: 10 - 30)
        self._perc_independent = 20           # EV6: What is the percentage of members who are unwilling to act alone? (allowed values: 20 - 80)
        self._dependent_thres = 2             # EV7: What is the member threshold needed for dependent members to defect? (allowed values: 2, 3)
        self._low_morale_quit_prob = 1/3      # EV9: Probability a low-morale member will quit if forced to reorg (Must be 1/3)

    ### All member variables past this point must be calculated from the others:
        self._cov_req = 0                     # EV10: Coverage Requirement. (must be total_member_cnt * monthly_premium)

    # number of members in each primary role
        self._member_cnt_unity = 0            # Number of members with the primary role “Unity”
        self._member_cnt_defectors = 0        # Number of members with the primary role “Defector” 
        self._member_cnt_low_morale = 0       # Number of members with the primary role "Low Morale"
    
    # number of members in each secondary role   
        self._member_cnt_independent = 0      # Number of members with the secondary role "Independent"
        self._member_cnt_dependent = 0        # Number of members with the secondary role "Dependent"
    
    def calculate_member_variables(self):
        # calculate number of members in each primary role
        self._member_cnt_defectors = int(self._total_member_cnt * (self._perc_honest_defectors / 100))
        self._member_cnt_low_morale = int(self._total_member_cnt * (self._perc_low_morale / 100))
        self._member_cnt_unity = int((self._total_member_cnt - self._member_cnt_defectors) - self._member_cnt_low_morale)
        
        #calculate number of members in each secondary role
        self._member_cnt_independent = int(self._total_member_cnt * (self._perc_independent / 100))
        self._member_cnt_dependent = int(self._total_member_cnt - self._member_cnt_independent)
        
        # calculate coverage requirement
        self._cov_req = self._total_member_cnt * self._monthly_premium

    @property
    def total_member_cnt(self):
        return self._total_member_cnt
    
    @total_member_cnt.setter
    def total_member_cnt(self, cnt):
        assert isinstance(cnt, int), "attempting to set total_member_cnt in EV to non integer!"
        self._total_member_cnt = cnt
        self.calculate_member_variables()

    @property
    def monthly_premium(self):
        return self._monthly_premium

    @monthly_premium.setter
    def monthly_premium(self, premium):
        assert isinstance(premium, (int, float)), "attempting to set monthly_premium EV to non-numeric value!"
        self._monthly_premium = premium
        self.calculate_member_variables()

    @property
    def chance_of_claim(self):
        return self._chance_of_claim

    @chance_of_claim.setter
    def chance_of_claim(self, chance):
        assert isinstance(chance, (int, float)), "attempting to set chance_of_claim EV to non-numeric value!"
        if 25 <= chance <= 75:
            self._chance_of_claim = chance
            self.calculate_member_variables()
        else:
            raise ValueError("Chance of claim must be between 25 and 75")

    @property
    def perc_honest_defectors(self):
        return self._perc_honest_defectors

    @perc_honest_defectors.setter
    def perc_honest_defectors(self, perc):
        assert isinstance(perc, (int, float)), "attempting to set perc_honest_defectors EV to non-numeric value!"
        if 10 <= perc <= 45:
            self._perc_honest_defectors = perc
            self.calculate_member_variables()
        else:
            raise ValueError("Percent honest defectors must be between 10 and 45")

    @property
    def member_cnt_defectors(self):
        return self._member_cnt_defectors

    @property
    def perc_low_morale(self):
        return self._perc_low_morale

    @perc_low_morale.setter
    def perc_low_morale(self, perc):
        assert isinstance(perc, (int, float)), "attempting to set perc_low_morale EV to non-numeric value!"
        if 10 <= perc <= 30:
            self._perc_low_morale = perc
            self.calculate_member_variables()
        else:
            raise ValueError("Percentage of low morale members must be between 10 and 30")

    @property
    def member_cnt_low_morale(self):
        return self._member_cnt_low_morale

    @property
    def perc_independent(self):
        return self._perc_independent

    @perc_independent.setter
    def perc_independent(self, perc):
        assert isinstance(perc, (int, float)), "attempting to set perc_independent EV to non-numeric value!"
        if 20 <= perc <= 80:
            self._perc_independent = perc
            self.calculate_member_variables()
        else:
            raise ValueError("Percentage of independent members must be between 20 and 80")

    @property
    def member_cnt_dependent(self):
        return self._member_cnt_dependent

    @property
    def dependent_thres(self):
        return self._dependent_thres

    @dependent_thres.setter
    def dependent_thres(self, thres):
        assert isinstance(thres, int), "attempting to set dependent_thres to non-integer value!"
        if thres in [2, 3]:
            self._dependent_thres = thres
            self.calculate_member_variables()
        else:
            raise ValueError("Dependent threshold must be 2 or 3")

    @property
    def low_morale_quit_prob(self):
        return self._low_morale_quit_prob

    @low_morale_quit_prob.setter
    def low_morale_quit_prob(self, prob):
        assert isinstance(prob, (int, float)), "attempting to set low_morale_quit_prob to non-numeric value!"
        if prob == 1/3:
            self._low_morale_quit_prob = prob
            self.calculate_member_variables()
        else:
            raise ValueError("Low morale quit probability must be 1/3")

    @property
    def member_cnt_unity(self):
        return self._member_cnt_unity

    @property
    def member_cnt_independent(self):
        return self._member_cnt_independent

    @property
    def cov_req(self):
        return self._cov_req

