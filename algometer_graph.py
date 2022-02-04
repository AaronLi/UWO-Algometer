"""
PyQt5 widget for displaying algometer pressure over time info
"""
import time

import numpy as np
import pyqtgraph as pg
import serial
from PyQt5 import QtCore, QtGui

from algometer.algometer import Unit, Algometer, MeasurementLocation, AlgometerReading
from reading_analyzer import ReadingAnalyzer


class AlgometerReadingGraph(pg.PlotWidget):
    def __init__(self, location: MeasurementLocation, parent=None, size=(400, 300)):
        super(AlgometerReadingGraph, self).__init__(parent)
        self.location = location
        self.setLabel('left', 'Force', units='deg')
        self.setLabel('bottom', 'Time', units='s')
        self.setMinimumSize(*size)
        self.setWindowTitle('Algometer Reading')
        self.graph = pg.PlotDataItem()
        plotitem = pg.PlotItem()
        plotitem.addItem(self.graph)
        plotitem.setYRange(-2.5, 3.5)
        self.target_line = pg.InfiniteLine(pos=0.449, angle=0, movable=False, pen=pg.mkPen('r', width=2))
        plotitem.addItem(self.target_line)
        plotitem.addLine(y=0.449 -0.25)
        plotitem.addLine(y=0.449 +0.25)
        plotitem.setMouseEnabled(x=False, y=False)
        plotitem.setMenuEnabled(False)
        self.setCentralItem(plotitem)
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.make_reading)
        self.algometer: Algometer = None
        self.reading_analyzer = ReadingAnalyzer()
        self.readings = []
        self.reading_times = []

    def start_reading(self, algometer: Algometer):
        self.algometer = algometer
        self.start_reading_time = time.time()
        self.timer.start(100)

    def stop_reading(self):
        self.timer.stop()
        self.algometer = None

    def make_reading(self):  # updates the widget
        try:
            response = self.algometer.get_reading(Unit.LBF, self.location)
            derivative = self.reading_analyzer.add_reading(response, time.time())
            if derivative is not None:
                value, reading_time = derivative
                self.readings.append(value)
                self.reading_times.append(reading_time)
                self.graph.setData(x=np.array(self.reading_times), y=np.array(self.readings))
        except serial.SerialTimeoutException:
            pass
        except ValueError:
            pass

    def reset(self):
        self.reading_analyzer.reset()
        self.readings = []
        self.reading_times = []
        self.graph.setData(x=[], y=[])

    def get_max_reading(self) -> AlgometerReading:
        return self.reading_analyzer.max_reading

    def freeze(self, parent=None):
        """
        Creates a copy of this graph
        :return:
        """
        new_reading = AlgometerReadingGraph(parent)
        new_reading.readings = self.readings.copy()
        new_reading.reading_times = self.reading_times.copy()
        new_reading.graph.setData(x=np.array(new_reading.reading_times), y=np.array(new_reading.readings))

        return new_reading

    def is_reading(self) -> bool:
        return self.algometer is not None and self.timer.isActive()