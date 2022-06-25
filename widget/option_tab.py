from PySide6.QtWidgets import QWidget, QTextEdit, QGridLayout, QGroupBox, QLabel, QFormLayout
from PySide6.QtCore import Signal

class OptionTab(QWidget):
    """
    ConfigTab tab for configuring the connection information.
    username_changed: Signal(str) signal emitted when username changed
    password_changed: Signal(str) signal emitted when password changed
    host_changed: Signal(str) signal emitted when host changed
    port_changed: Signal(str) signal emitted when port changed
    """
    username_changed = Signal(str)
    password_changed = Signal(str)
    host_changed = Signal(str)
    port_changed = Signal(str)

    def __init__(self) -> None:
        QWidget.__init__(self)

        self.username_text_edit = QTextEdit()
        self.password_text_edit = QTextEdit()
        self.host_text_edit = QTextEdit()
        self.port_text_edit = QTextEdit()

        self.setup_ui()
        self.setup_connections()
    
    def setup_ui(self):
        main_layout = QGridLayout()

        group_server = QGroupBox("Auth Information")
        group_server_layout = QFormLayout()
        group_server.setLayout(group_server_layout)
        group_server_layout.addRow(QLabel("Username :"), self.username_text_edit)
        group_server_layout.addRow(QLabel("Password :"), self.password_text_edit)
        main_layout.addWidget(group_server, 0, 0)

        group_client = QGroupBox("Client Information")
        group_client_layout = QFormLayout()
        group_client.setLayout(group_client_layout)
        group_client_layout.addRow(QLabel("Host :"), self.host_text_edit)
        group_client_layout.addRow(QLabel("Port :"), self.port_text_edit)
        main_layout.addWidget(group_client, 0, 1)
        self.setLayout(main_layout)
    
    def setup_connections(self):
        # self.username_text_edit.text_changed.connect(self.username_changed.emit)
        # self.password_text_edit.textChanged.connect(self.password_changed.emit)
        # self.host_text_edit.textChanged.connect(self.host_changed.emit)
        # self.port_text_edit.textChanged.connect(self.port_changed.emit)
        pass
        