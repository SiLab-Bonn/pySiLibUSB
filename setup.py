#!/usr/bin/env python   

from setuptools import setup

from SiLibUSB import __version__

author = 'Tomasz Hemperek'
author_email = 'hemperek@uni-bonn.de'

setup(
    name='pySiLibUSB',
    version=__version__,
    py_modules=['SiLibUSB'],
    description='SILAB USB Device Application Programming Interface',
    url='https://silab-redmine.physik.uni-bonn.de/projects/pysilibusb',
    license = 'BSD 3-Clause ("BSD New" or "BSD Simplified") License',
    long_description ='',
    author=author,
    maintainer=author,
    author_email=author_email,
    maintainer_email=author_email,
    install_requires=['pyusb>=1.0.0b2'],
)

