import random
import time

from algometer import Algometer, AlgometerReading, Unit


class DevelopmentAlgometer(Algometer):
    def __init__(self):
        super().__init__(None)
        self.current_force = 0
        self.start_reading_time = 0

    def get_reading_raw(self) -> AlgometerReading:
        if self.start_reading_time == 0:
            self.start_reading_time = time.time()
            return AlgometerReading(0, Unit.LBF)

        elapsed_time = time.time() - self.start_reading_time

        self.current_force = elapsed_time * 0.449

        if self.current_force > 11.18:
            self.current_force = 0
            self.start_reading_time = 0
        reading = self.current_force + random.gauss(0, 0.05)
        return AlgometerReading(reading, Unit.LBF)
