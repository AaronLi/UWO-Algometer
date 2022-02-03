import os
import sys

from PyQt5 import QtGui
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget

import algometer_data
from UI_MainWin import Ui_MainWindow
from tabs.measurements_tab.measurement_region_tab import MeasurementRegionTab
from userDataPrinter import print_pdf


class MainWindow:
    def __init__(self):
        self.main_win = QMainWindow()
        self.ui = Ui_MainWindow(self.main_win)
        self.main_win.setWindowTitle("Algometer Program")
        self.main_win.setWindowIcon(QtGui.QIcon('logo.png'))


        #list of measured areas
        self.measured_areas = []

        #connecting buttons here
        self.ui.patient_info_tab.add_measurement_button.clicked.connect(self.on_measure_area_add)
        self.ui.patient_info_tab.print_button.clicked.connect(self.on_print_button_clicked)

        self.tab_region_id_monotonic = 0


    def show(self):
        self.main_win.show()

    def on_measure_area_add(self):
        currentIndex = self.ui.patient_info_tab.comboBox.currentIndex()
        selected_location_measurementlocation = self.ui.patient_info_tab.comboBox.itemData(currentIndex,
                                                              role=Qt.UserRole)
        self.ui.measurement_tab.create_tab(selected_location_measurementlocation, self.tab_region_id_monotonic)
        self.measured_areas.append((self.tab_region_id_monotonic, selected_location_measurementlocation))
        self.ui.patient_info_tab.update_measured_areas(self.measured_areas)
        self.tab_region_id_monotonic += 1

    def on_print_button_clicked(self):
        name_text = self.ui.patient_info_tab.name_box.text()
        age_text = self.ui.patient_info_tab.age_box.text()
        height_text = self.ui.patient_info_tab.height_box.text()
        weight_text = self.ui.patient_info_tab.weight_box.text()
        formatted_name = name_text.replace(" ", "_")
        path = "{}_Report.pdf".format(formatted_name)
        comment = self.ui.patient_info_tab.comment_box.text()
        print_pdf(name_text, age_text, height_text, weight_text, comment, self.measured_areas)
        os.system(path)



if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_win = MainWindow()
    main_win.show()
    sys.exit(app.exec_())


