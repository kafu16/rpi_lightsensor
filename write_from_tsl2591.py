# SPDX-FileCopyrightText: 2021 ladyada for Adafruit Industries
# SPDX-License-Identifier: MIT

# Simple demo of the TSL2591 sensor.  Will print the detected light value
# every second.
import time
import board
import adafruit_tsl2591
import csv

freq = 15.0 # frequency of measurements
t_sleep = 1.0 / freq # sleeptime

# Create sensor object, communicating over the board's default I2C bus
i2c = board.I2C()  # uses board.SCL and board.SDA

# Initialize the sensor.
sensor = adafruit_tsl2591.TSL2591(i2c)

# You can optionally change the gain and integration time:
# (The longer the integration time the more light the sensor is able to integrate,
# making it more sensitive in low light the longer the integration time.)
# sensor.gain = adafruit_tsl2591.GAIN_LOW (1x gain)
# sensor.gain = adafruit_tsl2591.GAIN_MED (25x gain, the default)
# sensor.gain = adafruit_tsl2591.GAIN_HIGH (428x gain)
# sensor.gain = adafruit_tsl2591.GAIN_MAX (9876x gain)
# sensor.integration_time = adafruit_tsl2591.INTEGRATIONTIME_100MS (100ms, default)
# sensor.integration_time = adafruit_tsl2591.INTEGRATIONTIME_200MS (200ms)
# sensor.integration_time = adafruit_tsl2591.INTEGRATIONTIME_300MS (300ms)
# sensor.integration_time = adafruit_tsl2591.INTEGRATIONTIME_400MS (400ms)
# sensor.integration_time = adafruit_tsl2591.INTEGRATIONTIME_500MS (500ms)
# sensor.integration_time = adafruit_tsl2591.INTEGRATIONTIME_600MS (600ms)

header = ['time', 'total_light', 'IR', 'visible_light', 'full_spectrum']


with open('sensor_data.csv', 'w', encoding='UTF8') as f:
    writer = csv.writer(f)
    # write the header
    writer.writerow(header)

    time_of_measurement = 0
    # Read the total lux, IR, and visible light levels and print it every second.
    while True:
        # Read and calculate the light level in lux.
        lux = sensor.lux
        print("Total light: {0}lux".format(lux))
        # You can also read the raw infrared and visible light levels.
        # These are unsigned, the higher the number the more light of that type.
        # There are no units like lux.
        # Infrared levels range from 0-65535 (16-bit)
        infrared = sensor.infrared
        print("Infrared light: {0}".format(infrared))
        # Visible-only levels range from 0-2147483647 (32-bit)
        visible = sensor.visible
        print("Visible light: {0}".format(visible))
        # Full spectrum (visible + IR) also range from 0-2147483647 (32-bit)
        full_spectrum = sensor.full_spectrum
        print("Full spectrum (IR + visible) light: {0}".format(full_spectrum))
        time.sleep(t_sleep)

        data = [time_of_measurement, lux, infrared, visible, full_spectrum]
        time_of_measurement += t_sleep

        # write the data
        writer.writerow(data)
