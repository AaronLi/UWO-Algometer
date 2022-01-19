import os

from PyQt5.QtCore import QRect, QCoreApplication
from PyQt5.QtWidgets import QWidget, QHBoxLayout, QSpacerItem, QSizePolicy, QVBoxLayout, QLabel, QLineEdit, QFormLayout, \
    QComboBox, QPushButton, QListWidget

from userDataPrinter import print_pdf


class PatientInfoTab(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setObjectName("patientInfo")
        self.horizontalLayout = QHBoxLayout(self)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        spacerItem1 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem1)
        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.label_2 = QLabel(self)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_7.addWidget(self.label_2)
        spacerItem2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem2)
        self.NameBox = QLineEdit(self)
        self.NameBox.setObjectName("NameBox")
        self.horizontalLayout_7.addWidget(self.NameBox)
        self.verticalLayout.addLayout(self.horizontalLayout_7)
        spacerItem3 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem3)
        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.label_3 = QLabel(self)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_8.addWidget(self.label_3)
        spacerItem4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        self.horizontalLayout_8.addItem(spacerItem4)
        self.AgeBox = QLineEdit(self)
        self.AgeBox.setObjectName("AgeBox")
        self.horizontalLayout_8.addWidget(self.AgeBox)
        self.verticalLayout.addLayout(self.horizontalLayout_8)
        spacerItem5 = QSpacerItem(20, 48, QSizePolicy.Minimum, QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem5)
        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.label_4 = QLabel(self)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_9.addWidget(self.label_4)
        spacerItem6 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        self.horizontalLayout_9.addItem(spacerItem6)
        self.HeightBox = QLineEdit(self)
        self.HeightBox.setObjectName("HeightBox")
        self.horizontalLayout_9.addWidget(self.HeightBox)
        self.verticalLayout.addLayout(self.horizontalLayout_9)
        spacerItem7 = QSpacerItem(20, 48, QSizePolicy.Minimum, QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem7)
        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.label_5 = QLabel(self)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_10.addWidget(self.label_5)
        spacerItem8 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        self.horizontalLayout_10.addItem(spacerItem8)
        self.WeightBox = QLineEdit(self)
        self.WeightBox.setObjectName("WeightBox")
        self.horizontalLayout_10.addWidget(self.WeightBox)
        self.verticalLayout.addLayout(self.horizontalLayout_10)
        spacerItem9 = QSpacerItem(20, 48, QSizePolicy.Minimum, QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem9)
        self.horizontalLayout.addLayout(self.verticalLayout)
        spacerItem10 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem10)
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        spacerItem11 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem11)
        self.formLayout_2 = QFormLayout()
        self.formLayout_2.setObjectName("formLayout_2")
        self.comboBox = QComboBox(self)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setItemText(4, "")
        self.formLayout_2.setWidget(0, QFormLayout.LabelRole, self.comboBox)
        self.PrintButton_2 = QPushButton(self)
        self.PrintButton_2.setObjectName("PrintButton_2")
        self.formLayout_2.setWidget(1, QFormLayout.LabelRole, self.PrintButton_2)
        self.verticalLayout_2.addLayout(self.formLayout_2)
        spacerItem12 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem12)
        self.listWidget = QListWidget(self)
        self.listWidget.setObjectName("listWidget")
        self.verticalLayout_2.addWidget(self.listWidget)
        spacerItem13 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem13)
        self.PrintButton = QPushButton(self)
        self.PrintButton.setObjectName("PrintButton")
        self.verticalLayout_2.addWidget(self.PrintButton)
        spacerItem14 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem14)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        spacerItem15 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem15)

        self.PrintButton.clicked.connect(self.on_print_button_clicked)

    def retranslateUi(self):
        self.label_2.setText(QCoreApplication.translate("MainWindow", "Name"))
        self.label_3.setText(QCoreApplication.translate("MainWindow", "Age"))
        self.label_4.setText(QCoreApplication.translate("MainWindow", "Height"))
        self.label_5.setText(QCoreApplication.translate("MainWindow", "Weight"))
        self.comboBox.setItemText(0, QCoreApplication.translate("MainWindow", "Neck"))
        self.comboBox.setItemText(1, QCoreApplication.translate("MainWindow", "Bicep"))
        self.comboBox.setItemText(2, QCoreApplication.translate("MainWindow", "Thigh"))
        self.comboBox.setItemText(3, QCoreApplication.translate("MainWindow", "Other (No comparative data)"))
        self.PrintButton_2.setText(QCoreApplication.translate("MainWindow", "Add Measurement"))
        self.PrintButton.setText(QCoreApplication.translate("MainWindow", "Print Report"))

    def on_print_button_clicked(self):
        name_text = self.NameBox.text()
        age_text = self.AgeBox.text()
        height_text = self.HeightBox.text()
        weight_text = self.WeightBox.text()
        age_diff = 65-int(age_text)
        diagnosis_text = "{} years until retirement".format(age_diff)
        formatted_name = name_text.replace(" ", "_")
        path = "{}_Report.pdf".format(formatted_name)
        print_pdf(name_text, age_text, height_text, weight_text, diagnosis_text)
        os.system(path)