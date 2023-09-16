from enum import Enum
from statistics.hypothesis_test import TestTypeEnum

class OutcomeEnum(Enum):
    WIN = 0
    LOSS = 1
    DRAW = 2

class Other_Variables:
    def __init__(self):
        # simulation runs
        self.sample_size = 1            # number of times to run the simulation

        # statistics
        self.trial_sample_size = 100    # number of times to run the simulation for each trial
        self.trial_count = 30           # number of trials to run the simulation for

        self.alpha = 0.05               # alpha value to be used for confidence intervals & hypothesis testing
        
        self.test_type = TestTypeEnum.TWOTAILED
        self.test_outcome = OutcomeEnum.WIN
        self.value_to_test = 0.500

        # other
        self.settings_path = "config/settings.ini"
