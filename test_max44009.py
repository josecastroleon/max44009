#!/usr/bin/env python

import sys
import time

sys.path.append('./')

import max44009

# Main Program

print ""
print "Test Max44009"
print ""

max_sensor = max44009.MAX44009(1, 0x4a)

max_sensor.configure(cont=0, manual=0, cdr=0, timer=0)

# Main Loop - sleeps 2 seconds, then reads and print luminosity values

while True:
    print "Ambient Light luminance : %.2f lux" % max_sensor.luminosity()
    time.sleep(2.0)
