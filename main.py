from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton
from PySide6.QtGui import QCloseEvent
from liostunnel_resource import qInitResources
from model import Connection, Config
from page.main_page import MainPage


class MainWindow(QMainWindow):
    def __init__(self) -> None:
        QMainWindow.__init__(self)
        self.setWindowTitle("LIOSTUNEL")

        connection = Connection(
            config=Config(),
            is_connected=False
        )
        self.btn_start = QPushButton("Start")
        self.main_page = MainPage(connection=connection)
        qInitResources()
        self.setCentralWidget(self.main_page)
        

    def handle_start_btn(self):
        pass

    def closeEvent(self, event: QCloseEvent) -> None:
        event.accept()

if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec()
