def energy(density, coeff=1.0):
	total = 0.0
	for i in density:
		total += i*(i-1)
	return total*(coeff/2.0)