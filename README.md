# pySiLibUSB

pySiLibUSB - SILAB USB device application programming interface

## Installation

A working libusb installation is required. Read the [Wiki](https://github.com/SiLab-Bonn/pySiLibUSB/wiki) on how to install libusb library.

The following packages are required for pySiLibUSB to function:
  ```
  pyusb
  ```

To install [pyUSB](https://github.com/walac/pyusb), run the following command:
  ```
  pip install https://github.com/walac/pyusb/archive/1.0.0rc1.zip (Windows, without git)
  pip install git+https://github.com/walac/pyusb.git@1.0.0rc1 (Linux, Mac and Windows, with git)
  ```

Run the following command to install the latest version of pySiLibUSB:
  ```
  pip install pySiLibUSB
  ```

__Linux:__
Adding a udev rule is mandatory to gain access to the USB device. The udev rule needs to be placed in `/etc/udev/rules.d/`.
Examples are available in the [/udev](https://github.com/SiLab-Bonn/pySiLibUSB/tree/master/udev) folder.
