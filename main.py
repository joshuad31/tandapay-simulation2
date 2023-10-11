import ui
from simulation.simulation import *
from simulation.environment_variables import Environment_Variables
from simulation.pricing_variables import Pricing_Variables
from simulation.other_variables import *
from stats.statistics_runner import Statistics_Runner
from stats.searching import Searching
from util.ini_handler import INI_Handler
from util.results_db import Results_DB

class Main:
    def __init__(self):
        self.uic = ui.UI_Context()
        self.version = "v3.3.0"
        self.ini_handler = INI_Handler("config/settings.ini")
        
        # read config file
        self.uic.ev_obj = self.ini_handler.read_environment_variables()
        self.uic.pv_obj = self.ini_handler.read_pricing_variables()
        self.uic.ov_obj = self.ini_handler.read_other_variables()
        
        # set callbacks
        self.uic.run_simulation = self.run_simulation_callback
        self.uic.run_statistics = self.run_statistics_callback
        self.uic.run_searching = self.run_searching_callback
        self.uic.save_settings = self.save_settings_callback
        self.uic.run_debug = self.run_debug_callback
        self.uic.history = self.run_history_callback
        self.uic.about = self.run_about_callback

        self.uic.history_db_obj = Results_DB()

        ui.initialize(self.uic)

    def run_simulation_callback(self) -> str:
        results_aggregator = exec_simulation_multiple(self.uic.ev_obj, self.uic.pv_obj, self.uic.ov_obj.sample_size)
        result_str = results_aggregator.get_string()
        self.uic.history_db_obj.add_result("Simulation Run", self.version, result_str)
        return result_str

    def run_statistics_callback(self):
        statistics_runner = Statistics_Runner(self.uic.ev_obj, self.uic.pv_obj, self.uic.ov_obj)
        result_str = statistics_runner.get_string()
        self.uic.history_db_obj.add_result("Statistics Run", self.version, result_str)
        return statistics_runner.get_string()

    def run_searching_callback(self, attribute, target_percent, outcome, min_value, max_value, steps, order):
        searching = Searching(self.uic.ev_obj, self.uic.pv_obj, self.uic.ov_obj)
        result_str = searching.perform_full_search(attribute, target_percent, outcome, min_value, max_value, steps, order)
        self.uic.history_db_obj.add_result("Searching Run", self.version, result_str)
        return result_str 
    
    def run_debug_callback(self):
        result_dict = exec_simulation_debug(self.uic.ev_obj, self.uic.pv_obj)
        return f"""
        Result: {result_dict['result']}
        Wrote user record to CSV: {result_dict['user_csv_path']}
        Wrote system record to CSV: {result_dict['sys_csv_path']}
        """
    def save_settings_callback(self):
        self.ini_handler.write_environment_variables(self.uic.ev_obj)
        self.ini_handler.write_pricing_variables(self.uic.pv_obj)
        self.ini_handler.write_other_variables(self.uic.ov_obj)

    def run_history_callback(self):
        return "temporarily unavailable"

    def run_about_callback(self):
        return "temporarily unavailable"


if __name__ == "__main__":
    app = Main()
