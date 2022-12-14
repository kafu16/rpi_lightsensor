#!/bin/bash
# execute script via './<scriptname>.sh'

# go to directory of repo
cd rpi_lightsensor
echo "UPDATING LOCAL REPO (if not up to date with its remote counterpart)."
echo ""
git pull

echo "STARTING MEASUREMENT"
# execute script that writes sensor data to .csv-file
python3 write_from_tsl2591.py


exit
