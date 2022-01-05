import enum
import abc
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

class Algometer(abc.ABC):
    """
    Algometer, does not close serial port itself
    """
    def __init__(self, serial_device: serial.Serial):
        self.serial_device = serial_device


    def get_reading(self, target_units: Unit) -> (float, Unit):
        """
        Returns a reading in the target units
        :param target_units:
        :return:
        """
        value, measurement_units = self.get_reading_raw()
        return measurement_units.convert_to(value, target_units), target_units

    @abc.abstractmethod
    def get_reading_raw(self) -> (float, Unit):
        """
        Returns a reading in the default units from the device. For control over what units are returned, use get_reading(Unit)
        :return: The reading and its units
        """
        pass
