from typing import List, Tuple

from PyQt5.QtCore import QRect, QCoreApplication, Qt
from PyQt5.QtWidgets import QWidget, QLabel, QGridLayout, QVBoxLayout, QListWidget, QWidgetItem, QListWidgetItem, \
    QScrollArea, QFrame, QSizePolicy

import algometer_data
from algometer.algometer import MeasurementLocation
from tabs.analysis_tab.region_measurement_quartile_widget import MeasurementQuartileWidget


class AnalysisTab(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.setObjectName("analysisTab")
        layout = QVBoxLayout(self)
        self.patient_name_label = QLabel()
        self.subplots = QScrollArea(widgetResizable=True, verticalScrollBarPolicy=Qt.ScrollBarAlwaysOn)
        self.subplot_widget = QFrame()
        self.subplots.setWidget(self.subplot_widget)
        self.subplot_layout = QVBoxLayout()
        self.subplot_layout.setAlignment(Qt.AlignTop)
        self.subplot_widget.setLayout(self.subplot_layout)
        layout.addWidget(self.patient_name_label)
        layout.addWidget(self.subplots)

    def update_regions(self, regions: List[Tuple[int, MeasurementLocation]], normative_data=None) -> None:
        # remove all widgets and create them again with the updated info
        for i in reversed(range(self.subplot_layout.count())):
            to_remove = self.subplot_layout.itemAt(i).widget()
            self.subplot_layout.removeWidget(to_remove)
            to_remove.setParent(None)
        for region in regions:
            new_region = MeasurementQuartileWidget(region[0], normative_data)

            self.subplot_layout.addWidget(new_region)
        self.subplots.update()

    def retranslateUi(self):
        self.patient_name_label.setText(QCoreApplication.translate("MainWindow", "Patient Name Here"))
