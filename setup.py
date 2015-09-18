#!/usr/bin/env python

# building source distribution:
# python setup.py sdist

from setuptools import setup, find_packages

from SiLibUSB.siusbdevice import __version__

author = 'Tomasz Hemperek, Jens Janssen'
author_email = 'hemperek@uni-bonn.de, janssen@physik.uni-bonn.de'

setup(
    name='pySiLibUSB',
    version=__version__,
    description='SILAB USB Device Application Programming Interface',
    url='https://silab-redmine.physik.uni-bonn.de/projects/pysilibusb',
    license='BSD 3-Clause ("BSD New" or "BSD Simplified") License',
    long_description='',
    install_requires=['pyusb>=1.0.0rc1'],
    packages=find_packages(),
    include_package_data=True,  # accept all data files and directories matched by MANIFEST.in or found in source control
    package_data={'': ['*.txt', 'VERSION'], 'examples': ['*'], 'udev': ['*']},
    author=author,
    maintainer=author,
    author_email=author_email,
    maintainer_email=author_email,
)
