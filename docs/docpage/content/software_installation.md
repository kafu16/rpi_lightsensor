Title: 3 Software installation
Date: 2022-12-13
Category: Software installation

This is tested on Ubuntu 20.04 LTS   

### Information of the manufacturer:  
[repo](https://github.com/adafruit/Adafruit_CircuitPython_TSL2591)  
[docs](https://docs.circuitpython.org/projects/tsl2591/en/latest/)

### Install Adafruit library and driver bundle via   
`pip3 install adafruit-circuitpython-lis3dh`  
(see [https://github.com/adafruit/Adafruit_CircuitPython_Bundle](https://github.com/adafruit/Adafruit_CircuitPython_Bundle) for more information).

### Istall system-wide driver for TSL  
`sudo pip3 install adafruit-circuitpython-tsl2591`    
(see [https://docs.circuitpython.org/projects/tsl2591/en/latest/index.html](https://docs.circuitpython.org/projects/tsl2591/en/latest/index.html) for more information).

### Activate I2C-GPIO  
`sudo raspi-config` in terminal of the pi  
Go to "3 Interface Options"  
Select "P5 I2C"  

### Clone this [repository](https://github.com/kafu16/rpi_lightsensor.git) on local machine (for Linux-users preferably in home directory)  
`git clone https://github.com/kafu16/rpi_lightsensor.git`  
If not cloned in home directory: Adapt the path in rpi_lightsensor/measure_plot.sh line 5
that points to the directory where you cloned the repository (adapt the variable `local_repo`).  

Parts of the script are adapted from a [usage example](https://docs.circuitpython.org/projects/tsl2591/en/latest/examples.html) that can be downloaded [here](https://github.com/adafruit/Adafruit_CircuitPython_TSL2591/blob/main/examples/tsl2591_simpletest.py).

Give the script exection permission    
`cd rpi_lightsensor`    
`chmod +x measure_plot.sh`  

### On the RPi clone the same [repository](https://github.com/kafu16/rpi_lightsensor.git) in the home directory. You should get a directory `/home/pi/rpi_lightsensor`.

### Activate ssh on the rpi    
On rpi go to applications menu (top left)/Raspberry Pi Configuration/Interfaces  
Select "Enable"    
