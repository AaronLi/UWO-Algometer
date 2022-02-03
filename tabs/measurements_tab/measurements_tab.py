from PyQt5.QtCore import QCoreApplication
from PyQt5.QtWidgets import QTabWidget

from tabs.measurements_tab.measurement_region_tab import MeasurementRegionTab
from algometer.algometer import MeasurementLocation

class MeasurementsTab(QTabWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, *kwargs)
        self.setObjectName("measurementsTab")
        self.tab_count = -1
        measurement_tab_content = MeasurementRegionTab(MeasurementLocation.OTHER)
        self.addTab(measurement_tab_content, "")

    def stop_all_readings(self):
        for tab in range(self.count()):
            child_tab = self.widget(tab)
            if type(child_tab) == MeasurementRegionTab:
                child_tab.stop_reading()

    def retranslateUi(self):
        #measurement_tab_content.retranslateUi()

        self.setTabText(0, QCoreApplication.translate("MainWindow", "Default"))

    def create_tab(self, location: MeasurementLocation) -> MeasurementRegionTab:
        self.tab_count += 1
        # delete default tab if adding a new one
        if self.tab_count == 0:
            self.removeTab(0)
        new_tab = MeasurementRegionTab(location)
        self.addTab(new_tab, "")
        new_tab.setObjectName(str(location) + "_tab")
        self.setTabText(self.tab_count, QCoreApplication.translate("MainWindow", str(location)))
        return new_tab
