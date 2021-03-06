import os
from typing import List, Tuple

from PyQt5.QtCore import QRect, QCoreApplication
from PyQt5.QtWidgets import QWidget, QHBoxLayout, QSpacerItem, QSizePolicy, QVBoxLayout, QLabel, QLineEdit, QFormLayout, \
    QComboBox, QPushButton, QListWidget

import normative_data
from algometer.algometer import MeasurementLocation
from userDataPrinter import print_pdf


class PatientInfoTab(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setObjectName("patientInfo")
        horizontalLayout = QHBoxLayout(self)
        horizontalLayout.setContentsMargins(0, 0, 0, 0)
        horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        horizontalLayout.addItem(spacerItem)
        verticalLayout = QVBoxLayout()
        verticalLayout.setObjectName("verticalLayout")
        spacerItem1 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)
        verticalLayout.addItem(spacerItem1)
        horizontalLayout_7 = QHBoxLayout()
        horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.label_2 = QLabel(self)
        self.label_2.setObjectName("label_2")
        horizontalLayout_7.addWidget(self.label_2)
        spacerItem2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        horizontalLayout_7.addItem(spacerItem2)
        self.name_box = QLineEdit(self)
        self.name_box.setObjectName("self.name_box")
        horizontalLayout_7.addWidget(self.name_box)
        verticalLayout.addLayout(horizontalLayout_7)

        sex_layout = QHBoxLayout()
        self.sex_label = QLabel(self)
        self.sex_label.setText("Sex")
        sex_layout.addWidget(self.sex_label)
        self.sex_box = QComboBox(self)
        self.sex_box.addItem("Male", normative_data.Sex.MALE)
        self.sex_box.addItem("Female", normative_data.Sex.FEMALE)
        self.sex_box.addItem("Other (No normative data)", normative_data.Sex.OTHER)
        sex_layout.addWidget(self.sex_box)
        spacerItem21 = QSpacerItem(20, 40, QSizePolicy.Expanding, QSizePolicy.Minimum)
        verticalLayout.addItem(spacerItem21)
        verticalLayout.addLayout(sex_layout)

        spacerItem3 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)
        verticalLayout.addItem(spacerItem3)
        horizontalLayout_8 = QHBoxLayout()
        horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.label_3 = QLabel(self)
        self.label_3.setObjectName("label_3")
        horizontalLayout_8.addWidget(self.label_3)
        spacerItem4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        horizontalLayout_8.addItem(spacerItem4)
        self.age_box = QLineEdit(self)
        self.age_box.setObjectName("age_box")
        horizontalLayout_8.addWidget(self.age_box)
        verticalLayout.addLayout(horizontalLayout_8)
        spacerItem5 = QSpacerItem(20, 48, QSizePolicy.Minimum, QSizePolicy.Expanding)
        verticalLayout.addItem(spacerItem5)
        horizontal_layout_9 = QHBoxLayout()
        horizontal_layout_9.setObjectName("horizontalLayout_9")
        self.label_4 = QLabel(self)
        self.label_4.setObjectName("label_4")
        horizontal_layout_9.addWidget(self.label_4)
        spacerItem6 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        horizontal_layout_9.addItem(spacerItem6)
        self.height_box = QLineEdit(self)
        self.height_box.setObjectName("HeightBox")
        horizontal_layout_9.addWidget(self.height_box)
        verticalLayout.addLayout(horizontal_layout_9)
        spacerItem7 = QSpacerItem(20, 48, QSizePolicy.Minimum, QSizePolicy.Expanding)
        verticalLayout.addItem(spacerItem7)
        horizontal_layout_10 = QHBoxLayout()
        horizontal_layout_10.setObjectName("horizontalLayout_10")
        self.label_5 = QLabel(self)
        self.label_5.setObjectName("label_5")
        horizontal_layout_10.addWidget(self.label_5)
        spacerItem8 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        horizontal_layout_10.addItem(spacerItem8)
        self.weight_box = QLineEdit(self)
        self.weight_box.setObjectName("WeightBox")
        horizontal_layout_10.addWidget(self.weight_box)
        verticalLayout.addLayout(horizontal_layout_10)
        spacerItem9 = QSpacerItem(20, 48, QSizePolicy.Minimum, QSizePolicy.Expanding)
        verticalLayout.addItem(spacerItem9)

        ##test

        comment_horizontal_box = QHBoxLayout()
        comment_horizontal_box.setObjectName("comment_horizontal_box")
        self.comment_label = QLabel(self)
        self.comment_label.setObjectName("comment_label")
        comment_horizontal_box.addWidget(self.comment_label)
        comment_spacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        comment_horizontal_box.addItem(comment_spacer)
        self.comment_box = QLineEdit(self)
        self.comment_box.setObjectName("CommentBox")
        comment_horizontal_box.addWidget(self.comment_box)
        verticalLayout.addLayout(comment_horizontal_box)
        comment_bottom_spacer = QSpacerItem(20, 48, QSizePolicy.Minimum, QSizePolicy.Expanding)
        verticalLayout.addItem(comment_bottom_spacer)
        ##test


        horizontalLayout.addLayout(verticalLayout)
        spacerItem10 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        horizontalLayout.addItem(spacerItem10)
        vertical_layout_2 = QVBoxLayout()
        vertical_layout_2.setObjectName("verticalLayout_2")
        spacerItem11 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)
        vertical_layout_2.addItem(spacerItem11)
        form_layout_2 = QFormLayout()
        form_layout_2.setObjectName("formLayout_2")
        self.comboBox = QComboBox(self)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("", MeasurementLocation.UPPER_FIBERS_OF_TRAPEZIUS)
        self.comboBox.addItem("", MeasurementLocation.TIBIALIS_ANTERIOR)
        self.comboBox.addItem("", MeasurementLocation.OTHER)
        form_layout_2.setWidget(0, QFormLayout.LabelRole, self.comboBox)
        self.add_measurement_button = QPushButton(self)
        self.add_measurement_button.setObjectName("add_measurement_button")
        form_layout_2.setWidget(1, QFormLayout.LabelRole, self.add_measurement_button)
        self.remove_measurement_button = QPushButton(self)
        self.remove_measurement_button.setObjectName("remove_measurement_button")
        form_layout_2.setWidget(2, QFormLayout.LabelRole, self.remove_measurement_button)
        vertical_layout_2.addLayout(form_layout_2)
        spacerItem12 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)
        vertical_layout_2.addItem(spacerItem12)
        self.list_widget = QListWidget(self)
        self.list_widget.setObjectName("list_widget")
        vertical_layout_2.addWidget(self.list_widget)
        spacerItem13 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)
        vertical_layout_2.addItem(spacerItem13)
        self.print_button = QPushButton(self)
        self.print_button.setObjectName("PrintButton")
        vertical_layout_2.addWidget(self.print_button)
        spacerItem14 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)
        vertical_layout_2.addItem(spacerItem14)
        horizontalLayout.addLayout(vertical_layout_2)
        spacerItem15 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        horizontalLayout.addItem(spacerItem15)

    def update_measured_areas(self, areas: List[Tuple[int, MeasurementLocation]]):
        self.list_widget.clear()

        for area in areas:
            self.list_widget.addItem(str(area[1]))

    def retranslateUi(self):
        self.label_2.setText(QCoreApplication.translate("MainWindow", "Name"))
        self.label_3.setText(QCoreApplication.translate("MainWindow", "Age"))
        self.label_4.setText(QCoreApplication.translate("MainWindow", "Height"))
        self.label_5.setText(QCoreApplication.translate("MainWindow", "Weight"))
        self.comment_label.setText(QCoreApplication.translate("MainWindow", "Comment"))
        self.comboBox.setItemText(0, QCoreApplication.translate("MainWindow", "Upper Fibers of Trapezius"))
        self.comboBox.setItemText(1, QCoreApplication.translate("MainWindow", "Tibialis Anterior"))
        self.comboBox.setItemText(2 , QCoreApplication.translate("MainWindow", "Other (No comparative data)"))
        self.add_measurement_button.setText(QCoreApplication.translate("MainWindow", "Add Measurement"))
        self.remove_measurement_button.setText(QCoreApplication.translate("MainWindow", "Remove Measurement"))
        self.print_button.setText(QCoreApplication.translate("MainWindow", "Print Report"))

"""
    def on_print_button_clicked(self):
        name_text = self.name_box.text()
        age_text = self.age_box.text()
        height_text = self.height_box.text()
        weight_text = self.weight_box.text()
        age_diff = 65-int(age_text)
        diagnosis_text = "{} years until retirement".format(age_diff)
        formatted_name = name_text.replace(" ", "_")
        path = "{}_Report.pdf".format(formatted_name)
        print_pdf(name_text, age_text, height_text, weight_text, diagnosis_text)
        os.system(path)
"""
