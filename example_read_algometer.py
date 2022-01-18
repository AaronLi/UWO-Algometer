"""
Demonstrates how to use algometer.Algometer along with algometer_graph.AlgometerReadingGraph to
read, record, and display pressure over time
"""

import functools

import serial
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QVBoxLayout, QHBoxLayout, QWidget, QPushButton, \
    QLabel, QScrollArea
from serial.tools import list_ports

import algometer_graph
from algometer.wagnerfpx.algometer_wagnerfpx import AlgometerWagnerFPX
from algometer.development_testing.algometer_development_testing import DevelopmentAlgometer

ports = list_ports.comports()

if len(ports) == 1:
    desired_port = 0
    reader = serial.Serial(ports[desired_port].name, 9600)
    wagner = AlgometerWagnerFPX(reader)
elif len(ports) == 0:
    wagner = DevelopmentAlgometer()
else:
    for i, port in enumerate(ports):
        print(i, port.name)
    desired_port = int(input('Select a port: '))
    reader = serial.Serial(ports[desired_port].name, 9600)
    wagner = AlgometerWagnerFPX(reader)
readings = []
reading_times = []
app = QApplication([])
window = QWidget()
window.setMinimumSize(800, 600)
window.setWindowTitle('Algometer')
# this needs to go after app = QApplication([])
algometer_reader = algometer_graph.AlgometerReadingGraph()
columns = QHBoxLayout(window)
graph_column = QVBoxLayout()
past_reading_list = QScrollArea()
past_reading_list.setWidgetResizable(True)
past_reading_list.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
past_readings = QVBoxLayout(past_reading_list)
past_reading_list_widget = QWidget()
past_reading_list.setWidget(past_reading_list_widget)
past_reading_list_widget.setLayout(past_readings)


max_reading_label = QLabel(str(algometer_reader.get_max_reading()))
def stop_reading_and_update_label():
    algometer_reader.stop_reading()
    reading_and_result = QHBoxLayout()
    result = algometer_reader.freeze()
    reading_and_result.addWidget(result)
    reading_and_result.addWidget(QLabel(str(algometer_reader.get_max_reading())))
    past_readings.insertLayout(0, reading_and_result)
    max_reading_label.setText('peak: '+str(algometer_reader.get_max_reading()))
    algometer_reader.reset()

button_column = QVBoxLayout()
button_column.addWidget(QPushButton('Start', clicked=functools.partial(algometer_reader.start_reading, wagner)))
button_column.addWidget(QPushButton('Stop', clicked=stop_reading_and_update_label))

button_column.addWidget(max_reading_label)

columns.addLayout(button_column)
columns.addLayout(graph_column)
graph_column.addWidget(algometer_reader, stretch=1)
graph_column.addWidget(past_reading_list, stretch=2)
window.show()
app.exec_()
#reader.close()
