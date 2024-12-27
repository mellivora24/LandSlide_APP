import os
import sys
from PyQt5.uic import loadUi
from PyQt5.QtCore import QUrl
from services import firebase
from components.point_box import PointBox
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtWidgets import QVBoxLayout, QMainWindow, QApplication

class GUI(QMainWindow):
    def __init__(self):
        super().__init__()
        self.browser = None
        self.setFixedSize(1280, 720)
        self.setWindowTitle('Land Slide Desktop App')

        BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../"))
        self.main_ui = loadUi(os.path.join(BASE_DIR, 'src', 'resource', 'main.ui'), self)

        self.points = firebase.get_all_documents()
        self.render_points()

        self.browser = QWebEngineView()
        self.browser.setUrl(QUrl('https://www.google.com/maps/'))
        self.main_ui.map_layout.addWidget(self.browser)

    def render_points(self):
        self.point_layout = QVBoxLayout(self.main_ui.point_list)
        self.map_layout = QVBoxLayout(self.main_ui.point_view)

        for index, (ID, data) in enumerate(self.points.items()):
            point = PointBox(index + 1, ID, data)
            point.clicked.connect(lambda ID: self.show_point(ID))
            self.point_layout.addWidget(point)

    def show_point(self, ID):
        try:
            point = firebase.get_document_by_id(ID)
            lat = point['lat']
            lng = point['long']
            self.browser.setUrl(QUrl(f'https://www.google.com/maps/@{lat},{lng},17z'))

            self.show_point_detail(point)
        except Exception as e:
            print(e)

    def show_point_detail(self, data):
        self.main_ui.location_name.setText(f"kinh độ: {data['long']}, vĩ độ: {data['lat']}")
        self.main_ui.rain_flow_value.setText(data['rain_flow'])
        self.main_ui.tilt_value.setText(data['titl_value'])
        self.main_ui.humidity_1.setText(data['humidity_1'])
        self.main_ui.humidity_2.setText(data['humidity_2'])

        if data['is_connecting'] == 'Y' and int(data['titl_value']) in range(0, 10) and int(data['rain_flow']) in range(0, 300) and int(data['humidity_1']) in range(30, 60) and int(data['humidity_2']) in range(30, 60):
            self.main_ui.warning_level.setText('1')
        elif data['is_connecting'] == 'Y' and int(data['titl_value']) in range(10, 20) and int(data['rain_flow']) in range(300, 600) and int(data['humidity_1']) in range(60, 80) and int(data['humidity_2']) in range(60, 80):
            self.main_ui.warning_level.setText('2')
        elif data['is_connecting'] == 'Y' and int(data['titl_value']) in range(20, 30) and int(data['rain_flow']) in range(600, 900) and int(data['humidity_1']) in range(80, 100) and int(data['humidity_2']) in range(80, 100):
            self.main_ui.warning_level.setText('3')
        elif data['is_connecting'] == 'Y' and int(data['titl_value']) in range(30, 40) and int(data['rain_flow']) in range(900, 1200) and int(data['humidity_1']) in range(100, 120) and int(data['humidity_2']) in range(100, 120):
            self.main_ui.warning_level.setText('4')
        else:
            self.main_ui.warning_level.setText('5')

        if int(data['rain_flow']) > 0:
            self.main_ui.rain_state.setText('Có mưa')
        else:
            self.main_ui.rain_state.setText('Không mưa')


    def closeEvent(self, event):
        firebase.close_connection()
        event.accept()

if __name__ == '__main__':
    try:
        app = QApplication(sys.argv)
        gui = GUI()
        gui.show()
        sys.exit(app.exec_())
    except Exception as e:
        print(e)
