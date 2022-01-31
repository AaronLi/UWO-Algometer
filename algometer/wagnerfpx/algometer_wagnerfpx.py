"""
Implementation of Algometer for use with the Wagner FPX
"""
import re
from typing import Iterable, Any

import serial

from algometer.algometer import Algometer, Unit, AlgometerReading


class AlgometerWagnerFPX(Algometer):
    __reading_pattern = re.compile(r'(-?\d+\.\d+) (\w+)')

    def __init__(self, serial_device: serial.Serial) -> None:
        super().__init__()
        self.serial_device = serial_device

    def get_reading_raw(self) -> AlgometerReading:
        self.serial_device.write(b'?\r\n')
        response = self.serial_device.readline().decode('utf-8').strip()
        match = self.__reading_pattern.match(response)
        if match:
            reading = -float(match[1])
            unit = Unit.from_string(match[2])
            return AlgometerReading(reading, unit)
        else:
            raise ValueError('Invalid response from device: {}'.format(response))

    def disconnect(self):
        super().disconnect()
        self.serial_device.close()

    @classmethod
    def get_display_name(cls) -> str:
        return 'Wagner FPX'

    @classmethod
    def get_device_requirements(cls) -> Iterable[Any]:
        return [serial.Serial]



