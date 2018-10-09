# from cython.parallel import prange
import numpy as np
cimport numpy as np

def calculate_z(int maxiter, zs, cs):
	"""ジュリア漸化式を用いてoutputリストを計算する"""
	cdef int i, length
	cdef double complex z, c
	length = len(zs)
	output = [0]*length
	for i in range(length):
		n = 0
		z = zs[i]
		c = cs[i]
		output[i] = 0
		while output[i] < maxiter and (z.real * z.real + z.imag * z.imag) < 4:
			z = z * z + c
			n += 1
		output[i] += n
	return output