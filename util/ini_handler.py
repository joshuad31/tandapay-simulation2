import os
import configparser

from simulation.environment_variables import Environment_Variables
from simulation.pricing_variables import Pricing_Variables
from simulation.other_variables import Other_Variables
from statistics.hypothesis_test import TestTypeEnum

# Define the class for handling .ini files
class INI_Handler:
    def __init__(self, path):
        self.path = path
        self.config = configparser.ConfigParser()
        
        # ensure that the directory exists. If not, make it
        directory = os.path.dirname(self.path)
        if not os.path.exists(directory):
            os.makedirs(directory)
        if not os.path.exists(self.path):
            open(self.path, 'w').close()
            self.write_environment_variables(Environment_Variables())
            self.write_pricing_variables(Pricing_Variables())
            self.write_other_variables(Other_Variables())

    def read_environment_variables(self):
        self.config.read(self.path)
        ev = Environment_Variables()

        # Reading and setting Environment_Variables
        ev.total_member_cnt = int(self.config.get('Environment_Variables', 'total_member_cnt'))
        ev.monthly_premium = float(self.config.get('Environment_Variables', 'monthly_premium'))
        
        # Reading percentages as integers and converting to float
        ev.chance_of_claim = int(self.config.get('Environment_Variables', 'chance_of_claim')) / 100
        ev.perc_honest_defectors = int(self.config.get('Environment_Variables', 'perc_honest_defectors')) / 100
        ev.perc_low_morale = int(self.config.get('Environment_Variables', 'perc_low_morale')) / 100
        ev.perc_independent = int(self.config.get('Environment_Variables', 'perc_independent')) / 100

        ev.dependent_thres = int(self.config.get('Environment_Variables', 'dependent_thres'))
        ev.queueing = int(self.config.get('Environment_Variables', 'queueing'))

        return ev

    def read_pricing_variables(self):
        self.config.read(self.path)
        pv = Pricing_Variables()

        pv.noref_change_floor        = float(self.config.get('Pricing_Variables', 'noref_change_floor')      ) / 100
        pv.noref_change_ceiling      = float(self.config.get('Pricing_Variables', 'noref_change_ceiling')    ) / 100
        pv.noref_ph_leave_floor      = float(self.config.get('Pricing_Variables', 'noref_ph_leave_floor')    ) / 100
        pv.noref_ph_leave_ceiling    = float(self.config.get('Pricing_Variables', 'noref_ph_leave_ceiling')  ) / 100
        pv.refund_change_floor       = float(self.config.get('Pricing_Variables', 'refund_change_floor')     ) / 100
        pv.refund_change_ceiling     = float(self.config.get('Pricing_Variables', 'refund_change_ceiling')   ) / 100
        pv.refund_ph_leave_floor     = float(self.config.get('Pricing_Variables', 'refund_ph_leave_floor')   ) / 100
        pv.refund_ph_leave_ceiling   = float(self.config.get('Pricing_Variables', 'refund_ph_leave_ceiling') ) / 100
        pv.avg_3mo_change_floor      = float(self.config.get('Pricing_Variables', 'avg_3mo_change_floor')    ) / 100
        pv.avg_3mo_change_ceiling    = float(self.config.get('Pricing_Variables', 'avg_3mo_change_ceiling')  ) / 100
        pv.avg_3mo_ph_leave_floor    = float(self.config.get('Pricing_Variables', 'avg_3mo_ph_leave_floor')  ) / 100
        pv.avg_3mo_ph_leave_ceiling  = float(self.config.get('Pricing_Variables', 'avg_3mo_ph_leave_ceiling')) / 100

        return pv

    def read_other_variables(self):
        self.config.read(self.path)
        ov = Other_Variables()

        ov.sample_size              = int(self.config.get('Other_Variables', 'sample_size'))
        ov.trial_sample_size        = int(self.config.get('Other_Variables', 'trial_sample_size'))
        ov.trial_count              = int(self.config.get('Other_Variables', 'trial_count'))
        ov.alpha                    = float(self.config.get('Other_Variables', 'alpha'))
        ov.test_type                = TestTypeEnum[self.config.get('Other_Variables', 'test_type')]
        ov.test_outcome             = str(self.config.get('Other_Variables', 'test_outcome'))
        ov.value_to_test            = float(self.config.get('Other_Variables', 'value_to_test'))

        return ov

    def write_environment_variables(self, ev):
        self.config['Environment_Variables'] = {
            'total_member_cnt': ev.total_member_cnt,
            'monthly_premium': ev.monthly_premium,
            'chance_of_claim': round(ev.chance_of_claim * 100),
            'perc_honest_defectors': round(ev.perc_honest_defectors * 100),
            'perc_low_morale': round(ev.perc_low_morale * 100),
            'perc_independent': round(ev.perc_independent * 100),
            'dependent_thres': ev.dependent_thres,
            'queueing': ev.queueing
        }
        

        with open(self.path, 'w') as configfile:
            self.config.write(configfile)

    def write_pricing_variables(self, pv):
        self.config['Pricing_Variables'] = {
            'noref_change_floor'       : round(pv.noref_change_floor       * 100),
            'noref_change_ceiling'     : round(pv.noref_change_ceiling     * 100),
            'noref_ph_leave_floor'     : round(pv.noref_ph_leave_floor     * 100),
            'noref_ph_leave_ceiling'   : round(pv.noref_ph_leave_ceiling   * 100),
            'refund_change_floor'      : round(pv.refund_change_floor      * 100),
            'refund_change_ceiling'    : round(pv.refund_change_ceiling    * 100),
            'refund_ph_leave_floor'    : round(pv.refund_ph_leave_floor    * 100),
            'refund_ph_leave_ceiling'  : round(pv.refund_ph_leave_ceiling  * 100),
            'avg_3mo_change_floor'     : round(pv.avg_3mo_change_floor     * 100),
            'avg_3mo_change_ceiling'   : round(pv.avg_3mo_change_ceiling   * 100),
            'avg_3mo_ph_leave_floor'   : round(pv.avg_3mo_ph_leave_floor   * 100),
            'avg_3mo_ph_leave_ceiling' : round(pv.avg_3mo_ph_leave_ceiling * 100)
        }
        with open(self.path, 'w') as configfile:
            self.config.write(configfile)

    def write_other_variables(self, ov):
        self.config['Other_Variables'] = {
            'sample_size'           : ov.sample_size,
            'trial_sample_size'     : ov.trial_sample_size,
            'trial_count'           : ov.trial_count,
            'alpha'                 : ov.alpha,
            'test_type'             : ov.test_type.name,
            'test_outcome'          : ov.test_outcome,
            'value_to_test'         : ov.value_to_test,
        }
        with open(self.path, 'w') as configfile:
            self.config.write(configfile)

if __name__ == "__main__":
    ev = Environment_Variables()
    pv = Pricing_Variables()
    ov = Other_Variables()

    ini_handler = INI_Handler("config/settings_test.ini")
    ini_handler.write_environment_variables(ev)
    ini_handler.write_pricing_variables(pv)
    ini_handler.write_other_variables(ov) 
