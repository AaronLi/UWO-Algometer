import pyqtgraph as pg
from PyQt5.QtWidgets import QHBoxLayout, QLabel, QVBoxLayout, QFrame

import algometer_data
import normative_data
from tabs.measurements_tab.measurement_region_tab import MeasurementRegionSide


class MeasurementQuartileWidget(QFrame):
    def __init__(self, region_id: int, norm_data: normative_data.NormativeDataTable = None):
        super().__init__()
        self.data_source = region_id

        data = algometer_data.readings[self.data_source][1]
        left_readings = [reading[1] for reading in data if reading[0] == MeasurementRegionSide.LEFT]
        average_left_reading = sum(left_readings[1:], start=left_readings[0]) / len(left_readings) if len(left_readings) > 0 else None
        right_readings = [reading[1] for reading in data if reading[0] == MeasurementRegionSide.RIGHT]
        average_right_reading = sum(right_readings[1:], start=right_readings[0]) / len(right_readings) if len(right_readings) > 0 else None

        normative_data_table = norm_data.get_normative_data(algometer_data.readings[self.data_source][0], algometer_data.patient_sex)

        self.setFrameShape(QFrame.StyledPanel)
        self.setLineWidth(1)
        self.setFixedHeight(250)

        self.left_data_plot = pg.BarGraphItem(x=range(1,len(left_readings)+1), height=[reading.value for reading in left_readings], width=0.75, brush='b')

        self.left_plot_widget = pg.PlotWidget()
        self.left_plot_widget.setMouseEnabled(False, False)
        self.left_plot_widget.setMenuEnabled(False)


        self.left_plot_widget.addItem(self.left_data_plot)

        if average_left_reading is None:
            self.left_quartile_text = QLabel("No readings")
        elif normative_data_table is not None:
            print(average_left_reading, normative_data_table)
            left_quartile = normative_data_table.get_quartile(average_left_reading)
            label_text = f"{average_left_reading} ({left_quartile}{['', 'st', 'nd', 'rd', 'th'][left_quartile]} Quartile)"
            self.left_quartile_text = QLabel(label_text)
        else:
            self.left_quartile_text = QLabel(f"{average_left_reading}")

        self.left_quartile_layout = QHBoxLayout()
        self.left_quartile_layout.addWidget(self.left_plot_widget)
        self.left_quartile_layout.addWidget(self.left_quartile_text)

        self.right_data_plot = pg.BarGraphItem(x=range(1,len(right_readings)+1), height=[reading.value for reading in right_readings], width=0.75, brush='r')

        self.right_plot_widget = pg.PlotWidget()
        self.right_plot_widget.setMouseEnabled(False, False)
        self.right_plot_widget.setMenuEnabled(False)

        self.right_plot_widget.addItem(self.right_data_plot)

        if average_right_reading is None:
            self.right_quartile_text = QLabel("No readings")
        elif normative_data_table is not None:
            right_quartile = normative_data_table.get_quartile(average_right_reading)
            label_text = f"{average_right_reading} ({right_quartile}{['', 'st', 'nd', 'rd', 'th'][right_quartile]} Quartile)"
            self.right_quartile_text = QLabel(label_text)
        else:
           self.right_quartile_text = QLabel(f"{average_right_reading}")

        self.right_quartile_layout = QHBoxLayout()
        self.right_quartile_layout.addWidget(self.right_plot_widget)
        self.right_quartile_layout.addWidget(self.right_quartile_text)

        self.main_layout = QVBoxLayout(self)
        self.main_layout.addWidget(QLabel(f"{algometer_data.readings[self.data_source][0]}"))
        measurement_row = QHBoxLayout()

        measurement_row.addLayout(self.left_quartile_layout)
        measurement_row.addLayout(self.right_quartile_layout)
        self.main_layout.addLayout(measurement_row)

        #self.main_layout.addWidget(QLabel(f"Region {region_id}"))
        #self.update_data()

    # def update_data(self):
    #
    #     print("Left:", left_readings)
    #     print("Right:", right_readings)
    #     self.left_data_plot.setData(x=left_readings)
    #     self.right_data_plot.setData(x=right_readings)
