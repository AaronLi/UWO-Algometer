from typing import Optional

import serial
from PyQt5.QtWidgets import QWidget

from algometer.development_testing.algometer_bt_test import BTDevAlgometer
from tabs.config_tab.serial_port_list import SerialPortList


class BTDevAlgometerBuilder:
    def __init__(self):
        pass

    def build(self, data: QWidget) -> BTDevAlgometer:
        serial_port_selection: SerialPortList = data.findChild(QWidget, "serial_port_config")
        if not serial_port_selection.is_port_selected():
            raise ValueError("No serial port selected")

        serial_port = serial_port_selection.get_selected_port()
        return BTDevAlgometer(serial.Serial(serial_port, 115200, timeout=0.1))