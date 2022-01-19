from PyQt5.QtWidgets import QWidget

from algometer.development_testing.algometer_development_testing import DevelopmentAlgometer


class DevelopmentAlgometerBuilder:
    def __init__(self):
        pass

    def build(self, data: QWidget) -> DevelopmentAlgometer:
        return DevelopmentAlgometer()