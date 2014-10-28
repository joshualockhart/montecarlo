from MonteCarlo import MonteCarlo
from nose.tools import assert_equal,assert_raises
from mock import Mock
import numpy as np
from Energy import energy

def calculateP0(energyDiff, temp):
		return np.exp(-energyDiff/temp)

def test_accept_check_negative_energy_gap():
	temp = np.random.uniform(100)
	mc = MonteCarlo(temp,1,np.array([1]))
	d0 = np.random.random_integers(0,100,100)
	d1 = np.random.random_integers(0,100,100)

	e0 = energy(d0)
	e1 = energy(d1)

	energyDiff = e1 - e0
	
	# we want an instance that will trigger the calculation of p0 and p1,
	# i.e. a positive energy gap

	while energyDiff >= 0:
		d0 = np.random.random_integers(0,100,100)
		d1 = np.random.random_integers(0,100,100)

		e0 = energy(d0)
		e1 = energy(d1)

		energyDiff = e1 - e0

	assert(mc.checkIfAcceptMove(d0,d1))

def test_accept_check_positive_energy_gap():
	temp = np.random.uniform(100)
	mc = MonteCarlo(temp,1,np.array([1]))
	d0 = np.random.random_integers(0,100,100)
	d1 = np.random.random_integers(0,100,100)

	e0 = energy(d0)
	e1 = energy(d1)

	energyDiff = e1 - e0
	
	# we want an instance that will trigger the calculation of p0 and p1,
	# i.e. a positive energy gap

	while energyDiff < 0:
		d0 = np.random.random_integers(0,100,100)
		d1 = np.random.random_integers(0,100,100)

		e0 = energy(d0)
		e1 = energy(d1)

		energyDiff = e1 - e0

	p0 = calculateP0(energyDiff,temp)
	noP1 = p0+((1-p0)*0.1)
	yesP1 = p0-((1-p0)*0.1)

	mc.generateP1 = Mock(name="generateP1", return_value=yesP1)

	assert(mc.checkIfAcceptMove(d0,d1))

	mc.generateP1 = Mock(name="generateP1", return_value=noP1)

	assert(not mc.checkIfAcceptMove(d0,d1))	
