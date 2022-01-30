"""
Base Class for any algometer implementation.
"""
import abc
import enum
from dataclasses import dataclass
from functools import total_ordering
from typing import Optional, Iterable, Any

import serial


class Unit(enum.Enum):
    LBF = enum.auto()
    N = enum.auto()
    KGF = enum.auto()
    OZF = enum.auto()

    @classmethod
    def from_string(cls, string):
        string = string.lower()
        if string == 'lbf':
            return cls.LBF
        elif string == 'n':
            return cls.N
        elif string == 'kgf':
            return cls.KGF
        elif string == 'ozf':
            return cls.OZF
        else:
            raise ValueError('Unknown unit: {}'.format(string))

    def to_string(self):
        if self == Unit.LBF:
            return 'lbf'
        elif self == Unit.N:
            return 'N'
        elif self == Unit.KGF:
            return 'kgf'
        elif self == Unit.OZF:
            return 'ozf'
        else:
            raise ValueError('Unknown unit: {}'.format(self))

    def __str__(self) -> str:
        return self.to_string()

    def __to_newtons(self, value: float) -> float:
        if self == Unit.LBF:
            return value * 4.4482216152605
        elif self == Unit.N:
            return value
        elif self == Unit.KGF:
            return value * 9.80665
        elif self == Unit.OZF:
            return value * 0.2780139

    def __from_newtons(self, value: float) -> float:
        if self == Unit.LBF:
            return value / 4.4482216152605
        elif self == Unit.N:
            return value
        elif self == Unit.KGF:
            return value / 9.80665
        elif self == Unit.OZF:
            return value / 0.2780139

    def convert_to(self, value: float, to_unit: 'Unit') -> float:
        return to_unit.__from_newtons(self.__to_newtons(value))


@total_ordering
@dataclass(frozen=True)
class AlgometerReading:
    value: float
    unit: Unit

    def convert_to(self, to_unit: Unit) -> 'AlgometerReading':
        return AlgometerReading(self.unit.convert_to(self.value, to_unit), to_unit)

    @staticmethod
    def _valid_operand(other):
        return isinstance(other, AlgometerReading)

    def __neg__(self):
        return AlgometerReading(-self.value, self.unit)

    def __lt__(self, other: 'AlgometerReading'):
        if not self._valid_operand(other):
            return NotImplemented
        return self.value < other.convert_to(self.unit).value

    def __eq__(self, other: 'AlgometerReading'):
        if not self._valid_operand(other):
            return NotImplemented
        return self.value == other.convert_to(self.unit).value

    def __str__(self) -> str:
        return f'{self.value:.2f} {self.unit.to_string()}'


class Algometer(abc.ABC):
    """
    Algometer, does not close serial port itself
    """

    def get_reading(self, target_units: Unit) -> AlgometerReading:
        """
        Returns a reading in the target units
        :param target_units:
        :return:
        """
        reading = self.get_reading_raw()
        return reading.convert_to(target_units)

    @abc.abstractmethod
    def get_reading_raw(self) -> AlgometerReading:
        """
        Returns a reading in the default units from the device. For control over what units are returned, use get_reading(Unit)
        :return: The reading and its units
        """
        pass

    def disconnect(self):
        pass

    @classmethod
    @abc.abstractmethod
    def get_display_name(cls) -> str:
        """
        Returns a human readable name for the device
        :return:
        """
        pass

    @classmethod
    @abc.abstractmethod
    def get_device_requirements(cls) -> Iterable[Any]:
        """
        Returns a list of requirements for the device to be usable
        :return:
        """
        pass
