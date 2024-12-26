from random import random
from PyQt5.QtCore import QUrl
from PyQt5.uic import loadUi
from components.point_box import PointBox
from PyQt5.QtWidgets import QVBoxLayout, QMainWindow
from PyQt5.QtWebEngineWidgets import QWebEngineView
from src.app.controller import event_listener

class GUI(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setFixedSize(1280, 720)
        self.setWindowTitle('Land Slide Desktop App')
        self.main_ui = loadUi('E:/EarnMoney/KHKT/LandSlideSystem/LandSlide_APP/src/resource/main.ui', self)

        self.point_layout = QVBoxLayout(self.main_ui.point_list)
        self.map_layout = QVBoxLayout(self.main_ui.point_view)

        for i in range(0, 4):
            point = PointBox("adasd21312", i, 'Xã ' + str(i), 'Hoạt động' if random() > 0.5 else 'Ngắt kết nối', i)
            point.clicked.connect(lambda point_id=point.id: event_listener.on_point_box_clicked(point_id))
            self.point_layout.addWidget(point)

        self.browser = QWebEngineView()
        self.browser.setUrl(QUrl("https://www.google.com/maps/@21.028511,105.804817,15z"))
        self.main_ui.map_layout.addWidget(self.browser)

if __name__ == '__main__':
    import sys
    from PyQt5.QtWidgets import QApplication
    app = QApplication(sys.argv)
    gui = GUI()
    gui.show()
    sys.exit(app.exec_())

