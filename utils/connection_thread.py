from PySide6.QtCore import QThread, Signal
from model import Config

class ConnectionThread(QThread):
    """
    ConnectionThread thread for connecting to the server.
    Todo For implement
    """
    connected = Signal()
    disconnected = Signal()
    error = Signal(str)

    def __init__(self, config: Config) -> None:
        QThread.__init__(self)
        self.config = config

    def run(self) -> None:
        pass

    def stop(self) -> None:
        pass
