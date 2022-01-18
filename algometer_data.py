# this file serves as a "singleton" for the data that is used in the algometer
import enum
from collections import defaultdict

algometer = None

readings = defaultdict(list)
