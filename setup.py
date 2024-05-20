from setuptools import setup, Extension
from Cython.Build import cythonize
import numpy

VERSION="0.1.50"
f=open("src/ldpc_masked/VERSION","w+")
f.write(VERSION)
f.close()

extension = Extension(
    name="ldpc_masked.bp_decoder",
    sources=["src/ldpc_masked/include/mod2sparse.c","src/ldpc_masked/bp_decoder.pyx"],
    libraries=[],
    library_dirs=[],
    include_dirs=[numpy.get_include(),'src/ldpc_masked/include'],
    extra_compile_args=['-std=c11']
    )

extension2 = Extension(
    name="ldpc_masked.mod2sparse",
    sources=["src/ldpc_masked/include/mod2sparse.c","src/ldpc_masked/include/mod2sparse_extra.c","src/ldpc_masked/mod2sparse.pyx"],
    libraries=[],
    library_dirs=[],
    include_dirs=[numpy.get_include(),'src/ldpc_masked/include'],
    extra_compile_args=['-std=c11']
    )

extension3 = Extension(
    name="ldpc_masked.c_util",
    sources=["src/ldpc_masked/c_util.pyx","src/ldpc_masked/include/mod2sparse.c","src/ldpc_masked/include/binary_char.c","src/ldpc_masked/include/sort.c"],
    libraries=[],
    library_dirs=[],
    include_dirs=[numpy.get_include(),'src/ldpc_masked/include'],
    extra_compile_args=['-std=c11']
    )

extension4 = Extension(
    name="ldpc_masked.osd",
    sources=["src/ldpc_masked/osd.pyx","src/ldpc_masked/include/mod2sparse.c","src/ldpc_masked/include/mod2sparse_extra.c","src/ldpc_masked/include/binary_char.c","src/ldpc_masked/include/sort.c"],
    libraries=[],
    library_dirs=[],
    include_dirs=[numpy.get_include(),'src/ldpc_masked/include'],
    extra_compile_args=['-std=c11']
    )

setup(
    version=VERSION,
    ext_modules=cythonize([extension,extension2,extension3,extension4]),
)
