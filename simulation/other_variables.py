from enum import Enum
from statistics.hypothesis_test import TestTypeEnum
from statistics.statistics_attributes import statistics_attributes

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
        
        self._test_type = TestTypeEnum.TWOTAILED
        self._test_outcome = "num_wins" 
        self.value_to_test = 0.500

        # other
        self.settings_path = "config/settings.ini"

    @property
    def test_type(self):
        return self._test_type

    @test_type.setter
    def test_type(self, value):
        if isinstance(value, TestTypeEnum):
            self._test_type = value
        else:
            self._test_type = TestTypeEnum[value]

    @property
    def test_outcome(self):
        return self._test_outcome

    @test_outcome.setter
    def test_outcome(self, value):
        if not isinstance(value, str):
            raise TypeError("Attempting to pass non-string value to test_outcome. (attributes must be strings)")
        if value not in statistics_attributes:
            raise ValueError("Attempting to pass invalid attribute string to test_outcome.")

        self._test_outcome = value
