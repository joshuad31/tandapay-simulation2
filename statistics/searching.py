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

class Result:
    def __init__(self, results_aggregator, attribute, value):
        self.percent_wins = results_aggregator.percent_wins
        self.percent_draws = results_aggregator.percent_draws
        self.percent_losses = results_aggregator.percent_losses
        self.attribute = attribute
        self.value = value

class Searching:

    def __init__(self, ev, pv, ov):
        self.ev = ev
        self.pv = pv
        self.ov = ov
        
        self._past_searches = {}

    def _test_bounds(self, obj, attribute, min_value, max_value):
        # ensure the object has the attribute
        if not hasattr(obj, attribute):
            raise AttributeError("invalid attribute in searching...")

        # if min > max, switch them so that (min < max) 
        if min_value > max_value:
            min_value, max_value = max_value, min_value

        # ensure that our min and max are within the bounds of acceptable values
        # for this attribute. Otherwise, set min_value=a, max_value=b
        a, b = obj.get_limits(attribute)

        if not (a <= min_value <= b):
            min_value = a
        if not (a <= max_value <= b):
            max_value = b
        
        # return a tuple with the new bounds
        return (min_value, max_value)

    def _perform_search(self, obj, attribute: str, min_value: float, max_value: float, steps: int):
        # test the min and max values to ensure they are in the correct bounds for the
        # attribute's allowed values.
        min_value, max_value = self._test_bounds(obj, attribute, min_value, max_value)
        
        # calculate step size
        step_size = (max_value - min_value) / steps

        # results array
        results = [None] * (steps+1)

        for i in range(steps+1):
            cur_attr_value = min_value + (i * step_size)
            setattr(obj, attribute, cur_attr_value)
            results_aggregator = exec_simulation_multiple(self.ev, self.pv, self.ov.trial_sample_size)
            results[i] = Result(results_aggregator, attribute, cur_attr_value)

        return results

    def basic_search(self, attribute: str, min_value, max_value, steps):
        if hasattr(self.ev, attribute):
            return self._perform_search(self.ev, attribute, min_value, max_value, steps)
        elif hasattr(self.pv, attribute):
            return self._perform_search(self.pv, attribute, min_value, max_value, steps)
        else:
            raise AttributeError("Error: passed an attribute to searching that is not in EV or PV")

    def get_linreg(self, attribute: str, min_value: float, max_value: float, steps: int, order: int):
        # Perform the search and get the results array
        results = self.basic_search(attribute, min_value, max_value, steps)

        # Extract percent_wins, percent_draws, percent_losses, and value into separate arrays
        percent_wins = np.array([result.percent_wins for result in results])
        percent_draws = np.array([result.percent_draws for result in results])
        percent_losses = np.array([result.percent_losses for result in results])
        values = np.array([result.value for result in results])

        # Fit the linear regression models
        coef_wins = np.polyfit(values, percent_wins, order)
        coef_draws = np.polyfit(values, percent_draws, order)
        coef_losses = np.polyfit(values, percent_losses, order)

        # Create a dictionary to hold the coefficients for easy access
        linreg_models = {
            "wins": coef_wins,
            "draws": coef_draws,
            "losses": coef_losses
        }

        raw_results = np.vstack((values, percent_wins, percent_draws, percent_losses))

        #print(raw_results.shape)

        return linreg_models, raw_results
    
    def perform_full_search(self, attribute, target_percent, outcome, min_value, max_value, steps, order):
        linreg_models, raw_results = self.get_linreg(attribute, min_value, max_value, steps, order) 

        coeffs = []
        roots = []
        # find the roots:
        if outcome is OutcomeEnum.WIN:
            coeffs = linreg_models["wins"]
        elif outcome is OutcomeEnum.DRAW:
            coeffs = linreg_models["draws"]
        elif outcome is OutcomeEnum.LOSS:
            coeffs = linreg_models["losses"]
        else:
            raise ValueError("Invalid OutcomeEnum passed to perform_full_search")
        
        # find the roots
        coeffs[-1] -= target_percent
        roots = np.roots(coeffs)
        coeffs[-1] += target_percent

        # filter out nonreal answers
        real_roots = [root.real for root in roots if np.isreal(root)]
        bounds = (0, 1)

        if hasattr(self.ev, attribute):
            bounds = self.ev.get_limits(attribute)  
        elif hasattr(self.pv, attribute):
            bounds = self.pv.get_limits(attribute)
        else:
            raise ValueError("Invalid attribute passed to perform_full_search")

        # filter out answers that are out of the domain
        possible_answers = [root for root in real_roots if (bounds[0] <= root <= bounds[1])]
        
        # start building a string to return as the output of this function
        header = "| {:<14} | {:<14} | {:<14} | {:<14} |\n".format("Value", "Wins Percent", "Draws Percent", "Losses Percent")
        
        # put the values in each row:
        rows = [None] * raw_results.shape[1]
        for row in range(raw_results.shape[1]):
            rows[row] = "| {:<14} | {:<14} | {:<14} | {:<14} |".format(round(raw_results[0][row], 6),
                                                                       round(raw_results[1][row], 6),
                                                                       round(raw_results[2][row], 6),
                                                                       round(raw_results[3][row], 6))
        
        # make a string for the linear regression algorithm
        coeff_strs = []
        for i, coeff in enumerate(coeffs):
            coeff_strs.append(f"{coeff}x^{len(coeffs)-1-i}")
            
        coeff_str = "y = " + "\n   + ".join(coeff_strs)

#        results_str = f"""
#        Initial Parameters:
#        \tattribute = {attribute}
#        \ttarget_percent = {target_percent}
#        \toutcome = {outcome.name}
#        \tmin_value = {min_value}
#        \tmax_value = {max_value}
#        \tsteps = {steps}
#        \torder = {order}
#        """

        results_str = ""
        #results_str += "\n"
        results_str += header
        results_str += "\n".join(rows)
        results_str += "\n\n"

        results_str += "All Roots:\n"
        for root in roots:
            results_str += f"\t{root}\n"

        results_str += "\nReal Roots:\n"
        for root in real_roots:
            results_str += f"\t{root}\n"

        results_str += "\nPossible Solutions:\n"
        for root in possible_answers:
            results_str += f"\t{root}\n"
        
        results_str += "\nLinreg Model:\n"
        results_str += coeff_str
        

        return results_str
        




