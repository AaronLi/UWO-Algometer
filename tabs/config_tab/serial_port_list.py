from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QHBoxLayout, QComboBox, QPushButton
from serial.tools import list_ports


class SerialPortList(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.layout = QHBoxLayout()

        self.options = QComboBox()
        self.layout.addWidget(self.options)

        refresh_button = QPushButton("Refresh")
        refresh_button.clicked.connect(self.refresh)
        self.layout.addWidget(refresh_button)
        self.setLayout(self.layout)
        self.refresh()

    def refresh(self):
        self.options.clear()
        for port in list_ports.comports():
            self.options.addItem(port.description, port.name)

    def is_port_selected(self):
        return self.options.currentText() != ""

    def get_selected_port(self):
        return self.options.currentData(Qt.UserRole)