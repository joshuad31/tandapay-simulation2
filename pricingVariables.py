

class PricingVariables:
    def __init__(self):
        self._prem_inc_cum = 0                    # Premum price increase cumulative
        self._prem_inc_floor = 0                  # Premium Price increase floor
        self._prem_inc_ceiling = 0                # Premium Price increase ceiling
        
        self._ph_leave_cum = 0                    # Policyholders leave cumulative
        self._ph_leave_floor = 0                  # Policyholders leave floor
        self._ph_leave_ceiling = 0                # Policyholders leave ceiling

        self._pricing_slope = 0                   # Pricing Slope
        self._ph_skip_percentage = 0              # Percentage of policyholders that skip
        self._one_month_increase_percentage = 0   # Percentage increase in premiums for one month
        self._cumulative_increase_percentage = 0  # cumulative percentage increase in premiums
        
        
    # Getter and setter for prem_inc_cum
    @property
    def prem_inc_cum(self):
        return self._prem_inc_cum

    @prem_inc_cum.setter
    def prem_inc_cum(self, value):
        self._prem_inc_cum = value

    # Getter and setter for prem_inc_floor
    @property
    def prem_inc_floor(self):
        return self._prem_inc_floor

    @prem_inc_floor.setter
    def prem_inc_floor(self, value):
        self._prem_inc_floor = value

    # Getter and setter for prem_inc_ceiling
    @property
    def prem_inc_ceiling(self):
        return self._prem_inc_ceiling

    @prem_inc_ceiling.setter
    def prem_inc_ceiling(self, value):
        self._prem_inc_ceiling = value

    # Getter and setter for ph_leave_cum
    @property
    def ph_leave_cum(self):
        return self._ph_leave_cum

    @ph_leave_cum.setter
    def ph_leave_cum(self, value):
        self._ph_leave_cum = value

    # Getter and setter for ph_leave_floor
    @property
    def ph_leave_floor(self):
        return self._ph_leave_floor

    @ph_leave_floor.setter
    def ph_leave_floor(self, value):
        self._ph_leave_floor = value

    # Getter and setter for ph_leave_ceiling
    @property
    def ph_leave_ceiling(self):
        return self._ph_leave_ceiling

    @ph_leave_ceiling.setter
    def ph_leave_ceiling(self, value):
        self._ph_leave_ceiling = value

    # Getter and setter for pricing_slope
    @property
    def pricing_slope(self):
        return self._pricing_slope

    @pricing_slope.setter
    def pricing_slope(self, value):
        self._pricing_slope = value

    # Getter and setter for ph_skip_percentage
    @property
    def ph_skip_percentage(self):
        return self._ph_skip_percentage

    @ph_skip_percentage.setter
    def ph_skip_percentage(self, value):
        self._ph_skip_percentage = value

    # Getter and setter for one_month_increase_percentage
    @property
    def one_month_increase_percentage(self):
        return self._one_month_increase_percentage

    @one_month_increase_percentage.setter
    def one_month_increase_percentage(self, value):
        self._one_month_increase_percentage = value

    # Getter and setter for cumulative_increase_percentage
    @property
    def cumulative_increase_percentage(self):
        return self._cumulative_increase_percentage

    @cumulative_increase_percentage.setter
    def cumulative_increase_percentage(self, value):
        self._cumulative_increase_percentage = value
