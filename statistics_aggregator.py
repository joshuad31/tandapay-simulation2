import numpy as np
from scipy import stats

class Statistics_Aggregator:
    def __init__(self):
        self.wins_count = 0
        self.losses_count = 0
        self.draws_count = 0
        self.wins_squared = 0
        self.losses_squared = 0
        self.draws_squared = 0
        self.total_trials = 0

    def add_result(self, wins, losses, draws):
        self.wins_count += wins
        self.losses_count += losses
        self.draws_count += draws
        self.wins_squared += wins ** 2
        self.losses_squared += losses ** 2
        self.draws_squared += draws ** 2
        self.total_trials += 1

    def _mean(self, count):
        return count / self.total_trials

    def _std_dev(self, count, count_squared):
        mean = self._mean(count)
        return np.sqrt((count_squared / self.total_trials) - (mean ** 2))

    def distribution_estimates(self):
        win_mean = self._mean(self.wins_count)
        loss_mean = self._mean(self.losses_count)
        draw_mean = self._mean(self.draws_count)

        win_std_dev = self._std_dev(self.wins_count, self.wins_squared)
        loss_std_dev = self._std_dev(self.losses_count, self.losses_squared)
        draw_std_dev = self._std_dev(self.draws_count, self.draws_squared)

        return {
            'win': {'mean': win_mean, 'std_dev': win_std_dev},
            'loss': {'mean': loss_mean, 'std_dev': loss_std_dev},
            'draw': {'mean': draw_mean, 'std_dev': draw_std_dev},
        }

    def hypothesis_test(self, condition, alpha):
        dist_estimates = self.distribution_estimates()
        z_score = (condition['value'] - dist_estimates[condition['outcome']]['mean']) / dist_estimates[condition['outcome']]['std_dev']
        p_value = 2 * (1 - stats.norm.cdf(np.abs(z_score)))

        return {
            'z_score': z_score,
            'p_value': p_value,
            'reject_null': p_value < alpha
        }


    
