from PyQt5.QtCore import QCoreApplication
from PyQt5.QtWidgets import QTabWidget

from tabs.measurements_tab.measurement_region_tab import MeasurementRegionTab


class MeasurementsTab(QTabWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, *kwargs)
        self.setObjectName("measurementsTab")
        self.tab_count = 0
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


    def create_tab(self, name):
        self.tab_count += 1
        self.new_tab = MeasurementRegionTab()
        self.addTab(self.new_tab, "")
        self.new_tab.setObjectName(name+"_tab")
        self.setTabText(self.tab_count, QCoreApplication.translate("MainWindow", "Default"))
