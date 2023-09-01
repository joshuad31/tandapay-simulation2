from simulation_results import *

class Results_Aggregator:
    def __init__(self, sample_size, store_results = False):
        # will store results here if store_results = True
        self.results = []
        self.results_added = 0
        
        # sample size used in average calculations:
        self.sample_size = sample_size
        self.store_results = store_results

        # tracking various outcomes of the simulation
        self.num_wins_case_a = 0
        self.num_wins_case_b = 0
        self.num_draws_case_a = 0
        self.num_draws_case_b = 0
        self.num_losses_case_a = 0
        self.num_losses_case_b = 0

        # tracking defectors
        self.avg_defectors = 0
        self.min_defectors = 1e99
        self.max_defectors = 0
        self.result_on_min_defectors = None
        self.result_on_max_defectors = None

        # tracking skipped
        self.avg_skipped = 0
        self.min_skipped = 1e99
        self.max_skipped = 0
        self.result_on_min_skipped = None
        self.result_on_max_skipped = None
        
        # tracking invalid
        self.avg_invalid = 0
        self.min_invalid = 1e99
        self.max_invalid = 0
        self.result_on_min_invalid = None
        self.result_on_max_invalid = None
        
        # tracking quit
        self.avg_quit = 0
        self.min_quit = 1e99
        self.max_quit = 0
        self.result_on_min_quit = None
        self.result_on_max_quit = None

    def add_result(self, simulation_results):
        # if we're storing results, store it
        if self.store_results:
            self.results.append(simulation_results)
        
        # count the number of results we have added
        self.results_added += 1

        # increment the appropriate case
        if simulation_results.result == ResultsEnum.WIN_A:
            self.num_wins_case_a += 1
        elif simulation_results.result == ResultsEnum.WIN_B:
            self.num_wins_case_b += 1
        elif simulation_results.result == ResultsEnum.DRAW_A:
            self.num_draws_case_a += 1
        elif simulation_results.result == ResultsEnum.DRAW_B:
            self.num_draws_case_b += 1
        elif simulation_results.result == ResultsEnum.LOSS_A:
            self.num_losses_case_a += 1
        elif simulation_results.result == ResultsEnum.LOSS_B:
            self.num_losses_case_b += 1
      
        # calculate averages, minimums, and maximums
        self.calculate_averages(simulation_results)
        self.calculate_minimums(simulation_results)
        self.calculate_maximums(simulation_results)

    def get_string(self) -> str:
        if self.results_added != self.sample_size:
            return "ERROR: number of results {self.results_added} does not match sample size {self.sample_size}. If you see this error, contact the dev."
        
        self.calculate_secondaries()

        results_str = f"""
        Summary:
        \twins   = {self.num_wins}, {self.percent_wins:.4f}%
        \tdraws  = {self.num_draws}, {self.percent_draws:.4f}%
        \tlosses = {self.num_losses}, {self.percent_losses:.4f}%
       
        Wins Breakdown:
        \tCase A: {self.num_wins_case_a}
        \tDescription: {ResultsEnum.get_result_str(ResultsEnum.WIN_A)}
        \tCase B: {self.num_wins_case_b}
        \tDescription: {ResultsEnum.get_result_str(ResultsEnum.WIN_B)}

        Draws Breakdown:
        \tCase A: {self.num_draws_case_a}
        \tDescription: {ResultsEnum.get_result_str(ResultsEnum.DRAW_A)}
        \tCase B: {self.num_draws_case_b}
        \tDescription: {ResultsEnum.get_result_str(ResultsEnum.DRAW_B)}
        
        Losses Breakdown:
        \tCase A: {self.num_losses_case_a}
        \tDescription: {ResultsEnum.get_result_str(ResultsEnum.LOSS_A)}
        \tCase B: {self.num_losses_case_b}
        \tDescription: {ResultsEnum.get_result_str(ResultsEnum.LOSS_B)}

        Averages:
        \tAvg Defectors = {self.avg_defectors:.4f}
        \tAvg Skipped   = {self.avg_skipped:.4f}
        \tAvg Invalid   = {self.avg_invalid:.4f}
        \tAvg Quit      = {self.avg_quit:.4f}
        
        Minimums:
        \tMin Defectors = {self.min_defectors}
        \tInfo: {ResultsEnum.get_result_str(self.result_on_min_defectors)}
        
        \tMin Skipped   = {self.min_skipped}
        \tInfo: {ResultsEnum.get_result_str(self.result_on_min_skipped)}
        
        \tMin Invalid   = {self.min_invalid}
        \tInfo: {ResultsEnum.get_result_str(self.result_on_min_invalid)}
        
        \tMin Quit      = {self.min_quit}
        \tInfo: {ResultsEnum.get_result_str(self.result_on_min_quit)}
        
        Maximums:
        \tMax Defectors = {self.max_defectors}
        \tInfo: {ResultsEnum.get_result_str(self.result_on_max_defectors)}
        
        \tMax Skipped   = {self.max_skipped}
        \tInfo: {ResultsEnum.get_result_str(self.result_on_max_skipped)}
        
        \tMax Invalid   = {self.max_invalid}
        \tInfo: {ResultsEnum.get_result_str(self.result_on_max_invalid)}
        
        \tMax Quit      = {self.max_quit}
        \tInfo: {ResultsEnum.get_result_str(self.result_on_max_quit)}
        """
        
        return results_str

    # recalculate averages
    def calculate_averages(self, simulation_results):
        self.avg_defectors += (simulation_results.defectors / self.sample_size)
        self.avg_skipped += (simulation_results.skipped / self.sample_size)
        self.avg_invalid += (simulation_results.invalid / self.sample_size)
        self.avg_quit += (simulation_results.quit / self.sample_size)
        
    def calculate_minimums(self, simulation_results):
        self.min_defectors = min(simulation_results.defectors, self.min_defectors)
        self.min_skipped = min(simulation_results.skipped, self.min_skipped)
        self.min_invalid = min(simulation_results.invalid, self.min_invalid)
        self.min_quit = min(simulation_results.quit, self.min_quit)

        if self.min_defectors == simulation_results.defectors:
            self.result_on_min_defectors = simulation_results.result
        if self.min_skipped == simulation_results.skipped:
            self.result_on_min_skipped = simulation_results.result
        if self.min_invalid == simulation_results.invalid:
            self.result_on_min_invalid = simulation_results.result
        if self.min_quit == simulation_results.quit:
            self.result_on_min_quit = simulation_results.result


    def calculate_maximums(self, simulation_results):
        self.max_defectors = max(simulation_results.defectors, self.max_defectors)
        self.max_skipped = max(simulation_results.skipped, self.max_skipped)
        self.max_invalid = max(simulation_results.invalid, self.max_invalid)
        self.max_quit = max(simulation_results.quit, self.max_quit)

        if self.max_defectors == simulation_results.defectors:
            self.result_on_max_defectors = simulation_results.result
        if self.max_skipped == simulation_results.skipped:
            self.result_on_max_skipped = simulation_results.result
        if self.max_invalid == simulation_results.invalid:
            self.result_on_max_invalid = simulation_results.result
        if self.max_quit == simulation_results.quit:
            self.result_on_max_quit = simulation_results.result


    def calculate_secondaries(self):
        self.num_wins = self.num_wins_case_a + self.num_wins_case_b
        self.num_draws = self.num_draws_case_a + self.num_draws_case_b
        self.num_losses = self.num_losses_case_a + self.num_losses_case_b
        
        self.percent_wins = (self.num_wins / self.sample_size) * 100
        self.percent_draws = (self.num_draws / self.sample_size) * 100
        self.percent_losses = (self.num_losses / self.sample_size) * 100
