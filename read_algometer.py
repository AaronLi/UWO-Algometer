import PyQt5
from PyQt5 import QtCore
from PyQt5.QtWidgets import QApplication, QMainWindow
import numpy as np
import pyqtgraph as pg
import serial
import time
from serial.tools import list_ports

from algometer import Unit
from algometer_wagnerfpx import AlgometerWagnerFPX

ports = list_ports.comports()

if len(ports) == 1:
    desired_port = 0
else:
    for i, port in enumerate(ports):
        print(i, port.name)
    desired_port = int(input('Select a port: '))
reader = serial.Serial(ports[desired_port].name, 9600)
wagner = AlgometerWagnerFPX(reader)
readings = []
reading_times = []
app = QApplication([])
window = QMainWindow()
window.setMinimumSize(800, 600)
window.setWindowTitle('Algometer')
graph = pg.PlotCurveItem()
plot_item = pg.PlotItem()
plot_item.addItem(graph)
ui_widget = pg.PlotWidget(window, plotItem=plot_item) # the actual widget used for plotting
ui_widget.setMinimumSize(800, 600)
window.show()

start_reading_time = time.time()
def update(): # updates the widget
    response = wagner.get_reading(Unit.N)
    reading_times.append(time.time() - start_reading_time)
    readings.append(-response[0])
    graph.setData(x=np.array(reading_times), y=np.array(readings))
    app.processEvents(QtCore.QEventLoop.ExcludeUserInputEvents)


timer = QtCore.QTimer()
timer.timeout.connect(update)
timer.start(100) # calls update every x ms
app.exec_()
reader.close()
