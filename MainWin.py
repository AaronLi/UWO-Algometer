import sys
from PyQt5 import QtGui, QtCore
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget
from UI_MainWin import Ui_MainWindow
from userDataPrinter import print_pdf
import os


from algometer_graph import AlgometerReadingGraph

class MainWindow:
    def __init__(self):
        self.main_win = QMainWindow()
        self.ui = Ui_MainWindow()
        self.main_win.setWindowTitle("Algometer Program")
        self.main_win.setWindowIcon(QtGui.QIcon('logo.png'))
        self.ui.setupUi(self.main_win)

        #connecting buttons here
        self.ui.patient_info_tab.add_measurement_button.clicked.connect(self.on_measure_area_add)


    def show(self):
        self.main_win.show()

    def on_measure_area_add(self):
        currentIndex = self.ui.patient_info_tab.comboBox.currentIndex()
        self.ui.patient_info_tab.listWidget.addItem(self.ui.patient_info_tab.comboBox.itemText(currentIndex))
        self.add_measurement_tab()

    def add_measurement_tab(self):
        self.newTab = QWidget()
        new_area = self.ui.patient_info_tab.comboBox.itemText(self.ui.patient_info_tab.comboBox.currentIndex())
        self.ui.measurement_tab.create_tab(new_area)



if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_win = MainWindow()
    main_win.show()
    sys.exit(app.exec_())


