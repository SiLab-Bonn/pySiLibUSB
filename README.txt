
Installing pySiLibUSB
=====================================

1. Dependencies:
- libusb library: http://www.libusb.org/
  Linux:   apt-get install libusb-1.0-0
  Windows: WinUSB driver (use http://zadig.akeo.ie installer)
  OSX:     libusb from homebrew (http://brew.sh)
  
- PyUSB: https://github.com/walac/pyusb
  Windows: pip install https://github.com/walac/pyusb/archive/master.zip
  Linux/OSX: pip install git+https://github.com/walac/pyusb.git@master#egg=pyusb

2. pySiLibUSB:
  For users (preferred):
  python setup.py install
  
  For developers:
  python setup.py install
