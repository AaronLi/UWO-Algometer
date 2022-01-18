"""
Analyzes multiple algometer readings and prints the change over time when it has enough readings
also adds smoothing
"""
from typing import Tuple, Optional
from collections import deque
from algometer.algometer import Unit, AlgometerReading


class ReadingAnalyzer:
    def __init__(self, derivative_average_size: int = 10):
        self.start_reading_time: float = None
        self.max_reading = None
        self.previous_derivatives = deque(maxlen=derivative_average_size)
        self.previous_readings = deque(maxlen=2)

    def add_reading(self, reading: AlgometerReading, reading_time: float) -> Optional[Tuple[float, float]]:
        """
        Adds a reading to the analyzer. Returns the derivative of the readings if present.
        :param reading:
        :param reading_time:
        :return:
        """
        if self.start_reading_time is None:
            self.start_reading_time = reading_time
        if self.max_reading is None or reading > self.max_reading:
            self.max_reading = reading
        self.previous_readings.append((reading, reading_time - self.start_reading_time))
        if len(self.previous_readings) == 2:
            derivative = (self.previous_readings[1][0].value - self.previous_readings[0][0].value) / (self.previous_readings[1][1] - self.previous_readings[0][1])
            self.previous_derivatives.append((derivative, self.previous_readings[1][1])) # derivative uses time of second reading
        if len(self.previous_derivatives) == self.previous_derivatives.maxlen:
            return sum(d[0] for d in self.previous_derivatives) / len(self.previous_derivatives), self.previous_derivatives[-1][1]
        else:
            return None

    def reset(self):
        self.start_reading_time = None
        self.max_reading = None
        self.previous_derivatives.clear()
        self.previous_readings.clear()
