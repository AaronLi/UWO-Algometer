from typing import Hashable
import numpy as np
from PyQt5.QtWidgets import QWidget, QHBoxLayout, QLabel
import pyqtgraph as pg

import algometer_data


class MeasurementQuartileWidget(QWidget):
    def __init__(self, data_source: Hashable, *args, **kwargs):
        super.__init__(*args, **kwargs)

        self.data_source = data_source

        self.data_plot = pg.BarGraphItem()

        self.plot_widget = pg.PlotWidget()

        self.plot_widget.addItem(self.data_plot)

        horizontal_layout = QHBoxLayout()

        horizontal_layout.addWidget(self.plot_widget)

        self.quartile_text = QLabel()

        horizontal_layout.addWidget(self.quartile_text)

        self.setLayout(horizontal_layout)

    def update_data(self):
        data = algometer_data.readings[self.data_source]
