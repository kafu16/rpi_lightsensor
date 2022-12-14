#!/bin/bash
# execute script via './<scriptname>.sh'

# directory of local host repo and slave repo (raspberry pi)
local_repo="$HOME/rpi_lightsensor"
slave_repo="/home/pi/rpi_lightsensor"

# ip-address of raspberry pi
ip_address=130.149.244.206

ssh pi@$ip_address 'bash -s' < script_on_pi.sh
# if this and the following commented lines are omitted `rsync` copies only an empty file

# rsync -r pi@$ip_address:/home/pi/Desktop/sensor_data.csv $local_repo
# rsync -r pi@$ip_address:/home/pi/Desktop/sensor_data.csv $local_repo
rsync -r pi@$ip_address:"$slave_repo/sensor_data.csv" $local_repo

python3 plot_sensor_data.py

exit
