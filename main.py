import ui
from simulation.simulation import *
from simulation.environment_variables import Environment_Variables
from simulation.pricing_variables import Pricing_Variables
from simulation.other_variables import *
from statistics.statistics_runner import Statistics_Runner
from util.ini_handler import INI_Handler

class Main:
    def __init__(self):
        self.uic = ui.UI_Context()
        self.ini_handler = INI_Handler("config/settings.ini")
        
        # read config file
        self.uic.ev_obj = self.ini_handler.read_environment_variables()
        self.uic.pv_obj = self.ini_handler.read_pricing_variables()
        self.uic.ov_obj = self.ini_handler.read_other_variables()
        
        # set callbacks
        self.uic.run_simulation = self.run_simulation_callback
        self.uic.run_statistics = self.run_statistics
        self.uic.history = self.run_history
        self.uic.about = self.run_about

        ui.initialize(self.uic)

    def run_simulation_callback(self) -> str:
        results_aggregator = exec_simulation_multiple(self.uic.ev_obj, self.uic.pv_obj, self.uic.ov_obj.sample_size)
        return results_aggregator.get_string()

    def run_statistics(self):
        statistics_runner = Statistics_Runner(self.uic.ev_obj, self.uic.pv_obj, self.uic.ov_obj)
        return statistics_runner.get_string()

    def run_history(self):
        return "temporarily unavailable"

    def run_about(self):
        return "temporarily unavailable"

if __name__ == "__main__":
    app = Main()
