import ui
from simulation.environment_variables import Environment_Variables
from simulation.pricing_variables import Pricing_Variables
from simulation.other_variables import *

def initialize_ui():
    uic = ui.UI_Context()
    uic.ev_obj = Environment_Variables()
    uic.pv_obj = Pricing_Variables()
    uic.ov_obj = Other_Variables()

    ui.initialize(uic)

initialize_ui()
