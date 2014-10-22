import numpy as np
import copy

class MonteCarlo(object):
	
	def __init__(self, temperature, iterations, initialDensity):
		try:
			if temperature <= 0: 
				raise(ValueError("Negative/zero temperature? You are an idiot."))
		except TypeError:
			raise(TypeError("Temperature you have given me does not support mathematical operations"))

		try:
			if iterations < 0:
				raise(ValueError("Run the simulation for a negative number of iterations? You are an idiot."))
		except TypeError:
			raise(TypeError("Temperature you have given me does not support mathematical operations"))

		try:
			if len(initialDensity)==0:
				raise(ValueError("The initial density you have given me has no particles, this will not work"))
		except TypeError:
			raise(TypeError("The initial density you have given me is not an array type, this will not work"))

		for val in initialDensity:
			try:
				if val < 0:
					raise(ValueError("The initial density you have given me has a negative particle number in it, this will not work"))
				elif np.abs(val) != val:
					raise(ValueError("The initial density you have given me has a non-whole number of particles in it, this will not work"))
			except TypeError:
				raise(TypeError("You have given me an initial density with elements that do not support mathematical operations, this will not work"))

		try:
			if (initialDensity == 0).all():
				raise(ValueError("Density has no particles"))
		except AttributeError:
			raise(TypeError("Density object is not a numpy array: doesn't support all()"))

		self.temp = temperature
		self.iterations = iterations
		self.history = [initialDensity]

	def energy(self, density, coeff=1.0):
		total = 0.0
		for i in density:
			total += i*(i-1)
		return total*(coeff/2.0)

	def moveRandomParticle(self, density):
		if (density == 0).all():
			raise(ValueError("Density has no particles"))

		if not (density >= 0).all():
			raise(ValueError("Density has an entry with negative particle number"))

		density_c = copy.copy(density)
		randomPosition = np.random.randint(0,len(density))
		while density_c[randomPosition] == 0:
			randomPosition = np.random.randint(0,len(density))

		if np.random.randint(0,2) == 0:
			# move left
			if randomPosition > 0:
				density_c[randomPosition]-=1
				density_c[randomPosition-1]+=1
		else:
			# move right
			if randomPosition < len(density)-1:
				density_c[randomPosition]-=1
				density_c[randomPosition+1]+=1
		return density_c
		
	def performIteration(self):
		pass

	def runSimulation(self):
		for i in range(self.iterations):
			self.performIteration()


if __name__=="__main__":
	mc = MonteCarlo(10,10,np.array([0,0,0,0,0,0,1]))
	print mc.moveRandomParticle([0,0,0,1,0,0,0])
	#mc.runSimulation()