import RPi.GPIO as GPIO
import spidev
import time
GPIO.setmode(GPIO.BCM)
spi = spidev.SpiDev()
spi.open(0,0)
def ReadChannel(channel):
 adc = spi.xfer2([1,(8+channel)<<4,0])
 data = ((adc[1]&3) << 8) + adc[2]
 return data
def ConvertVolts(data,places):
 volts = (data * 3.3) / float(1023)
 volts = round(volts,places)
 return volts
try:
 while True:
 temp_level = ReadChannel(0)
 temp = ConvertVolts(temp_level,2)
 print temp
 time.sleep(1)
except:
 KeyboardInterrupt()
 GPIO.cleanup()
import subprocess
from subprocess import call
import time
call(["espeak","Hello everyone"])
time.sleep(5)