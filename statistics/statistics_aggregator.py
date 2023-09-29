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
from .statistics_attributes import statistics_attributes
from .confidence_interval import calculate_confidence_interval
from .hypothesis_test import perform_hypothesis_test
from .hypothesis_test import TestTypeEnum 


class Statistics_Aggregator:
    def __init__(self, ov):
        self.ov = ov
        
        # store the results aggregator object for each trial
        self.results = [None] * self.ov.trial_count
        self.results_added = 0
        self.mean_dict = {}
        self.std_dict = {}
        self.ci_dict = {}

        self._attributes = statistics_attributes

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
            self.calculate_stats()

    def calculate_stats(self):
        self.mean_dict = {}
        self.std_dict = {}

        if self.results_added != len(self.results):
            raise ValueError("Error: attempting to perform calculations in statistics aggregator before results have been added")

        for attribute in self._attributes:
            mean_value = sum([getattr(result, attribute) for result in self.results]) / self.ov.trial_count
            self.mean_dict[attribute] = mean_value
            
            std_value = math.sqrt(sum([(getattr(result, attribute) - mean_value) ** 2 for result in self.results]) / (self.ov.trial_count - 1))
            self.std_dict[attribute] = std_value

        self.calculate_confidence_intervals()

    def calculate_confidence_intervals(self):
        self.ci_dict = {}

        # Z-value for the confidence level
        z_value = norm.ppf(1 - self.ov.alpha / 2)

        for attribute in self._attributes:
            mean_value = self.mean_dict[attribute]
            std_value = self.std_dict[attribute]

            # Calculate the margin of error
            margin_of_error = z_value * (std_value / math.sqrt(self.ov.trial_count))

            # Calculate the confidence interval
            lower_bound = mean_value - margin_of_error
            upper_bound = mean_value + margin_of_error

            self.ci_dict[attribute] = (lower_bound, upper_bound)

    def calculate_hypothesis_test(self, attribute: str, null_value: float, test_type: TestTypeEnum):
        if attribute not in self._attributes:
            raise ValueError("Attempting to perform hypothesis test on an attribute that isn't in the statistics model.")

        p_value = perform_hypothesis_test(self.mean_dict[attribute], self.std_dict[attribute], self.ov.trial_count, null_value, test_type)

        operator_str = ""
        if test_type == TestTypeEnum.GREATER:
            operator_str = ">"
        elif test_type == TestTypeEnum.LESS:
            operator_str = "<"
        else:
            operator_str = "≠"
       
        math_str = f"with {(1 - self.ov.alpha)*100}% confidence that {attribute} {operator_str} {null_value}"
        
        if p_value < self.ov.alpha:
            return (p_value, f"We can say {math_str}")
        else:
            return (p_value, f"We can not say {math_str}")


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

    def get_string(self):
        if len(self.ci_dict) == 0 or len(self.std_dict) == 0 or len(self.mean_dict) == 0:
            self.calculate_stats()

        string = ""
        for attribute in self._attributes:
            string += f"""
            {attribute}:
            \tmean:                   {self.mean_dict[attribute]}
            \tstd. dev:               {self.std_dict[attribute]}
            \tconfidence interval:    {self.ci_dict[attribute]}
            """

        return string.replace("_", " ")
