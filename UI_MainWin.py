import os
import sys

from PyQt5 import QtCore, QtWidgets, QtGui
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QMainWindow, QApplication

import algometer_data
from normative_data import NormativeDataTable
from tabs.analysis_tab.analysis_tab import AnalysisTab
from tabs.config_tab.config_tab import ConfigTab
from tabs.measurements_tab.measurements_tab import MeasurementsTab
from tabs.patientinfo_tab import PatientInfoTab
from userDataPrinter import print_pdf


class AlgometerApp(QMainWindow):
    def __init__(self, *args, **kwargs):
        super(AlgometerApp, self).__init__(*args, **kwargs)
        self.setWindowTitle("Algometer Program")
        self.setWindowIcon(QtGui.QIcon('logo.png'))
        self.setObjectName("MainWindow")
        self.resize(1000, 650)

        # list of measured areas
        self.measured_areas = []

        self.normative_data = NormativeDataTable('normative_data_1.json')

        self.tab_region_id_monotonic = 0

        self.centralwidget = QtWidgets.QWidget(self)
        self.centralwidget.setObjectName("centralwidget")
        self.formLayout = QtWidgets.QFormLayout(self.centralwidget)
        self.formLayout.setObjectName("formLayout")

        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName("tabWidget")

        self.patient_info_tab = PatientInfoTab()
        self.tabWidget.addTab(self.patient_info_tab, "")

        self.measurement_tab = MeasurementsTab(on_stop_reading_callback=self.update_analysis_tab)
        self.measurement_tab.setObjectName("measurement_tab")
        self.tabWidget.addTab(self.measurement_tab, "")
        self.tabWidget.currentChanged.connect(self.measurement_tab.stop_all_readings)

        self.analysisTab = AnalysisTab()
        self.analysisTab.setObjectName("analysisTab")
        self.tabWidget.addTab(self.analysisTab, "")

        self.configTab = ConfigTab()
        self.configTab.setObjectName("configTab")
        self.tabWidget.addTab(self.configTab, "")

        self.formLayout.setWidget(0, QtWidgets.QFormLayout.SpanningRole, self.tabWidget)
        self.setCentralWidget(self.centralwidget)

        self.retranslateUi()
        self.tabWidget.setCurrentIndex(0)
        self.measurement_tab.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(self)

        # connecting buttons here
        self.patient_info_tab.add_measurement_button.clicked.connect(self.on_measure_area_add)
        self.patient_info_tab.print_button.clicked.connect(self.on_print_button_clicked)
        self.patient_info_tab.sex_box.currentIndexChanged.connect(self.set_patient_sex)
        self.set_patient_sex()
        self.patient_info_tab.name_box.textChanged.connect(self.on_name_update)

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.centralwidget.parent().setWindowTitle(_translate("MainWindow", "Algometer Application"))
        self.patient_info_tab.retranslateUi()
        self.measurement_tab.retranslateUi()
        self.analysisTab.retranslateUi()
        self.configTab.retranslateUi()
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.patient_info_tab), _translate("MainWindow", "Patient Info"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.measurement_tab), _translate("MainWindow", "Measurements"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.analysisTab), _translate("MainWindow", "Analysis"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.configTab), _translate("MainWindow", "Config"))


    #functionality of the program

    def on_measurement_area_remove(self):
        current_index = self.patient_info_tab.comboBox.currentIndex()
        ## do all of the stuff needed to delete a measurement
        #
        #
        #
        #

    def on_name_update(self):
        self.analysisTab.patient_name_label.setText(self.patient_info_tab.name_box.text())


    def update_analysis_tab(self):
        self.analysisTab.update_regions(self.measured_areas, self.normative_data)

    def on_measure_area_add(self):
        current_index = self.patient_info_tab.comboBox.currentIndex()
        selected_location_measurementlocation = self.patient_info_tab.comboBox.itemData(current_index,
                                                              role=Qt.UserRole)
        algometer_data.readings[self.tab_region_id_monotonic] = (selected_location_measurementlocation, [])
        self.measurement_tab.create_tab(selected_location_measurementlocation, self.tab_region_id_monotonic)
        self.measured_areas.append((self.tab_region_id_monotonic, selected_location_measurementlocation))
        self.update_analysis_tab()
        self.patient_info_tab.update_measured_areas(self.measured_areas)
        self.tab_region_id_monotonic += 1

    def on_print_button_clicked(self):
        name_text = self.patient_info_tab.name_box.text()
        age_text = self.patient_info_tab.age_box.text()
        height_text = self.patient_info_tab.height_box.text()
        weight_text = self.patient_info_tab.weight_box.text()
        formatted_name = name_text.replace(" ", "_")
        path = "{}_Report.pdf".format(formatted_name)
        comment = self.patient_info_tab.comment_box.text()
        print_pdf(name_text, age_text, height_text, weight_text, comment, self.measured_areas)
        os.system(path)

    def set_patient_sex(self):
        new_selection = self.patient_info_tab.sex_box.itemData(self.patient_info_tab.sex_box.currentIndex(), role=Qt.UserRole)
        algometer_data.patient_sex = new_selection
        self.update_analysis_tab()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_win = AlgometerApp()
    main_win.show()
    sys.exit(app.exec_())
