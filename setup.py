from distutils.core import setup
from distutils.extension import Extension
from Cython.Distutils import build_ext
import numpy

gco_directory = "../../tools/gco/"

files = ['GCoptimization.cpp', 'graph.cpp', 'LinkedBlockList.cpp',
    'maxflow.cpp']

files = [gco_directory + f for f in files]
files.insert(0, "gco_python.pyx")

setup(cmdclass={'build_ext': build_ext},
    ext_modules=[Extension("pygco", files, language="c++",
    include_dirs=[gco_directory, numpy.get_include()], 
    library_dirs=[gco_directory])])
