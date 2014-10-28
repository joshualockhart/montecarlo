from MonteCarlo import MonteCarlo
import numpy as np

i = np.zeros(100)
i[50] = 50

mc = MonteCarlo(1,1000,i)
mc.runSimulation()