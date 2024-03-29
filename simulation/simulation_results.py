from enum import Enum

class ResultsEnum(Enum):
    """
    Has 6 states: WIN_A, WIN_B, DRAW_A, DRAW_B, LOSS_A, LOSS_B,
    each of which indicates the results of a simulation, but also the reason
    that triggered the win/loss/draw (reason A or reason B?)
    """
    WIN_A = 0
    WIN_B = 1
    DRAW_A = 2
    DRAW_B = 3
    LOSS_A = 4
    LOSS_B = 5

    @staticmethod
    def get_result_str(result):
        if result == ResultsEnum.WIN_A:
            return "WIN: valid_remaining below 50% of total_member_cnt"
        elif result == ResultsEnum.WIN_B:
            return "WIN: final period completed with valid_remaining below 55% of total_member_cnt"
        elif result == ResultsEnum.DRAW_A:
            return "DRAW: 3 periods in a row where nobody quits or leaves, and valid_remaining below 60% of total_member_cnt"
        elif result == ResultsEnum.DRAW_B:
            return "DRAW: final period completed with valid_remaining below 65% of total_member_cnt"
        elif result == ResultsEnum.LOSS_A:
            return "LOSS: 3 periods in a row where nobody quits or leaves, and valid_remaining above 60% of total_member_cnt"
        elif result == ResultsEnum.LOSS_B:
            return "LOSS: final period reached with valid_remaining above 65% of total_member_cnt"

        return "INVALID RESULT: If this result pops up, contact the developer."

class Simulation_Results:
    """
    stores a results enum with some additional information
    """
    def __init__(self):
        self.result = None
        self.defectors = 0 
        self.skipped = 0 
        self.invalid = 0 
        self.quit = 0 
        self.total_member_count = -1
