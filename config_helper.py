import os
import configparser

from environment_variables import Environment_Variables
from pricing_variables import Pricing_Variables

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

        # Reading and setting Pricing_Variables
        pv.prem_inc_cum = float(self.config.get('Pricing_Variables', 'prem_inc_cum')) / 100
        pv.prem_inc_floor = float(self.config.get('Pricing_Variables', 'prem_inc_floor')) / 100
        pv.prem_inc_ceiling = float(self.config.get('Pricing_Variables', 'prem_inc_ceiling')) / 100
        pv.ph_leave_cum = float(self.config.get('Pricing_Variables', 'ph_leave_cum')) / 100
        pv.ph_leave_floor = float(self.config.get('Pricing_Variables', 'ph_leave_floor')) / 100
        pv.ph_leave_ceiling = float(self.config.get('Pricing_Variables', 'ph_leave_ceiling')) / 100

        return pv

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
            'prem_inc_cum': round(pv.prem_inc_cum * 100),
            'prem_inc_floor': round(pv.prem_inc_floor * 100),
            'prem_inc_ceiling': round(pv.prem_inc_ceiling * 100),
            'ph_leave_cum': round(pv.ph_leave_cum * 100),
            'ph_leave_floor': round(pv.ph_leave_floor * 100),
            'ph_leave_ceiling': round(pv.ph_leave_ceiling * 100)
        }
        with open(self.path, 'w') as configfile:
            self.config.write(configfile)


if __name__ == "__main__":
    ev = Environment_Variables()
    pv = Pricing_Variables()

    ini_handler = INI_Handler("config/settings_test.ini")
    ini_handler.write_environment_variables(ev)
    ini_handler.write_pricing_variables(pv)
    
