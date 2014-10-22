import MonteCarlo
from MonteCarlo import MonteCarlo
from nose.tools import assert_equal,assert_raises
import numpy as np

def test_number_of_particles_is_preserved():
	mc = MonteCarlo(1,0,[1])
	random_density = np.random.random_integers(0,1000,1000)
	totalNumberOfParticles = random_density.sum()
	shifted_density = mc.moveRandomParticle(random_density)
	assert_equal(shifted_density.sum(),totalNumberOfParticles)

def test_shift_is_only_by_one_block():
	mc = MonteCarlo(1,0,[1])
	shifted_density = mc.moveRandomParticle([0,0,1,0,0])
	assert(shifted_density==[0,1,0,0,0] or shifted_density == [0,0,0,1,0])

def test_zero_length_density_is_maintained():
	mc = MonteCarlo(1,0,[1])
	zero_density = np.zeros(np.random.randint(1,100))
	shifted_density = mc.moveRandomParticle(zero_density)
	assert_equal(shifted_density.all(),zero_density.all())

def test_invalid_densities_are_rejected():
	mc = MonteCarlo(1,0,[1])
	invalid_density = np.zeros(np.random.randint(1,100))
	invalid_density[np.random.randint(len(invalid_density))] = -1
	
	shifted_density = mc.moveRandomParticle(invalid_density)
	assert_raises(ValueError, mc.moveRandomParticle, invalid_density)
