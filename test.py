from statistics.statistics_runner import Statistics_Runner
from simulation.other_variables import *
from simulation.pricing_variables import *
from simulation.environment_variables import *

def test():
    sr = Statistics_Runner(Environment_Variables(), Pricing_Variables(), Other_Variables())
    sr.run()

test()
