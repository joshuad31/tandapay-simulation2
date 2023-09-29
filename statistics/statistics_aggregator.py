import numpy as np
from scipy.stats import norm
from enum import Enum
import math

from simulation.other_variables import OutcomeEnum
from simulation.other_variables import Other_Variables
from simulation.environment_variables import *
from simulation.pricing_variables import *
from simulation.simulation import exec_simulation
from simulation.simulation_results import *
from simulation.results_aggregator import *
from .confidence_interval import calculate_confidence_interval
from .hypothesis_test import perform_hypothesis_test

class Statistics_Aggregator:
    def __init__(self, ov):
        self.ov = ov
        
        # store the results aggregator object for each trial
        self.results = [None] * self.ov.trial_count
        self.results_added = 0
        self.mean_dict = {}
        self.std_dict = {}
        self.ci_dict = {}

        self._attributes = [
            "num_wins",
            "num_draws",
            "num_losses",
            "win_defector_stat",
            "win_skipped_stat",
            "win_invalid_stat",
            "win_quit_stat",
            "draw_defector_stat",
            "draw_skipped_stat",
            "draw_invalid_stat",
            "draw_quit_stat",
            "loss_defector_stat",
            "loss_skipped_stat",
            "loss_invalid_stat",
            "loss_quit_stat",
            "avg_defectors",
            "avg_skipped",
            "avg_invalid",
            "avg_quit",
        ]

    def add_result(self, result: Results_Aggregator):
        # if we try to pass it additional results after the
        # results array has been filled, raise an error
        if self.results_added >= len(self.results):
            raise IndexError("Attempting to add too many results to statistics aggregator!")

        self.results[self.results_added] = result
        self.results_added += 1

        # if we have filled the results array, calculate the
        # statistics on all of the results
        if self.results_added == len(self.results):
            self.calculate_stats(self._attributes)

    def calculate_stats(self, attributes: list[str]):
        self.mean_dict = {}
        self.std_dict = {}

        for attribute in attributes:
            mean_value = sum([getattr(result, attribute) for result in self.results]) / self.ov.trial_count
            self.mean_dict[attribute] = mean_value
            
            std_value = math.sqrt(sum([(getattr(result, attribute) - mean_value) ** 2 for result in self.results]) / (self.ov.trial_count - 1))
            self.std_dict[attribute] = std_value

    def calculate_confidence_intervals(self, alpha=0.05):
        self.ci_dict = {}

        # Z-value for the confidence level
        z_value = norm.ppf(1 - alpha / 2)

        for attribute in self._attributes:
            mean_value = self.mean_dict[attribute]
            std_value = self.std_dict[attribute]

            # Calculate the margin of error
            margin_of_error = z_value * (std_value / math.sqrt(self.ov.trial_count))

            # Calculate the confidence interval
            lower_bound = mean_value - margin_of_error
            upper_bound = mean_value + margin_of_error

            self.ci_dict[attribute] = (lower_bound, upper_bound)

    # this function is mainly for debugging
    def print_dicts(self):
        print("means:\n")

        for key, value in self.mean_dict.items():
            print(f"{key}: {value}")
        
        print("\nStandard Deviations:\n")

        for key, value in self.std_dict.items():
            print(f"{key}: {value}")

        print("\nConfidence Intervals:\n")
        if len(self.ci_dict) == 0:
            self.calculate_confidence_intervals()

        for key, value in self.ci_dict.items():
            print(f"{key}: {value}")
