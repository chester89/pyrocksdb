from setuptools import setup
from setuptools import find_packages
from distutils.extension import Extension
import platform

try:
    from Cython.Build import cythonize
except ImportError:
    def cythonize(extensions): return extensions
    sources = ['rocksdb/_rocksdb.cpp']
else:
    sources = ['rocksdb/_rocksdb.pyx']

default_flags={ '-std=c++11', '-O3', '-Wall', '-Wextra', '-Wconversion', '-fno-strict-aliasing' }

platform_to_compiler_flags = {
    'linux':default_flags,
    'windows':{ '/O2', '/Wall' }
}

mod1 = Extension(
    'rocksdb._rocksdb',
    sources,
    extra_compile_args=list(platform_to_compiler_flags.get(platform.system(), default_flags)),
    language='c++',
    libraries=[
        'rocksdb',
        'snappy',
        'bz2',
        'z'
    ]
)

setup(
    name="pyrocksdb",
    version='0.5',
    description="Python bindings for RocksDB",
    keywords='rocksdb',
    author='Stephan Hofmockel',
    author_email="Use the github issues",
    url="https://github.com/stephan-hof/pyrocksdb",
    license='BSD License',
    install_requires=['setuptools'],
    package_dir={'rocksdb': 'rocksdb'},
    packages=find_packages('.'),
    ext_modules=cythonize([mod1]),
    test_suite='rocksdb.tests',
    include_package_data=True
)
