"""
Implementation of Algometer for use with the Wagner FPX
"""
import re
from types import NoneType
from typing import Iterable, Any

import serial

from algometer.algometer import Algometer, Unit, AlgometerReading


class BTDevAlgometer(Algometer):
    __reading_pattern = re.compile(r'(-?\d+\.\d+) (\w+)')

    def get_reading_raw(self) -> AlgometerReading:
        self.serial_device.write(b'?\r\n')
        response = self.serial_device.readline().decode('utf-8').strip()
        print(response)
        if not isinstance(response, NoneType):
            return AlgometerReading(float(response), Unit.LBF)
        #match = self.__reading_pattern.match(response)
        #if match:
        #    reading = -float(match[1])
        #    unit = Unit.from_string(match[2])

    def disconnect(self):
        super().disconnect()
        self.serial_device.close()

    @classmethod
    def get_display_name(cls) -> str:
        return 'Bluetooth Dev Algometer'

    @classmethod
    def get_device_requirements(cls) -> Iterable[Any]:
        return [serial.Serial]



