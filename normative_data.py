import json
import dataclasses
import enum
from typing import List, Optional

from algometer.algometer import AlgometerReading, Unit

class MeasurementLocation(enum.Enum):
    OTHER = enum.auto()
    UPPER_FIBERS_OF_TRAPEZIUS = enum.auto()
    TIBIALIS_ANTERIOR = enum.auto()

    @classmethod
    def from_string(cls, string):
        string = string.lower()

        if string == "uft":
            return cls.UPPER_FIBERS_OF_TRAPEZIUS
        elif string == "ta":
            return cls.TIBIALIS_ANTERIOR
        else:
            return cls.OTHER

class Sex(enum.Enum):
    OTHER = enum.auto()
    MALE = enum.auto()
    FEMALE = enum.auto()

    @classmethod
    def from_string(cls, string):
        string = string.lower()

        if string == 'male':
            return cls.MALE
        elif string == 'female':
            return cls.FEMALE
        else:
            return cls.OTHER

@dataclasses.dataclass
class NormativeData:
    sex: Sex
    location: MeasurementLocation
    quartiles: List[AlgometerReading]
    standard_error_of_measurement: AlgometerReading

    def get_quartile(self, measurement: AlgometerReading) -> Optional[int]:
        quartile = len(self.quartiles)-1
        while self.quartiles[quartile] > measurement:
            quartile -= 1
            if quartile < 0:
                return None
        return quartile + 1

class NormativeDataTable:
    def __init__(self, data_file):
        self.data_file = data_file
        self.data = self.load_data()

    def load_data(self):
        out_data = {}
        with open(self.data_file, 'r') as f:
            table = json.load(f)

            for sex in table:
                data_sex = Sex.from_string(sex)
                for region in table[sex]:
                    data_region = MeasurementLocation.from_string(region)

                    if data_sex not in out_data:
                        out_data[data_sex] = {}

                    data_table = table[sex][region]
                    units = Unit.from_string(data_table['Unit'])
                    first_quartile = AlgometerReading(float(data_table['Q1']), units)
                    second_quartile = AlgometerReading(float(data_table['Q2']), units)
                    third_quartile = AlgometerReading(float(data_table['Q3']), units)
                    standard_error_of_measurement = AlgometerReading(float(data_table['SEM']), units)
                    out_data[data_sex][data_region] = NormativeData(data_sex, data_region, [AlgometerReading(0, Unit.N), first_quartile, second_quartile, third_quartile], standard_error_of_measurement)
        return out_data
    def get_normative_data(self, location: MeasurementLocation, sex: Sex) -> NormativeData:
        return self.data[sex][location]

if __name__ == '__main__':
    table = NormativeDataTable('normative_data_1.json')
    data = table.get_normative_data(MeasurementLocation.TIBIALIS_ANTERIOR, Sex.FEMALE)
    print(data)

    test_reading = AlgometerReading(-1, Unit.N)
    print(data.get_quartile(test_reading))

    test_reading = AlgometerReading(5, Unit.N)

    print(data.get_quartile(test_reading))
    test_reading = AlgometerReading(25, Unit.N)

    print(data.get_quartile(test_reading))

    test_reading = AlgometerReading(45, Unit.N)

    print(data.get_quartile(test_reading))

    test_reading = AlgometerReading(55, Unit.N)

    print(data.get_quartile(test_reading))

    test_reading = AlgometerReading(505, Unit.N)

    print(data.get_quartile(test_reading))
