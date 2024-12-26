import sys
from PyQt5.QtCore import QUrl
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget
from PyQt5.QtWebEngineWidgets import QWebEngineView

class MapWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Nhúng Bản Đồ vào PyQt5")

        # Tạo một QWebEngineView để hiển thị bản đồ
        self.browser = QWebEngineView()

        # Mở bản đồ Google Maps với URL đầy đủ
        self.browser.setUrl(QUrl("https://www.google.com/maps/@21.028511,105.804817,15z"))

        # Thiết lập layout cho cửa sổ chính
        layout = QVBoxLayout()
        layout.addWidget(self.browser)

        # Thiết lập widget chính
        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

if __name__ == '__main__':
    app = QApplication(sys.argv)

    window = MapWindow()
    window.show()

    sys.exit(app.exec_())
