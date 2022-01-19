from typing import Optional

import serial
from PyQt5.QtWidgets import QWidget

from algometer.wagnerfpx.algometer_wagnerfpx import AlgometerWagnerFPX
from tabs.config_tab.serial_port_list import SerialPortList


class WagnerFPXBuilder:
    def __init__(self):
        pass

    def build(self, data: QWidget) -> AlgometerWagnerFPX:
        serial_port_selection: SerialPortList = data.findChild(QWidget, "serial_port_config")
        if not serial_port_selection.is_port_selected():
            raise ValueError("No serial port selected")

        serial_port = serial_port_selection.get_selected_port()
        return AlgometerWagnerFPX(serial.Serial(serial_port, 9600, timeout=3))