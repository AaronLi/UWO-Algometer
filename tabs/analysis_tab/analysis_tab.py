from PyQt5.QtWidgets import QWidget, QGraphicsView, QLabel, QGraphicsView
from PyQt5.QtCore import QRect, QCoreApplication

import algometer_data


class AnalysisTab(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.setObjectName("analysisTab")
        self.left_graph_1 = QGraphicsView(self)
        self.left_graph_1.setGeometry(QRect(40, 90, 256, 192))
        self.left_graph_1.setObjectName("left_graph_1")
        self.patient_name_label = QLabel(self)
        self.patient_name_label.setGeometry(QRect(60, 40, 231, 20))
        self.patient_name_label.setObjectName("patient_name_label")
        self.left_quartile_1 = QLabel(self)
        self.left_quartile_1.setGeometry(QRect(310, 140, 81, 20))
        self.left_quartile_1.setObjectName("left_quartile_1")
        self.right_quartile_1 = QLabel(self)
        self.right_quartile_1.setGeometry(QRect(690, 140, 81, 20))
        self.right_quartile_1.setObjectName("right_quartile_1")
        self.right_graph_1 = QGraphicsView(self)
        self.right_graph_1.setGeometry(QRect(420, 90, 256, 192))
        self.right_graph_1.setObjectName("right_graph_1")

    def update(self) -> None:
        print(algometer_data.readings)

    def retranslateUi(self):
        self.patient_name_label.setText(QCoreApplication.translate("MainWindow", "Patient Name Here"))
        self.left_quartile_1.setText(QCoreApplication.translate("MainWindow", "xth quartile"))
        self.right_quartile_1.setText(QCoreApplication.translate("MainWindow", "xth quartile"))
