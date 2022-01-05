import serial
import re
import algometer
from algometer import Algometer, Unit


class AlgometerWagnerFPX(Algometer):
    __reading_pattern = re.compile(r'(-?\d+\.\d+) (\w+)')

    def get_reading_raw(self) -> (float, Unit):
        self.serial_device.write(b'?\r\n')
        response = self.serial_device.readline().decode('utf-8').strip()
        match = self.__reading_pattern.match(response)
        reading, unit = float(match[1]), algometer.Unit.from_string(match[2])
        return reading, unit

