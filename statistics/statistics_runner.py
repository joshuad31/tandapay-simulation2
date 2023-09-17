import numpy as np
from scipy.stats import norm
from enum import Enum

from simulation.other_variables import OutcomeEnum
from simulation.other_variables import Other_Variables
from simulation.environment_variables import *
from simulation.pricing_variables import *
from simulation.simulation import exec_simulation
from simulation.simulation_results import *
from .confidence_interval import calculate_confidence_interval
from .hypothesis_test import perform_hypothesis_test

class Statistics_Runner:

    def __init__(self, ev, pv, ov):
        self.ev = ev
        self.pv = pv
        self.ov = ov
        self.results = None  # Will hold the 2D numpy array of results
        self.probabilities = None # Will hold the probabilities of win/loss/draw for each trial

    def run(self):
        # Initialize a 2D numpy array with dimensions (trial_count, trial_sample_size)
        self.results = np.zeros((self.ov.trial_count, self.ov.trial_sample_size), dtype=object)

        # Running trials
        for trial in range(self.ov.trial_count):
            for sample in range(self.ov.trial_sample_size):
                # Execute the simulation and store the result
                simulation_result = exec_simulation(self.ev, self.pv)
                
                # store the result as an OutcomeEnum since we're not interested in the rest
                # of the data provided in the simulation_result object:
                if simulation_result.result in [ResultsEnum.WIN_A, ResultsEnum.WIN_B]:
                    self.results[trial, sample] = OutcomeEnum.WIN
                elif simulation_result.result in [ResultsEnum.LOSS_A, ResultsEnum.LOSS_B]:
                    self.results[trial, sample] = OutcomeEnum.LOSS
                elif simulation_result.result in [ResultsEnum.DRAW_A, ResultsEnum.DRAW_B]:
                    self.results[trial, sample] = OutcomeEnum.DRAW

    def calculate_probabilities(self):
        if self.results is None:
            self.run()

        # Initialize an array to hold the probabilities for each trial
        self.probabilities = np.zeros((self.ov.trial_count, 3))  # Each row: [P(WIN), P(LOSS), P(DRAW)]

        for trial in range(self.ov.trial_count):
            trial_results = self.results[trial, :]
            total_samples = len(trial_results)

            self.probabilities[trial, 0] = np.sum(trial_results == OutcomeEnum.WIN) / total_samples  # Replace 'WIN' with your actual identifier
            self.probabilities[trial, 1] = np.sum(trial_results == OutcomeEnum.LOSS) / total_samples  # Replace 'LOSS' with your actual identifier
            self.probabilities[trial, 2] = np.sum(trial_results == OutcomeEnum.DRAW) / total_samples  # Replace 'DRAW' with your actual identifier

    def get_mean_std(self):
        # Calculate the mean and standard deviation for win, loss, and draw probabilities
        if self.probabilities is None:
            self.calculate_probabilities()

        mean_probabilities = np.mean(self.probabilities, axis=0)
        std_probabilities = np.std(self.probabilities, axis=0)

        mean_dict = {
            OutcomeEnum.WIN:  mean_probabilities[0],
            OutcomeEnum.LOSS: mean_probabilities[1],
            OutcomeEnum.DRAW: mean_probabilities[2],
        }

        std_dict = {
            OutcomeEnum.WIN:  std_probabilities[0],
            OutcomeEnum.LOSS: std_probabilities[1],
            OutcomeEnum.DRAW: std_probabilities[2],
        }

        return mean_dict, std_dict

    def get_confidence_interval(self):
        # Calculate the mean and standard deviation first if not already calculated
        if self.probabilities is None:
            self.calculate_probabilities()

        mean_probabilities, std_probabilities = self.get_mean_std()
        
        # Create dictionaries to store the confidence intervals
        ci_lower_dict = {}
        ci_upper_dict = {}
        
        for outcome in [OutcomeEnum.WIN, OutcomeEnum.LOSS, OutcomeEnum.DRAW]:
            mean = mean_probabilities[outcome]
            stddev = std_probabilities[outcome]
            lower, upper = calculate_confidence_interval(mean, stddev, self.ov.trial_count, self.ov.alpha)

            ci_lower_dict[outcome] = lower
            ci_upper_dict[outcome] = upper

        return ci_lower_dict, ci_upper_dict

    def get_hypothesis_test(self):
        # calculate mean and std.dev if not calculated
        if self.probabilities is None:
            self.calculate_probabilities()

        mean_probabilities, std_probabilities = self.get_mean_std()

        mean = mean_probabilities[self.ov.test_outcome]
        std = std_probabilities[self.ov.test_outcome]

#        print(f"mean: {mean}, std: {std}, value to test: {self.ov.value_to_test}")
        p_value = perform_hypothesis_test(mean, std, self.ov.trial_count, self.ov.value_to_test, self.ov.test_type)
#        print(f"p-value: {p_value}")

        if p_value < self.ov.alpha:
            return (True, p_value)


        return (False, p_value)

    def get_string(self):
        mean_dict, std_dict = self.get_mean_std()
        ci_lower_dict, ci_upper_dict = self.get_confidence_interval()
        reject_null, p_value = self.get_hypothesis_test()

        return f"""
            Mean:
            \twins:   {mean_dict[OutcomeEnum.WIN]:.4f}
            \tdraws:  {mean_dict[OutcomeEnum.DRAW]:.4f}
            \tlosses: {mean_dict[OutcomeEnum.LOSS]:.4f}

            Standard Deviation:
            \twins:   {std_dict[OutcomeEnum.WIN]:.4f}
            \tdraws:  {std_dict[OutcomeEnum.DRAW]:.4f}
            \tlosses: {std_dict[OutcomeEnum.LOSS]:.4f}

            Confidence Intervals:
            \twins:   ({ci_lower_dict[OutcomeEnum.WIN]:.4f}, {ci_upper_dict[OutcomeEnum.WIN]:.4f})
            \tdraws:  ({ci_lower_dict[OutcomeEnum.DRAW]:.4f}, {ci_upper_dict[OutcomeEnum.DRAW]:.4f})
            \tlosses: ({ci_lower_dict[OutcomeEnum.LOSS]:.4f}, {ci_upper_dict[OutcomeEnum.LOSS]:.4f})
        
            Hypothesis Test:
            \treject null: {reject_null}
            \tp-value: {p_value:.4f}

            Note: This section is not complete. This is a test release.
        """

if __name__ == "__main__":
    statistics_runner = Statistics_Runner(Environment_Variables(), Pricing_Variables(), Other_Variables())
    mean_dict, std_dict = statistics_runner.get_mean_std()
    ci_lower_dict, ci_upper_dict = statistics_runner.get_confidence_interval()

    if statistics_runner.get_hypothesis_test():
        print("we can say with 95% confidence that the proportion of wins ≠ 0.50 (50%)")
    else:
        print("we cannot say with 95% confidence that the proportion of wins ≠ 0.50 (50%)")

    print(mean_dict)
    print(std_dict)
    print(ci_lower_dict)
    print(ci_upper_dict)
