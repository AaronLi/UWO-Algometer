# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(832, 615)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName("tabWidget")
        self.patientInfo = QtWidgets.QWidget()
        self.patientInfo.setObjectName("patientInfo")
        self.PrintButton = QtWidgets.QPushButton(self.patientInfo)
        self.PrintButton.setGeometry(QtCore.QRect(680, 500, 111, 41))
        self.PrintButton.setObjectName("PrintButton")
        self.widget = QtWidgets.QWidget(self.patientInfo)
        self.widget.setGeometry(QtCore.QRect(1, 11, 230, 284))
        self.widget.setObjectName("widget")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.label_2 = QtWidgets.QLabel(self.widget)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_7.addWidget(self.label_2)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem)
        self.NameBox = QtWidgets.QLineEdit(self.widget)
        self.NameBox.setObjectName("NameBox")
        self.horizontalLayout_7.addWidget(self.NameBox)
        self.verticalLayout_5.addLayout(self.horizontalLayout_7)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.label_3 = QtWidgets.QLabel(self.widget)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_8.addWidget(self.label_3)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_8.addItem(spacerItem1)
        self.AgeBox = QtWidgets.QLineEdit(self.widget)
        self.AgeBox.setObjectName("AgeBox")
        self.horizontalLayout_8.addWidget(self.AgeBox)
        self.verticalLayout_5.addLayout(self.horizontalLayout_8)
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.label_4 = QtWidgets.QLabel(self.widget)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_9.addWidget(self.label_4)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_9.addItem(spacerItem2)
        self.HeightBox = QtWidgets.QLineEdit(self.widget)
        self.HeightBox.setObjectName("HeightBox")
        self.horizontalLayout_9.addWidget(self.HeightBox)
        self.verticalLayout_5.addLayout(self.horizontalLayout_9)
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.label_5 = QtWidgets.QLabel(self.widget)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_10.addWidget(self.label_5)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_10.addItem(spacerItem3)
        self.WeightBox = QtWidgets.QLineEdit(self.widget)
        self.WeightBox.setObjectName("WeightBox")
        self.horizontalLayout_10.addWidget(self.WeightBox)
        self.verticalLayout_5.addLayout(self.horizontalLayout_10)
        self.tabWidget.addTab(self.patientInfo, "")
        self.measurementsTab = QtWidgets.QWidget()
        self.measurementsTab.setObjectName("measurementsTab")
        self.PrintButton2 = QtWidgets.QPushButton(self.measurementsTab)
        self.PrintButton2.setGeometry(QtCore.QRect(660, 500, 121, 41))
        self.PrintButton2.setObjectName("PrintButton2")
        self.stackedWidget = QtWidgets.QStackedWidget(self.measurementsTab)
        self.stackedWidget.setGeometry(QtCore.QRect(10, 50, 771, 416))
        self.stackedWidget.setObjectName("stackedWidget")
        self.default_measure_page_1 = QtWidgets.QWidget()
        self.default_measure_page_1.setObjectName("default_measure_page_1")
        self.widget1 = QtWidgets.QWidget(self.default_measure_page_1)
        self.widget1.setGeometry(QtCore.QRect(10, 10, 226, 331))
        self.widget1.setObjectName("widget1")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.widget1)
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_17 = QtWidgets.QLabel(self.widget1)
        self.label_17.setObjectName("label_17")
        self.horizontalLayout.addWidget(self.label_17)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem4)
        self.comboBox = QtWidgets.QComboBox(self.widget1)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.horizontalLayout.addWidget(self.comboBox)
        self.verticalLayout_7.addLayout(self.horizontalLayout)
        spacerItem5 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_7.addItem(spacerItem5)
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.measurement_1_label = QtWidgets.QLabel(self.widget1)
        self.measurement_1_label.setObjectName("measurement_1_label")
        self.verticalLayout.addWidget(self.measurement_1_label)
        spacerItem6 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem6)
        self.measurement_1_record_button = QtWidgets.QPushButton(self.widget1)
        self.measurement_1_record_button.setObjectName("measurement_1_record_button")
        self.verticalLayout.addWidget(self.measurement_1_record_button)
        self.horizontalLayout_12.addLayout(self.verticalLayout)
        spacerItem7 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_12.addItem(spacerItem7)
        self.measurement_1_display = QtWidgets.QLCDNumber(self.widget1)
        self.measurement_1_display.setObjectName("measurement_1_display")
        self.horizontalLayout_12.addWidget(self.measurement_1_display)
        self.verticalLayout_7.addLayout(self.horizontalLayout_12)
        spacerItem8 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_7.addItem(spacerItem8)
        self.horizontalLayout_13 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_13.setObjectName("horizontalLayout_13")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.measurement_1_label_2 = QtWidgets.QLabel(self.widget1)
        self.measurement_1_label_2.setObjectName("measurement_1_label_2")
        self.verticalLayout_6.addWidget(self.measurement_1_label_2)
        spacerItem9 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_6.addItem(spacerItem9)
        self.measurement_1_record_button_2 = QtWidgets.QPushButton(self.widget1)
        self.measurement_1_record_button_2.setObjectName("measurement_1_record_button_2")
        self.verticalLayout_6.addWidget(self.measurement_1_record_button_2)
        self.horizontalLayout_13.addLayout(self.verticalLayout_6)
        spacerItem10 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_13.addItem(spacerItem10)
        self.measurement_1_display_2 = QtWidgets.QLCDNumber(self.widget1)
        self.measurement_1_display_2.setObjectName("measurement_1_display_2")
        self.horizontalLayout_13.addWidget(self.measurement_1_display_2)
        self.verticalLayout_7.addLayout(self.horizontalLayout_13)
        self.stackedWidget.addWidget(self.default_measure_page_1)
        self.default_measure_page_2 = QtWidgets.QWidget()
        self.default_measure_page_2.setObjectName("default_measure_page_2")
        self.layoutWidget_4 = QtWidgets.QWidget(self.default_measure_page_2)
        self.layoutWidget_4.setGeometry(QtCore.QRect(10, 10, 226, 331))
        self.layoutWidget_4.setObjectName("layoutWidget_4")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.layoutWidget_4)
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.label_18 = QtWidgets.QLabel(self.layoutWidget_4)
        self.label_18.setObjectName("label_18")
        self.horizontalLayout_11.addWidget(self.label_18)
        spacerItem11 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_11.addItem(spacerItem11)
        self.comboBox_2 = QtWidgets.QComboBox(self.layoutWidget_4)
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.horizontalLayout_11.addWidget(self.comboBox_2)
        self.verticalLayout_8.addLayout(self.horizontalLayout_11)
        spacerItem12 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_8.addItem(spacerItem12)
        self.horizontalLayout_14 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_14.setObjectName("horizontalLayout_14")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout()
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.measurement_1_label_3 = QtWidgets.QLabel(self.layoutWidget_4)
        self.measurement_1_label_3.setObjectName("measurement_1_label_3")
        self.verticalLayout_9.addWidget(self.measurement_1_label_3)
        spacerItem13 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_9.addItem(spacerItem13)
        self.measurement_1_record_button_3 = QtWidgets.QPushButton(self.layoutWidget_4)
        self.measurement_1_record_button_3.setObjectName("measurement_1_record_button_3")
        self.verticalLayout_9.addWidget(self.measurement_1_record_button_3)
        self.horizontalLayout_14.addLayout(self.verticalLayout_9)
        spacerItem14 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_14.addItem(spacerItem14)
        self.measurement_1_display_3 = QtWidgets.QLCDNumber(self.layoutWidget_4)
        self.measurement_1_display_3.setObjectName("measurement_1_display_3")
        self.horizontalLayout_14.addWidget(self.measurement_1_display_3)
        self.verticalLayout_8.addLayout(self.horizontalLayout_14)
        spacerItem15 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_8.addItem(spacerItem15)
        self.horizontalLayout_15 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_15.setObjectName("horizontalLayout_15")
        self.verticalLayout_10 = QtWidgets.QVBoxLayout()
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.measurement_1_label_4 = QtWidgets.QLabel(self.layoutWidget_4)
        self.measurement_1_label_4.setObjectName("measurement_1_label_4")
        self.verticalLayout_10.addWidget(self.measurement_1_label_4)
        spacerItem16 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_10.addItem(spacerItem16)
        self.measurement_1_record_button_4 = QtWidgets.QPushButton(self.layoutWidget_4)
        self.measurement_1_record_button_4.setObjectName("measurement_1_record_button_4")
        self.verticalLayout_10.addWidget(self.measurement_1_record_button_4)
        self.horizontalLayout_15.addLayout(self.verticalLayout_10)
        spacerItem17 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_15.addItem(spacerItem17)
        self.measurement_1_display_4 = QtWidgets.QLCDNumber(self.layoutWidget_4)
        self.measurement_1_display_4.setObjectName("measurement_1_display_4")
        self.horizontalLayout_15.addWidget(self.measurement_1_display_4)
        self.verticalLayout_8.addLayout(self.horizontalLayout_15)
        self.stackedWidget.addWidget(self.default_measure_page_2)
        self.widget2 = QtWidgets.QWidget(self.measurementsTab)
        self.widget2.setGeometry(QtCore.QRect(10, 10, 311, 31))
        self.widget2.setObjectName("widget2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.widget2)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label = QtWidgets.QLabel(self.widget2)
        self.label.setObjectName("label")
        self.horizontalLayout_2.addWidget(self.label)
        self.number_of_areas = QtWidgets.QSpinBox(self.widget2)
        self.number_of_areas.setObjectName("number_of_areas")
        self.horizontalLayout_2.addWidget(self.number_of_areas)
        self.tabWidget.addTab(self.measurementsTab, "")
        self.analysisTab = QtWidgets.QWidget()
        self.analysisTab.setObjectName("analysisTab")
        self.tabWidget.addTab(self.analysisTab, "")
        self.gridLayout.addWidget(self.tabWidget, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        self.stackedWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Algometer Application"))
        self.PrintButton.setText(_translate("MainWindow", "Print Report"))
        self.label_2.setText(_translate("MainWindow", "Name"))
        self.label_3.setText(_translate("MainWindow", "Age"))
        self.label_4.setText(_translate("MainWindow", "Height"))
        self.label_5.setText(_translate("MainWindow", "Weight"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.patientInfo), _translate("MainWindow", "Patient Info"))
        self.PrintButton2.setText(_translate("MainWindow", "Print Report"))
        self.label_17.setText(_translate("MainWindow", "Area: "))
        self.comboBox.setItemText(0, _translate("MainWindow", "Neck"))
        self.comboBox.setItemText(1, _translate("MainWindow", "Shoulder"))
        self.comboBox.setItemText(2, _translate("MainWindow", "Thigh"))
        self.comboBox.setItemText(3, _translate("MainWindow", "Knee"))
        self.comboBox.setItemText(4, _translate("MainWindow", "Additional"))
        self.measurement_1_label.setText(_translate("MainWindow", "Measurement 1"))
        self.measurement_1_record_button.setText(_translate("MainWindow", "Start\n"
"Recording"))
        self.measurement_1_label_2.setText(_translate("MainWindow", "Measurement 2"))
        self.measurement_1_record_button_2.setText(_translate("MainWindow", "Start\n"
"Recording"))
        self.label_18.setText(_translate("MainWindow", "Area: "))
        self.comboBox_2.setItemText(0, _translate("MainWindow", "Neck"))
        self.comboBox_2.setItemText(1, _translate("MainWindow", "Shoulder"))
        self.comboBox_2.setItemText(2, _translate("MainWindow", "Thigh"))
        self.comboBox_2.setItemText(3, _translate("MainWindow", "Knee"))
        self.comboBox_2.setItemText(4, _translate("MainWindow", "Additional"))
        self.measurement_1_label_3.setText(_translate("MainWindow", "Measurement 1"))
        self.measurement_1_record_button_3.setText(_translate("MainWindow", "Start\n"
"Recording"))
        self.measurement_1_label_4.setText(_translate("MainWindow", "Measurement 2"))
        self.measurement_1_record_button_4.setText(_translate("MainWindow", "Start\n"
"Recording"))
        self.label.setText(_translate("MainWindow", "Input number of areas to be measured"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.measurementsTab), _translate("MainWindow", "Measurements"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.analysisTab), _translate("MainWindow", "Analysis"))
