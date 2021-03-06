#!/usr/bin/env python

import sys
from datetime import datetime
import time
import array
import struct
import os

try:
    import serial
except:
    print "This tool needs PySerial, but it was not found"
    sys.exit(1)

sys.path.append("../shell")
import swapforth

class TetheredJ1a(swapforth.TetheredTarget):
    cellsize = 2

    def reset(self):
        ser = self.ser
        ser.setDTR(1)
        ser.setDTR(0)
        time.sleep(0.01)

        for c in ' 1 tth !':
            ser.write(c)
            ser.flush()
            time.sleep(0.001)
            ser.flushInput()
            # print repr(ser.read(ser.inWaiting()))
        ser.write('\r')

        while 1:
            c = ser.read(1)
            # print repr(c)
            if c == chr(30):
                break

    def boot(self, bootfile = None):
        sys.stdout.write('Contacting... ')
        self.reset()
        print 'established'

    def interrupt(self):
        self.reset()
        
if __name__ == '__main__':
    swapforth.main(TetheredJ1a)
