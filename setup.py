#!/usr/bin/env python   

from distutils.core import setup

from SiLibUSB import __version__

setup(
    name='pySiLibUSB',
    version=__version__,
    py_modules=['SiLibUSB'],
    description='SILAB USB Device Application Programming Interface',
    url='https://silab-redmine.physik.uni-bonn.de/projects/pysilibusb',
    license = 'BSD 3-Clause ("BSD New" or "BSD Simplified") License',
    long_description =''
)

