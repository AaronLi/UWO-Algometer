import random
import time
from typing import Iterable, Any

from algometer.algometer import Algometer, AlgometerReading, Unit, MeasurementLocation


class DevelopmentAlgometer(Algometer):
    def __init__(self):
        super().__init__()
        self.current_force = 0
        self.start_reading_time = 0

    def get_reading_raw(self, location: MeasurementLocation) -> AlgometerReading:
        if self.start_reading_time == 0:
            self.start_reading_time = time.time()
            return AlgometerReading(0, Unit.LBF, location)

        elapsed_time = time.time() - self.start_reading_time

        self.current_force = elapsed_time * 0.449

        if self.current_force > 11.18:
            self.current_force = 0
            self.start_reading_time = 0
        reading = self.current_force + random.gauss(0, 0.05)
        return AlgometerReading(reading, Unit.LBF, location)

    @classmethod
    def get_display_name(cls) -> str:
        return "***DEVELOPMENT ALGOMETER***"

    @classmethod
    def get_device_requirements(cls) -> Iterable[Any]:
        return []


