"""
Implementation of Algometer for use with the Wagner FPX
"""
import re

import algometer
from algometer import Algometer, Unit, AlgometerReading


class AlgometerWagnerFPX(Algometer):
    __reading_pattern = re.compile(r'(-?\d+\.\d+) (\w+)')

    def get_reading_raw(self) -> algometer.AlgometerReading:
        self.serial_device.write(b'?\r\n')
        response = self.serial_device.readline().decode('utf-8').strip()
        match = self.__reading_pattern.match(response)
        reading = -float(match[1])
        unit = Unit.from_string(match[2])
        return AlgometerReading(reading, unit)

