Title: 4 Execute measurement
Date: 2022-12-12
Category: Software installation

Important: The local host and the RPi have to be in the same local network
(e.g. connect both local host and RPi via LAN-Cable to a local network.) The ip-address
of the RPi is then static.

### How to run the script in order to execute a measurement:  
`./measure_plot.sh`
type in password     
Measurement starts after password is entered
`Ctrl-C` to stop the measurement
type in password again (in order to copy .csv-file via rsync to host)
plot_sensor_data.pdf is created on local machine


There is a time lag of the print statements reporting the values of every single
measurement. To get the values of the measurements reported immediately:  
`ssh pi@130.149.244.206`      
execute write_from_tsl2591.py on RPi    
To create the plot in a second step    
delete `ssh pi@$ip_address 'bash -s' < script_on_pi.sh` in measure_plot.sh      
execute measure_plot.sh as described above.
