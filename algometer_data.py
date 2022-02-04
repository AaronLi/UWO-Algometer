# this file serves as a "singleton" for the data that is used in the algometer
import enum
from collections import defaultdict
from typing import List, Tuple

import normative_data
from algometer.algometer import AlgometerReading, MeasurementLocation

algometer = None

patient_sex = normative_data.Sex.MALE

measured_areas = []

readings: dict[int, Tuple[MeasurementLocation, List[Tuple['MeasurementRegionSide', AlgometerReading]]]] = {}
