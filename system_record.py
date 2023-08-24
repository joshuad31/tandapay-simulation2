
class System_Record:
    def __init__(self, total_member_cnt):
        self._valid_remaining = total_member_cnt          # SysRec1:  Number of valid remembers remaining (init to EV1 a.k.a total_member_cnt)
        self._defected_cnt = 0                            # SysRec3:  Number of defected members (init to 0)
        self._skipped_cnt = 0                             # SysRec5:  Number of members skipped (init to 0)
        self._invalid_cnt = 0                             # SysRec6:  Number of invalid members (init to 0)
        self._reorged_cnt = 0                             # SysRec8:  Number of members that have reorged (init to 0) 
        self._quit_cnt = 0                                # SysRec7:  Number of members that quit (init to 0) 

        self._defection_shortfall = 0                     # SysRec9:  Fracture debt from defections (init to 0)
        self._invalid_shortfall = 0                       # SysRec12: Fracture debt from invalid new (init to 0)
        self._skip_shortfall = 0                          # SysRec10: Fracture debt from skips new (init to 0)
        
        self._shortfall_debt_individual = 0  
        self._shortfall_debt_total = 0        # Fracture Debt total (init to 0)
        self._cur_month_individual_shortfall = 0
        self._cur_month_total_shortfall = 0
        self._first_premium_calc = 0
        self._claimed = False

    def calculate_vars(self):
        self._defection_shortfall = self._defected_cnt * self._first_premium_calc
        self._skip_shortfall = self._skipped_cnt * self._first_premium_calc
        self._invalid_shortfall = self._invalid_cnt * self._first_premium_calc

    @property
    def valid_remaining(self):
        return self._valid_remaining

    @valid_remaining.setter
    def valid_remaining(self, value):
        self._valid_remaining = value

    @property
    def defected_cnt(self):
        return self._defected_cnt

    @defected_cnt.setter
    def defected_cnt(self, value):
        self._defected_cnt = value
        self.calculate_vars()

    @property
    def skipped_cnt(self):
        return self._skipped_cnt

    @skipped_cnt.setter
    def skipped_cnt(self, value):
        self._skipped_cnt = value
        self.calculate_vars()

    @property
    def invalid_cnt(self):
        return self._invalid_cnt

    @invalid_cnt.setter
    def invalid_cnt(self, value):
        self._invalid_cnt = value
        self.calculate_vars()

    @property
    def reorged_cnt(self):
        return self._reorged_cnt

    @reorged_cnt.setter
    def reorged_cnt(self, value):
        self._reorged_cnt = value
        self.calculate_vars()

    @property
    def quit_cnt(self):
        return self._quit_cnt

    @quit_cnt.setter
    def quit_cnt(self, value):
        self._quit_cnt = value
        self.calculate_vars()

    @property
    def defection_shortfall(self):
        return self._defection_shortfall

#    @defection_shortfall.setter
#    def defection_shortfall(self, value):
#        self._defection_shortfall = value

    @property
    def invalid_shortfall(self):
        return self._invalid_shortfall

#    @invalid_shortfall.setter
#    def invalid_shortfall(self, value):
#        self._invalid_shortfall = value
#        

    @property
    def skip_shortfall(self):
        return self._skip_shortfall

#    @skip_shortfall.setter
#    def skip_shortfall(self, value):
#        self._skip_shortfall = value

    @property
    def shortfall_debt_individual(self):
        return self._shortfall_debt_individual

    @shortfall_debt_individual.setter
    def shortfall_debt_individual(self, value):
        self._shortfall_debt_individual = value

    @property
    def shortfall_debt_total(self):
        return self._shortfall_debt_total

    @shortfall_debt_total.setter
    def shortfall_debt_total(self, value):
        self._shortfall_debt_total = value

    @property
    def cur_month_individual_shortfall(self):
        return self._cur_month_individual_shortfall

    @cur_month_individual_shortfall.setter
    def cur_month_individual_shortfall(self, value):
        self._cur_month_individual_shortfall = value

    @property
    def cur_month_total_shortfall(self):
        return self._cur_month_total_shortfall

    @cur_month_total_shortfall.setter
    def cur_month_total_shortfall(self, value):
        self._cur_month_total_shortfall = value

    @property
    def first_premium_calc(self):
        return self._first_premium_calc

    @first_premium_calc.setter
    def first_premium_calc(self, value):
        self._first_premium_calc = value
        self.calculate_vars()

    @property
    def claimed(self):
        return self._claimed

    @claimed.setter
    def claimed(self, value):
        self._claimed = value

