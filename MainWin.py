import sys
from PyQt5 import QtGui
from PyQt5.QtWidgets import QMainWindow, QApplication
from UI_MainWin import Ui_MainWindow
from userDataPrinter import print_pdf
import os

class MainWindow:
    def __init__(self):
        self.main_win = QMainWindow()
        self.ui = Ui_MainWindow()
        self.main_win.setWindowTitle("Algometer Program")
        self.main_win.setWindowIcon(QtGui.QIcon('logo.png'))
        self.ui.setupUi(self.main_win)


        #connect signals to slots

        #self.ui.yesButton.clicked.connect(self.on_yes_button_clicked)
        #self.ui.noButton.clicked.connect(self.on_no_button_clicked)
        self.ui.PrintButton.clicked.connect(self.on_print_button_clicked)



    def show(self):
        self.main_win.show()

    def on_yes_button_clicked(self):
        self.ui.label.setText("yes is the answer")

    def on_no_button_clicked(self):
        self.ui.label.setText("no is the answer")

    def on_print_button_clicked(self):
        name_text = self.ui.NameBox.text()
        age_text = self.ui.AgeBox.text()
        height_text = self.ui.HeightBox.text()
        weight_text = self.ui.WeightBox.text()
        age_diff = 65-int(age_text)
        diagnosis_text = "{} years until retirement".format(age_diff)
        formatted_name = name_text.replace(" ", "_")
        path = "{}_Report.pdf".format(formatted_name)
        print_pdf(name_text, age_text, height_text, weight_text, diagnosis_text)
        os.system(path)

    def on_measure_button_clicked(self, measure_value):
        a = 10



if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_win = MainWindow()
    main_win.show()
    sys.exit(app.exec_())
