def calculate_z(unsigned int maxiter, zs, cs):
	"""ジュリア漸化式を用いてoutputリストを計算する"""
	cdef unsigned int i, n
	cdef double complex z, c
	output = [0]*len(zs)
	for i in range(len(zs)):
		n = 0
		z = zs[i]
		c = cs[i]
		while n < maxiter and (z.real * z.real + z.imag * z.imag) < 4:
			z = z * z + c
			n += 1
		output[i] += n
	return output