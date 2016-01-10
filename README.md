# pySiLibUSB

pySiLibUSB - SILAB USB device application programming interface

## Installation

A working libusb installation is required. Read the [Wiki](https://github.com/SiLab-Bonn/pySiLibUSB/wiki) on how to install libusb library.

The following packages are required for pySiLibUSB to function:
  ```
  pyusb
  ```

To install from PyPI:
  ```
  pip install pySiLibUSB
  ```
  
To install from repository:
  ```
  pip install https://github.com/walac/pyusb/archive/master.zip (Windows without git)
  pip install git+https://github.com/walac/pyusb.git@master#egg=pyusb (Linux, Mac, Windows with git)
  ```

__Linux:__
Adding a udev rule is mandatory to gain access to the USB device. The udev rule needs to be placed in `/etc/udev/rules.d/`.
Examples are available in the [/udev](https://github.com/SiLab-Bonn/pySiLibUSB/tree/master/udev) folder.
