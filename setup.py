#!/usr/bin/env python   

from distutils.core import setup

from SiLibUSB import __version__

setup(
    name='pySiLibUSB',
    version=__version__,
    py_modules=['SiLibUSB'],
    description='SILAB USB Device Application Programming Interface',
    url='http://icwiki.physik.uni-bonn.de/',
    long_description =''
)

