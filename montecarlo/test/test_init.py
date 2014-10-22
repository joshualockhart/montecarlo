import MonteCarlo
from MonteCarlo import MonteCarlo
from nose.tools import assert_equal,assert_raises
import numpy as np

def test_negative_temperature_rejected():
	assert_raises(ValueError, MonteCarlo, -1,0,np.array([1]))

def test_zero_temperature_rejected():
	assert_raises(ValueError, MonteCarlo, 0,0,np.array([1]))	

def test_negative_iterations_rejected():
	assert_raises(ValueError, MonteCarlo, -1,0,np.array([1]))

def test_no_particles_density_rejected():
	zero_density = np.zeros(np.random.randint(1,100))
	assert_raises(ValueError, MonteCarlo, 1,1,zero_density)

def test_invalid_initialDensity_rejected():
	invalid_density = np.zeros(np.random.randint(1,100))
	invalid_density[np.random.randint(len(invalid_density))] = -1
	assert_raises(ValueError, MonteCarlo, 1,1,invalid_density)