from enum import Enum

class ConditionEnum(Enum):
    EQUAL_TO = 0,
    NOT_EQUAL_TO = 1,
    GREATER_THAN = 2
    GREATER_THAN_OR_EQ = 3
    LESS_THAN = 4
    LESS_THAN_OR_EQ = 5

    @staticmethod
    def is_allowed(null, alt):
        A = (null is ConditionEnum.GREATER_THAN) and (alt is ConditionEnum.LESS_THAN)
        B = (null is ConditionEnum.LESS_THAN) and (alt is ConditionEnum.GREATER_THAN)
        C = (null is ConditionEnum.GREATER_THAN) and (alt is ConditionEnum.GREATER_THAN_OR_EQ)
        D = (null is ConditionEnum.GREATER_THAN_OR_EQ) and (alt is ConditionEnum.GREATER_THAN)
        E = (null is ConditionEnum.LESS_THAN) and (alt is ConditionEnum.LESS_THAN_OR_EQ)
        F = (null is ConditionEnum.LESS_THAN_OR_EQ) and (alt is ConditionEnum.LESS_THAN)

        return not (A or B or C or D or E or F)

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
        
        self.null_condition = ConditionEnum.EQUAL_TO        # null condition for hypothesis testing        
        self.alt_condition = ConditionEnum.NOT_EQUAL_TO     # alternative condition for hypothesis testing

        self.test_outcome = OutcomeEnum.WIN

        self.value_to_test = 50.0

        # other
        self.settings_path = "config/settings.ini"
