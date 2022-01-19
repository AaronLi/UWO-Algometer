from typing import Type

from PyQt5.QtWidgets import QWidget

from algometer.algometer import Algometer
from algometer.development_testing.algometer_development_testing import DevelopmentAlgometer
from algometer.development_testing.development_testing_builder import DevelopmentAlgometerBuilder
from algometer.wagnerfpx.algometer_wagnerfpx import AlgometerWagnerFPX
from algometer.wagnerfpx.wagnerfpx_builder import WagnerFPXBuilder


class AlgometerBuilder:
    def __init__(self):
        pass

    def build(self, algometer_type: Type[Algometer], config: QWidget):
        if algometer_type == AlgometerWagnerFPX:
            return WagnerFPXBuilder().build(config)
        elif algometer_type == DevelopmentAlgometer:
            return DevelopmentAlgometerBuilder().build(config)