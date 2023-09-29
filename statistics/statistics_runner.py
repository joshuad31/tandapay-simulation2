import numpy as np
from scipy.stats import norm
from enum import Enum

from simulation.other_variables import OutcomeEnum
from simulation.other_variables import Other_Variables
from simulation.environment_variables import *
from simulation.pricing_variables import *
from simulation.simulation import exec_simulation
from simulation.simulation import exec_simulation_multiple
from simulation.simulation_results import *
from .confidence_interval import calculate_confidence_interval
from .hypothesis_test import perform_hypothesis_test
from .hypothesis_test import TestTypeEnum
from .statistics_aggregator import Statistics_Aggregator

class Statistics_Runner:

    def __init__(self, ev, pv, ov):
        self.ev = ev
        self.pv = pv
        self.ov = ov
        
        # will store all the results
        self.statistics_aggregator = Statistics_Aggregator(self.ov) 
    
    def run(self, hypothesis_tests=None):
        self.statistics_aggregator = Statistics_Aggregator(self.ov) 

        # Running trials
        for trial in range(self.ov.trial_count):
            self.statistics_aggregator.add_result(exec_simulation_multiple(self.ev, self.pv, self.ov.trial_sample_size))
        
        #self.statistics_aggregator.print_dicts()
        
        #p_value, string = self.statistics_aggregator.calculate_hypothesis_test("num_wins", 30.0, TestTypeEnum.TWOTAILED)
        #print(f"p_value = {p_value}, result = {string}")

    def get_string(self):
        self.run()
        base_str = self.statistics_aggregator.get_string()
        
        p_value, legible_str = self.statistics_aggregator.calculate_hypothesis_test(self.ov.test_outcome, self.ov.value_to_test, self.ov.test_type)
        full_string = f"""{base_str}

            Hypothesis Test:
            \tp-value: {p_value}
            \tResult: {legible_str}
            """

        return full_string
