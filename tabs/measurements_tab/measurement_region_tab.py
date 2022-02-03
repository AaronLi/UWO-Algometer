import enum
from typing import Hashable

from PyQt5 import QtGui
from PyQt5.QtCore import QRect, QCoreApplication, QSize
from PyQt5.QtWidgets import QWidget, QGridLayout, QLabel, QPushButton, QTableWidget, QTableWidgetItem, QMessageBox

from algometer.algometer import MeasurementLocation
from algometer_graph import AlgometerReadingGraph
import algometer_data

class MeasurementRegionSide(enum.Enum):
    NONE = enum.auto()
    LEFT = enum.auto()
    RIGHT = enum.auto()

class MeasurementRegionTab(QWidget):
    def __init__(self, location: MeasurementLocation, region_id: int, on_stop_reading: callable = None):
        super().__init__()

        self.on_stop_reading_callback = on_stop_reading
        self.region_id = region_id
        self.location = location
        self.current_reading_side = MeasurementRegionSide.NONE
        self.setObjectName("measurement_tab_content")
        grid_layout = QGridLayout(self)
        grid_layout.setContentsMargins(0, 0, 0, 0)
        grid_layout.setObjectName("gridLayout")
        self.left_side_label = QLabel(self)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.left_side_label.setFont(font)
        self.left_side_label.setText("Left Side")
        grid_layout.addWidget(self.left_side_label, 0, 0, 1, 1)
        self.right_side_label = QLabel(self)
        self.right_side_label.setFont(font)
        self.right_side_label.setText("Right Side")
        grid_layout.addWidget(self.right_side_label, 0, 1, 1, 1)
        self.record_left = QPushButton(self)
        self.record_left.setObjectName("record_left")
        grid_layout.addWidget(self.record_left, 1, 0, 1, 1)
        self.record_right = QPushButton(self)
        self.record_right.setObjectName("record_right")
        grid_layout.addWidget(self.record_right, 1, 1, 1, 1)
        self.tableWidget = QTableWidget(self)
        self.tableWidget.setShowGrid(True)
        self.tableWidget.setWordWrap(False)
        self.tableWidget.setRowCount(5)
        self.tableWidget.setColumnCount(2)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setMinimumSize(QSize(290, 0))
        grid_layout.addWidget(self.tableWidget, 2, 0, 1, 2)

        self.algometer_widget = AlgometerReadingGraph(location)
        grid_layout.addWidget(self.algometer_widget, 1, 2, 2, 1)

        self.remove_reading = QPushButton(self)
        self.remove_reading.setObjectName("remove_reading")
        grid_layout.addWidget(self.remove_reading, 3, 0, 1, 1)

        self.record_left.clicked.connect(self.on_start_recording_left)
        self.record_right.clicked.connect(self.on_start_recording_right)

        self.retranslateUi()

    def retranslateUi(self):
        self.record_left.setText(QCoreApplication.translate("MainWindow", "Start\nRecording"))
        self.record_right.setText(QCoreApplication.translate("MainWindow", "Start\nRecording"))
        self.remove_reading.setText(QCoreApplication.translate("MainWindow", "Remove Reading"))

    def get_region_identifier(self) -> Hashable:
        return self.region_id

    def on_start_recording_left(self):
        if algometer_data.algometer is None:
            QMessageBox.information(self, "No Algometer Connected",
                                    "Please go to the Config tab to connect an Algometer")
            return
        if self.algometer_widget.is_reading():
            self.stop_reading()
        else:
            self.algometer_widget.reset()
            self.record_right.setEnabled(False)
            self.record_left.setText(QCoreApplication.translate("MainWindow", "Stop\nRecording"))
            self.algometer_widget.start_reading(algometer_data.algometer)
            self.current_reading_side = MeasurementRegionSide.LEFT

    def on_start_recording_right(self):
        if algometer_data.algometer is None:
            QMessageBox.information(self, "No Algometer Connected",
                                    "Please go to the Config tab to connect an Algometer")
            return
        if self.algometer_widget.is_reading():
            self.stop_reading()
        else:
            self.algometer_widget.reset()
            self.record_left.setEnabled(False)
            self.record_right.setText(QCoreApplication.translate("MainWindow", "Stop\nRecording"))
            self.algometer_widget.start_reading(algometer_data.algometer)
            self.current_reading_side = MeasurementRegionSide.RIGHT

    def stop_reading(self):
        if self.current_reading_side is not None:
            self.algometer_widget.stop_reading()
            self.update_reading_table()
            self.record_left.setEnabled(True)
            self.record_right.setEnabled(True)
            self.record_right.setText(QCoreApplication.translate("MainWindow", "Start\nRecording"))
            self.record_left.setText(QCoreApplication.translate("MainWindow", "Start\nRecording"))
            algometer_data.readings[self.get_region_identifier()].append(
                (self.current_reading_side, self.algometer_widget.get_max_reading()))
            try:
                print("calling callback")
                self.on_stop_reading_callback()
            except TypeError:
                pass
            self.current_reading_side = MeasurementRegionSide.NONE

    def update_reading_table(self):
        self.tableWidget.clear()
        left_readings = 0
        right_readings = 0
        for i, reading in enumerate(algometer_data.readings[self.get_region_identifier()]):
            if reading[0] == MeasurementRegionSide.LEFT:
                self.tableWidget.setItem(left_readings, 0, QTableWidgetItem(str(reading[1])))
                left_readings += 1
            elif reading[0] == MeasurementRegionSide.RIGHT:
                self.tableWidget.setItem(right_readings, 1, QTableWidgetItem(str(reading[1])))
                right_readings += 1

# class SingleReadingWidget(QWidget):
