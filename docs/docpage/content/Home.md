Title: 0 Home
Date: 2022-12-16
Category: Home

This documentation contains a step-by-step manual how to set up a Raspberry Pi (RPi) and connect it to the Adafruit TSL2591 High Dynamic Range Digital Light Sensor (TSL), install the necessary software on the RPi for that and set up the codebase on [https://github.com/kafu16/rpi_lightsensor](https://github.com/kafu16/rpi_lightsensor) for invoking a measurement from a local host  via ssh on the RPi and generate a plot of this
measurement on the local host.

Just follow the steps below:  
[1. Install OS on Raspberry Pi]({filename}/install_os_rpi.md)  
[2. Connect Adafruit TSL2591 High Dynamic Range Digital Light Sensor to a Raspberry Pi]({filename}/connect_sensor_to_rpi.md)  
[3. Software installation]({filename}/software_installation.md)    
[4. Execute measurement]({filename}/execute_measurement.md)  

Further information on the light sensor by the manufacturer can be found [here](https://learn.adafruit.com/adafruit-tsl2591?view=all).

### Example
In the following picture, the grayscale varies sinusoidally  
![image cannot be displayed](images/grayscales.png "grayscales")
Image taken from [here](https://www.cns.nyu.edu/~david/courses/perception/lecturenotes/channels/channels.html).

We projected similar picture using a beamer and measured the grayscales along the
horizontal axis getting
![image cannot be displayed](images/plot_sensor_data.svg "OS for Raspberry Pi")  
This figure can be downloaded [here]({static}pdfs/plot_sensor_data.pdf).
