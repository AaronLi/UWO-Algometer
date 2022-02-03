from PyQt5.QtCore import QCoreApplication
from PyQt5.QtWidgets import QTabWidget

from tabs.measurements_tab.measurement_region_tab import MeasurementRegionTab
from algometer.algometer import MeasurementLocation

class MeasurementsTab(QTabWidget):

    def __init__(self, *args, on_stop_reading_callback: callable = None, **kwargs):
        """
        Constructor
        @param args:
        @param on_stop_reading_callback: Called every time algometer readings are stopped
        @param kwargs:
        """
        super().__init__(*args, *kwargs)
        self.setObjectName("measurementsTab")
        self.tab_count = -1
        self.on_stop_reading_callback = on_stop_reading_callback
        measurement_tab_content = MeasurementRegionTab(MeasurementLocation.OTHER, -1, on_stop_reading=self.on_stop_reading_callback)
        self.addTab(measurement_tab_content, "")

    def stop_all_readings(self):
        for child_tab in self.children():
            if type(child_tab) == MeasurementRegionTab:
                child_tab.stop_reading()

    def retranslateUi(self):
        #measurement_tab_content.retranslateUi()

        self.setTabText(0, QCoreApplication.translate("MainWindow", "Default"))

    def create_tab(self, location: MeasurementLocation, region_id: int) -> MeasurementRegionTab:
        self.tab_count += 1
        # delete default tab if adding a new one
        if self.tab_count == 0:
            self.removeTab(0)
        new_tab = MeasurementRegionTab(location, region_id, on_stop_reading=self.on_stop_reading_callback)
        self.addTab(new_tab, "")
        new_tab.setObjectName(str(location) + "_tab")
        self.setTabText(self.tab_count, QCoreApplication.translate("MainWindow", str(location)))
        return new_tab
