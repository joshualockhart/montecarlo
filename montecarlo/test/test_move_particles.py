import MonteCarlo
from MonteCarlo import MonteCarlo
from nose.tools import assert_equal,assert_raises
import numpy as np

def test_number_of_particles_is_preserved():
	random_density = np.random.random_integers(0,1000,1000)
	mc = MonteCarlo(1,0,random_density)
	totalNumberOfParticles = random_density.sum()
	shifted_density = mc.moveRandomParticle(random_density)
	assert_equal(shifted_density.sum(),totalNumberOfParticles)

def test_shift_is_only_by_one_block():
	mc = MonteCarlo(1,0,np.array([1]))
	shifted_density = mc.moveRandomParticle(np.array([0,0,1,0,0]))
	print shifted_density
	assert(shifted_density.all()==np.array([0,1,0,0,0]).all() or shifted_density.all() == np.array([0,0,0,1,0]).all())

def test_zero_length_density_is_rejected():
	mc = MonteCarlo(1,0,np.array([1]))
	zero_density = np.zeros(np.random.randint(1,100))
	assert_raises(ValueError, mc.moveRandomParticle, zero_density)

def test_negative_densities_are_rejected():
	mc = MonteCarlo(1,0,np.array([1]))
	invalid_density = np.zeros(np.random.randint(1,100))
	invalid_density[np.random.randint(len(invalid_density))] = -1
	assert_raises(ValueError, mc.moveRandomParticle, invalid_density)
