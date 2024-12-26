from PyQt5.QtCore import pyqtSignal
from PyQt5 import QtWidgets
from PyQt5.uic import loadUi

class PointBox(QtWidgets.QWidget):
    clicked = pyqtSignal(str)

    def __init__(self, id, index, name, state, level):
        super().__init__()
        self.id = id
        self.point_widget = loadUi('E:/EarnMoney/KHKT/LandSlideSystem/LandSlide_APP/src/resource/point.ui', self)

        self.point_widget.index.setText("ĐIỂM " + str(index))
        self.point_widget.name.setText(name)
        self.point_widget.state.setText(state)
        self.point_widget.level.setText(str(level))
        self.setFixedSize(440, 145)

        self.point_widget.setObjectName("widget")

        # Thiết lập màu sắc theo trạng thái
        if state.lower() in ['hoạt động', 'activate']:
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
