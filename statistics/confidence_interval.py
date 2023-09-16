import numpy as np
from scipy.stats import norm

def calculate_confidence_interval(mean, std_dev, sample_size, alpha):
    """
    Calculate the confidence interval for a given mean, standard deviation, sample size, and alpha level.

    Parameters:
    - mean: The sample mean
    - std_dev: The sample standard deviation
    - sample_size: The size of the sample
    - alpha: The alpha level for the confidence interval

    Returns:
    - (lower_bound, upper_bound): The lower and upper bounds of the confidence interval
    """
    # Calculate the Z-value for the given alpha level (two-tailed test)
    z_value = norm.ppf(1 - alpha / 2)

    # Calculate the margin of error
    margin_of_error = z_value * (std_dev / np.sqrt(sample_size))
    
    # Calculate the confidence intervals
    lower_bound = mean - margin_of_error
    upper_bound = mean + margin_of_error

    return lower_bound, upper_bound

