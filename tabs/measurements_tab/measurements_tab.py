from PyQt5.QtCore import QCoreApplication
from PyQt5.QtWidgets import QTabWidget

from tabs.measurements_tab.measurement_region_tab import MeasurementRegionTab


class MeasurementsTab(QTabWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, *kwargs)
        self.setObjectName("measurementsTab")
        self.measurement_tab_content = MeasurementRegionTab()
        self.addTab(self.measurement_tab_content, "")

    def stop_all_readings(self):
        for tab in range(self.count()):
            child_tab = self.widget(tab)
            if type(child_tab) == MeasurementRegionTab:
                child_tab.stop_reading()


    def retranslateUi(self):
        self.measurement_tab_content.retranslateUi()

        "Uncomment below once multiple measurements are implemented"
        self.setTabText(0, QCoreApplication.translate("MainWindow", "Default"))