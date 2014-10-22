from MonteCarlo import MonteCarlo
from nose.tools import assert_equal
import numpy as np

def test_energy_calculation_is_correct():
	mc = MonteCarlo(1,0,np.array([1]))
	ret = mc.energy(np.array([1,2,3]),1.0)
	assert_equal(ret, 4.0)

	ret = mc.energy(np.array([2,2]),2.0)
	assert_equal(ret, 4.0)

	ret = mc.energy(np.array([7,2,3]),3.0)
	assert_equal(ret, 75.0)

def test_zero_length_densities_are_zero():
	mc = MonteCarlo(1,0,np.array([1]))
	ret = mc.energy(np.array([]),1.0)
	assert_equal(ret, 0.0)

def test_negative_values_are_rejected():
	mc = MonteCarlo(1,0,np.array([1]))
	ret = mc.energy(np.array([0.0,0.0,0.0,-1.0]),1.0)
	