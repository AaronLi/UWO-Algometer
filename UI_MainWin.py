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
        self.formLayout = QtWidgets.QFormLayout(self.centralwidget)
        self.formLayout.setObjectName("formLayout")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName("tabWidget")
        self.patientInfo = QtWidgets.QWidget()
        self.patientInfo.setObjectName("patientInfo")
        self.layoutWidget = QtWidgets.QWidget(self.patientInfo)
        self.layoutWidget.setGeometry(QtCore.QRect(0, 0, 638, 493))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem1)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.label_2 = QtWidgets.QLabel(self.layoutWidget)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_7.addWidget(self.label_2)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem2)
        self.NameBox = QtWidgets.QLineEdit(self.layoutWidget)
        self.NameBox.setObjectName("NameBox")
        self.horizontalLayout_7.addWidget(self.NameBox)
        self.verticalLayout.addLayout(self.horizontalLayout_7)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem3)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.label_3 = QtWidgets.QLabel(self.layoutWidget)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_8.addWidget(self.label_3)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_8.addItem(spacerItem4)
        self.AgeBox = QtWidgets.QLineEdit(self.layoutWidget)
        self.AgeBox.setObjectName("AgeBox")
        self.horizontalLayout_8.addWidget(self.AgeBox)
        self.verticalLayout.addLayout(self.horizontalLayout_8)
        spacerItem5 = QtWidgets.QSpacerItem(20, 48, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem5)
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.label_4 = QtWidgets.QLabel(self.layoutWidget)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_9.addWidget(self.label_4)
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_9.addItem(spacerItem6)
        self.HeightBox = QtWidgets.QLineEdit(self.layoutWidget)
        self.HeightBox.setObjectName("HeightBox")
        self.horizontalLayout_9.addWidget(self.HeightBox)
        self.verticalLayout.addLayout(self.horizontalLayout_9)
        spacerItem7 = QtWidgets.QSpacerItem(20, 48, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem7)
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.label_5 = QtWidgets.QLabel(self.layoutWidget)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_10.addWidget(self.label_5)
        spacerItem8 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_10.addItem(spacerItem8)
        self.WeightBox = QtWidgets.QLineEdit(self.layoutWidget)
        self.WeightBox.setObjectName("WeightBox")
        self.horizontalLayout_10.addWidget(self.WeightBox)
        self.verticalLayout.addLayout(self.horizontalLayout_10)
        spacerItem9 = QtWidgets.QSpacerItem(20, 48, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem9)
        self.horizontalLayout.addLayout(self.verticalLayout)
        spacerItem10 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem10)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        spacerItem11 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem11)
        self.formLayout_2 = QtWidgets.QFormLayout()
        self.formLayout_2.setObjectName("formLayout_2")
        self.comboBox = QtWidgets.QComboBox(self.layoutWidget)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setItemText(4, "")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.comboBox)
        self.PrintButton_2 = QtWidgets.QPushButton(self.layoutWidget)
        self.PrintButton_2.setObjectName("PrintButton_2")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.PrintButton_2)
        self.verticalLayout_2.addLayout(self.formLayout_2)
        spacerItem12 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem12)
        self.listWidget = QtWidgets.QListWidget(self.layoutWidget)
        self.listWidget.setObjectName("listWidget")
        self.verticalLayout_2.addWidget(self.listWidget)
        spacerItem13 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem13)
        self.PrintButton = QtWidgets.QPushButton(self.layoutWidget)
        self.PrintButton.setObjectName("PrintButton")
        self.verticalLayout_2.addWidget(self.PrintButton)
        spacerItem14 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem14)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        spacerItem15 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem15)
        self.tabWidget.addTab(self.patientInfo, "")
        self.measurementsTab = QtWidgets.QWidget()
        self.measurementsTab.setObjectName("measurementsTab")
        self.tabWidget_2 = QtWidgets.QTabWidget(self.measurementsTab)
        self.tabWidget_2.setGeometry(QtCore.QRect(4, 9, 801, 541))
        self.tabWidget_2.setObjectName("tabWidget_2")
        self.default_tab = QtWidgets.QWidget()
        self.default_tab.setObjectName("default_tab")



        self.widget = QtWidgets.QWidget(self.default_tab)
        self.widget.setGeometry(QtCore.QRect(20, 20, 361, 461))
        self.widget.setObjectName("widget")
        self.gridLayout = QtWidgets.QGridLayout(self.widget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label.setFont(font)
        self.label.setText("Left Side")
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.label_10 = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_10.setFont(font)
        self.label_10.setText("Right Side")
        self.label_10.setObjectName("label_10")
        self.gridLayout.addWidget(self.label_10, 0, 1, 1, 1)
        self.record_left = QtWidgets.QPushButton(self.widget)
        self.record_left.setObjectName("record_left")
        self.gridLayout.addWidget(self.record_left, 1, 0, 1, 1)
        self.record_right = QtWidgets.QPushButton(self.widget)
        self.record_right.setObjectName("record_right")
        self.gridLayout.addWidget(self.record_right, 1, 1, 1, 1)
        self.tableWidget = QtWidgets.QTableWidget(self.widget)
        self.tableWidget.setShowGrid(True)
        self.tableWidget.setWordWrap(False)
        self.tableWidget.setRowCount(10)
        self.tableWidget.setColumnCount(2)
        self.tableWidget.setObjectName("tableWidget")
        self.gridLayout.addWidget(self.tableWidget, 2, 0, 1, 2)
        self.tabWidget_2.addTab(self.default_tab, "")
        self.tabWidget.addTab(self.measurementsTab, "")
        self.analysisTab = QtWidgets.QWidget()
        self.analysisTab.setObjectName("analysisTab")
        self.tabWidget.addTab(self.analysisTab, "")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.SpanningRole, self.tabWidget)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(1)
        self.tabWidget_2.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Algometer Application"))
        self.label_2.setText(_translate("MainWindow", "Name"))
        self.label_3.setText(_translate("MainWindow", "Age"))
        self.label_4.setText(_translate("MainWindow", "Height"))
        self.label_5.setText(_translate("MainWindow", "Weight"))
        self.comboBox.setItemText(0, _translate("MainWindow", "Neck"))
        self.comboBox.setItemText(1, _translate("MainWindow", "Bicep"))
        self.comboBox.setItemText(2, _translate("MainWindow", "Thigh"))
        self.comboBox.setItemText(3, _translate("MainWindow", "Other (No comparative data)"))
        self.PrintButton_2.setText(_translate("MainWindow", "Add Measurement"))
        self.PrintButton.setText(_translate("MainWindow", "Print Report"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.patientInfo), _translate("MainWindow", "Patient Info"))
        self.record_left.setText(_translate("MainWindow", "Start\n"
"Recording"))
        self.record_right.setText(_translate("MainWindow", "Start\n"
"Recording"))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.default_tab), _translate("MainWindow", "Default"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.measurementsTab), _translate("MainWindow", "Measurements"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.analysisTab), _translate("MainWindow", "Analysis"))
