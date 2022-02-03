from PyQt5.QtWidgets import QWidget

import algometer_data


class AnalysisTab(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def update(self) -> None:
        print(algometer_data.readings)

    def retranslateUi(self):
        pass