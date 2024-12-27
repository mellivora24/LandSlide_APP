import os
from PyQt5 import QtWidgets
from PyQt5.uic import loadUi
from PyQt5.QtCore import pyqtSignal

class PointBox(QtWidgets.QWidget):
    clicked = pyqtSignal(str)

    def __init__(self, index, ID, data):
        super().__init__()
        self.id = ID

        BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../"))
        self.point_widget = loadUi(os.path.join(BASE_DIR, 'resource', 'point.ui'), self)

        self.point_widget.index.setText("ĐIỂM " + str(index))
        self.point_widget.name.setText(data['name'])

        state = 'Kết nối' if data['is_connecting'] == 'Y' else 'Ngắt kết nối'
        if data['is_connecting'] == 'Y' and int(data['titl_value']) in range(0, 10) and int(data['rain_flow']) in range(0, 300) and int(data['humidity_1']) in range(30, 60) and int(data['humidity_2']) in range(30, 60):
            level = 1
        elif data['is_connecting'] == 'Y' and int(data['titl_value']) in range(10, 20) and int(data['rain_flow']) in range(300, 600) and int(data['humidity_1']) in range(60, 80) and int(data['humidity_2']) in range(60, 80):
            level = 2
        elif data['is_connecting'] == 'Y' and int(data['titl_value']) in range(20, 30) and int(data['rain_flow']) in range(600, 900) and int(data['humidity_1']) in range(80, 100) and int(data['humidity_2']) in range(80, 100):
            level = 3
        elif data['is_connecting'] == 'Y' and int(data['titl_value']) in range(30, 40) and int(data['rain_flow']) in range(900, 1200) and int(data['humidity_1']) in range(100, 120) and int(data['humidity_2']) in range(100, 120):
            level = 4
        else:
            level = 5

        self.point_widget.state.setText(state)
        self.point_widget.level.setText(str(level))
        self.setFixedSize(440, 145)

        self.point_widget.setObjectName("widget")

        # Thiết lập màu sắc theo trạng thái
        if state.lower() in ['kết nối', 'connected']:
            self.point_widget.state.setStyleSheet('color: green')
            border_color = 'green'
        else:
            self.point_widget.state.setStyleSheet('color: red')
            border_color = 'red'

        self.setStyleSheet(f"""
            QWidget#widget {{
                background-color: #f0f0f0;
                border: 2px solid {border_color};
                border-radius: 10px;
                padding: 10px;
            }}
        """)

    def mousePressEvent(self, event):
        """Phát tín hiệu khi widget được nhấp chuột."""
        self.clicked.emit(self.id)
