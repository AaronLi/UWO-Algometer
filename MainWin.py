import os
import sys

from PyQt5 import QtGui
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget

from UI_MainWin import Ui_MainWindow
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


    def show(self):
        self.main_win.show()

    def on_measure_area_add(self):
        currentIndex = self.ui.patient_info_tab.comboBox.currentIndex()
        self.ui.patient_info_tab.list_widget.addItem(self.ui.patient_info_tab.comboBox.itemText(currentIndex))
        self.add_measurement_tab()
        self.measured_areas.append(self.ui.patient_info_tab.comboBox.itemText(currentIndex))

    def add_measurement_tab(self):
        self.newTab = QWidget()
        new_area = self.ui.patient_info_tab.comboBox.itemText(self.ui.patient_info_tab.comboBox.currentIndex())
        self.ui.measurement_tab.create_tab(new_area)

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


