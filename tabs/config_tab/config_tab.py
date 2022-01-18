from typing import Type

import serial
from PyQt5.QtCore import QCoreApplication
from PyQt5.QtWidgets import QWidget, QFormLayout, QComboBox, QPushButton, QStackedWidget

from algometer import algometer
from algometer.development_testing import algometer_development_testing
from algometer.wagnerfpx import algometer_wagnerfpx
from algometer.algometer_builder import AlgometerBuilder
from tabs.config_tab.serial_port_list import SerialPortList
import algometer_data


class ConfigTab(QWidget):
    SUPPORTED_ALGOMETERS = [
        algometer_development_testing.DevelopmentAlgometer,
        algometer_wagnerfpx.AlgometerWagnerFPX
    ]
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.config_layout = QFormLayout()

        self.algometer_type_choice = QComboBox()
        self.algometer_type_choice.addItems([a.get_display_name() for a in self.SUPPORTED_ALGOMETERS])
        self.config_layout.addRow("Algometer type", self.algometer_type_choice)
        self.algometer_type_choice.currentIndexChanged.connect(self.on_algometer_type_changed)

        self.algometer_widget_map = {}
        self.algometer_requirements = QStackedWidget()
        for algometer_type in self.SUPPORTED_ALGOMETERS:
            self.algometer_widget_map[algometer_type] = self.get_algometer_requirements_ui(algometer_type)
            self.algometer_requirements.addWidget(self.algometer_widget_map[algometer_type])
        self.config_layout.addRow("Config", self.algometer_requirements)

        self.connect_button = QPushButton("Connect")
        self.connect_button.clicked.connect(self.on_connect_button_clicked)
        self.config_layout.addRow(self.connect_button)
        self.setLayout(self.config_layout)


        self.retranslateUi()

    def get_current_algometer_type(self) -> Type[algometer.Algometer]:
        return self.SUPPORTED_ALGOMETERS[self.algometer_type_choice.currentIndex()]

    def on_algometer_type_changed(self, _index):
        self.algometer_requirements.setCurrentWidget(self.algometer_widget_map[self.get_current_algometer_type()])

    def on_connect_button_clicked(self):
        if algometer_data.algometer is None:
            algometer_type = self.get_current_algometer_type()
            algometer_parameters = self.algometer_requirements.currentWidget()
            builder = AlgometerBuilder()
            algometer_data.algometer = builder.build(algometer_type, algometer_parameters)
            self.connect_button.setText(QCoreApplication.translate("MainWindow", "Disconnect"))
            self.algometer_type_choice.setEnabled(False)
            self.algometer_requirements.setEnabled(False)
        else:
            algometer_data.algometer.disconnect()
            algometer_data.algometer = None
            self.connect_button.setText(QCoreApplication.translate("MainWindow", "Connect"))
            self.algometer_type_choice.setEnabled(True)
            self.algometer_requirements.setEnabled(True)


    def get_algometer_requirements_ui(self, algometer: Type[algometer.Algometer]) -> QWidget:
        containerWidget = QWidget()
        requirements = QFormLayout()

        for requirement in algometer.get_device_requirements():
            if requirement == serial.Serial:
                # Device requires a serial port
                serial_port_config = SerialPortList()
                serial_port_config.setObjectName("serial_port_config")
                requirements.addRow("Serial Port:", serial_port_config)
        containerWidget.setLayout(requirements)
        return containerWidget

    def retranslateUi(self):
        pass

