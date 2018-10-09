from distutils.core import setup
from distutils.extension import Extension
from Cython.Distutils import build_ext
from Cython.Build import cythonize
import numpy

###### cythonfn.pyx ########
setup(
	cmdclass = {'build_ext': build_ext},
	ext_modules = [Extension("calculate", ["cythonfn.pyx"])]
)

######## cython_np.pyx ########
# setup(
# 	cmdclass = {'build_ext': build_ext},
# 	ext_modules = [
# 		Extension("calculate",
# 							 ["cython_np.pyx"],
#                              include_dirs = [numpy.get_include()]
# )])