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
    description='pySiLibUSB - SILAB USB device application programming interface',
    url='https://github.com/SiLab-Bonn/pySiLibUSB',
    license='BSD 3-Clause ("BSD New" or "BSD Simplified") License',
    long_description='API for SILAB USB devices.',
    install_requires=['pyusb>=1.0.0rc1'],
    packages=find_packages(),
    include_package_data=True,  # accept all data files and directories matched by MANIFEST.in or found in source control
    package_data={'': ['*.txt', 'VERSION'], 'examples': ['*'], 'udev': ['*']},
    author=author,
    maintainer=author,
    author_email=author_email,
    maintainer_email=author_email,
    python_requires='>=2.7',
    platforms='any'
)
