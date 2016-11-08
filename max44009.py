#!/usr/bin/env python

import smbus

class MAX44009():

    _REG_INTERRUPT_STATUS = 0x00
    _REG_INTERRUPT_ENABLE = 0x01
    _REG_CONFIGURATION    = 0x02
    _REG_LUX_HIGH_BYTE    = 0x03
    _REG_LUX_LOW_BYTE     = 0x04
    _REG_UPPER_THRESHOLD  = 0x05
    _REG_LOWER_THRESHOLD  = 0x06
    _REG_TIMER_THRESHOLD  = 0x07

    ###########################
    # MAX44009 Code
    ###########################
    def __init__(self, bus=1, addr=0x4a):
        self._bus = smbus.SMBus(bus)
        self._addr = addr


    def _write(self, register, data):
        self._bus.write_byte_data(self._addr, register, data)


    def _read(self, register):
        return self._bus.read_byte_data(self._addr, register)

    def _read_block(self, register, size=2):
        return self._bus.read_i2c_block_data(self._addr, register, size)


    def configure(self, cont=0, manual=0, cdr=0, timer=0):
        configuration = (cont & 0x01) << 7 | (manual & 0x01) << 6 | (cdr & 0x01) << 3 | timer & 0x07
        self._write(self._REG_CONFIGURATION, configuration)


    def luminosity(self):
        data = self._read_block(self._REG_LUX_HIGH_BYTE, 2)
        exponent = (data[0] & 0xF0) >> 4
        mantissa = ((data[0] & 0x0F) << 4) | (data[1] & 0x0F)
        luminance = ((2 ** exponent) * mantissa) * 0.045
        return luminance
