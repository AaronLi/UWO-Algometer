from PyQt5 import QtGui
from PyQt5.QtCore import QRect, QCoreApplication
from PyQt5.QtWidgets import QWidget, QGridLayout, QLabel, QPushButton, QTableWidget, QTableWidgetItem, QMessageBox

from algometer_graph import AlgometerReadingGraph
import algometer_data

class MeasurementRegionTab(QWidget):
    def __init__(self):
        super().__init__()
        self.setObjectName("measurement_tab_content")
        self.gridLayout = QGridLayout(self)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.left_side_label = QLabel(self)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.left_side_label.setFont(font)
        self.left_side_label.setText("Left Side")
        self.gridLayout.addWidget(self.left_side_label, 0, 0, 1, 1)
        self.right_side_label = QLabel(self)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.right_side_label.setFont(font)
        self.right_side_label.setText("Right Side")
        self.gridLayout.addWidget(self.right_side_label, 0, 1, 1, 1)
        self.record_left = QPushButton(self)
        self.record_left.setObjectName("record_left")
        self.gridLayout.addWidget(self.record_left, 1, 0, 1, 1)
        self.record_right = QPushButton(self)
        self.record_right.setObjectName("record_right")
        self.gridLayout.addWidget(self.record_right, 1, 1, 1, 1)
        self.tableWidget = QTableWidget(self)
        self.tableWidget.setShowGrid(True)
        self.tableWidget.setWordWrap(False)
        self.tableWidget.setRowCount(10)
        self.tableWidget.setColumnCount(2)
        self.tableWidget.setObjectName("tableWidget")
        self.gridLayout.addWidget(self.tableWidget, 2, 0, 1, 2)

        self.algometer_widget = AlgometerReadingGraph()
        self.gridLayout.addWidget(self.algometer_widget, 1, 3, 2, 1)

        self.record_left.clicked.connect(self.on_start_recording_left)
        self.record_right.clicked.connect(self.on_start_recording_right)

        self.retranslateUi()

    def retranslateUi(self):
        self.record_left.setText(QCoreApplication.translate("MainWindow", "Start\nRecording"))
        self.record_right.setText(QCoreApplication.translate("MainWindow", "Start\nRecording"))

    def get_region_index(self) -> int:
        return self.parent().children().index(self)

    def on_start_recording_left(self):
        if algometer_data.algometer is None:
            QMessageBox.information(self, "No Algometer Connected", "Please go to the Config tab to connect an Algometer")
            return
        if self.algometer_widget.is_reading():
            self.algometer_widget.stop_reading()
            algometer_data.readings[self.get_region_index()].append(('left', self.algometer_widget.get_max_reading()))
            self.update_reading_table()
            self.record_right.setEnabled(True)
            self.record_left.setText(QCoreApplication.translate("MainWindow", "Start\nRecording"))
        else:
            self.algometer_widget.reset()
            self.record_right.setEnabled(False)
            self.record_left.setText(QCoreApplication.translate("MainWindow", "Stop\nRecording"))
            self.algometer_widget.start_reading(algometer_data.algometer)

    def on_start_recording_right(self):
        if algometer_data.algometer is None:
            QMessageBox.information(self, "No Algometer Connected", "Please go to the Config tab to connect an Algometer")
            return
        if self.algometer_widget.is_reading():
            self.algometer_widget.stop_reading()
            algometer_data.readings[self.get_region_index()].append(('right', self.algometer_widget.get_max_reading()))
            self.update_reading_table()
            self.record_left.setEnabled(True)
            self.record_right.setText(QCoreApplication.translate("MainWindow", "Start\nRecording"))
        else:
            self.algometer_widget.reset()
            self.record_left.setEnabled(False)
            self.record_right.setText(QCoreApplication.translate("MainWindow", "Stop\nRecording"))
            self.algometer_widget.start_reading(algometer_data.algometer)

    def update_reading_table(self):
        self.tableWidget.clear()
        left_readings = 0
        right_readings = 0
        for i, reading in enumerate(algometer_data.readings[self.get_region_index()]):
            if reading[0] == 'left':
                self.tableWidget.setItem(left_readings, 0, QTableWidgetItem(str(reading[1])))
                left_readings += 1
            elif reading[0] == 'right':
                self.tableWidget.setItem(right_readings, 1, QTableWidgetItem(str(reading[1])))
                right_readings += 1
