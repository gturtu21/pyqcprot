from distutils.core import setup
from distutils.extension import Extension

import numpy as np


try:
    #Return the directory that contains the NumPy *.h header files.
    #Extension modules that need to compile against NumPy should use this function to locate the appropriate include directory.
    numpy_include = np.get_include()
except AttributeError:
    numpy_include = np.get_numpy_include()

# Handle cython modules
try:
    from Cython.Distutils import build_ext
    use_cython = True
    cmdclass = {'build_ext': build_ext}
except ImportError:
    use_cython = False
    cmdclass = {}
finally:
    print('use_cython: {}'.format(use_cython))

ext_modules = [Extension("pyqcprot", ["pyqcprot.{}".format('pyx' if use_cython else 'c')],
                include_dirs=[numpy_include],
                extra_compile_args=["-O3","-ffast-math"])]

setup(
  name = 'Python qcprot module',
  cmdclass = cmdclass,
  ext_modules = ext_modules
)
