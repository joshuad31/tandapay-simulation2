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
from .statistics_aggregator import Statistics_Aggregator

class Statistics_Runner:

    def __init__(self, ev, pv, ov):
        self.ev = ev
        self.pv = pv
        self.ov = ov
        
        # will store all the results
        self.statistics_aggregator = Statistics_Aggregator(self.ov) 
    
    def run(self):
        self.statistics_aggregator = Statistics_Aggregator(self.ov) 

        # Running trials
        for trial in range(self.ov.trial_count):
            self.statistics_aggregator.add_result(exec_simulation_multiple(self.ev, self.pv, self.ov.trial_sample_size))
        
        self.statistics_aggregator.print_dicts()
