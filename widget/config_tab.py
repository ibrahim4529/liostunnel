from PySide6.QtWidgets import QWidget, QLineEdit, QGridLayout, QGroupBox, QLabel, QFormLayout, QCheckBox, QSizePolicy
from PySide6.QtCore import Signal
from model import Config

class ConfigTab(QWidget):
    """
    ConfigTab tab for configuring the connection information.
    config_changed: Signal(Config) signal emitted when field changed.
    """
    config_changed = Signal(Config)

    def __init__(self) -> None:
        QWidget.__init__(self)

        self.username_text_edit = QLineEdit()
        self.password_text_edit = QLineEdit()
        self.host_text_edit = QLineEdit()
        self.port_text_edit = QLineEdit()
        self.is_using_proxy_check_box = QCheckBox()
        self.proxy_host_text_edit = QLineEdit()
        self.proxy_port_text_edit = QLineEdit()

        self.setup_ui()
        self.setup_connections()
    
    def setup_ui(self):
        main_layout = QGridLayout()

        group_server = QGroupBox("Auth Information")
        group_server.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        group_server_layout = QFormLayout()
        group_server_layout.setFieldGrowthPolicy(QFormLayout.ExpandingFieldsGrow)
        group_server.setLayout(group_server_layout)
        group_server_layout.addRow(QLabel("Username :"), self.username_text_edit)
        group_server_layout.addRow(QLabel("Password :"), self.password_text_edit)
        main_layout.addWidget(group_server, 0, 0)
        main_layout.setRowStretch(0, 0)

        group_client = QGroupBox("Client Information")
        group_client_layout = QFormLayout()

        group_client.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        group_client_layout.setFieldGrowthPolicy(QFormLayout.ExpandingFieldsGrow)
        group_client.setLayout(group_client_layout)
        group_client_layout.addRow(QLabel("Host :"), self.host_text_edit)
        group_client_layout.addRow(QLabel("Port :"), self.port_text_edit)
        main_layout.addWidget(group_client, 0, 1)
        main_layout.setRowStretch(1, 0)

        group_proxy = QGroupBox("Proxy Information")
        group_proxy.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        group_proxy_layout = QFormLayout()
        group_proxy_layout.setFieldGrowthPolicy(QFormLayout.AllNonFixedFieldsGrow)
        group_proxy.setAutoFillBackground(False)
        group_proxy.setLayout(group_proxy_layout)
        group_proxy_layout.addRow(QLabel("Is Using Proxy :"), self.is_using_proxy_check_box)
        group_proxy_layout.addRow(QLabel("Proxy Host :"), self.proxy_host_text_edit)
        group_proxy_layout.addRow(QLabel("Proxy Port :"), self.proxy_port_text_edit)
        main_layout.addWidget(group_proxy, 1, 0)

        self.setLayout(main_layout)
    
    def setup_connections(self):
        self.username_text_edit.editingFinished.connect(self.on_config_field_changed)
        self.password_text_edit.editingFinished.connect(self.on_config_field_changed)
        self.host_text_edit.editingFinished.connect(self.on_config_field_changed)
        self.port_text_edit.editingFinished.connect(self.on_config_field_changed)
        self.is_using_proxy_check_box.stateChanged.connect(self.on_config_field_changed)
        self.proxy_host_text_edit.editingFinished.connect(self.on_config_field_changed)
        self.proxy_port_text_edit.editingFinished.connect(self.on_config_field_changed)
    
    def on_config_field_changed(self):
        self.config_changed.emit(self.get_config())
    
    def get_config(self) -> Config:
        return Config(
            username=self.username_text_edit.text(),
            password=self.password_text_edit.text(),
            host=self.host_text_edit.text(),
            port=int(self.port_text_edit.text()),
            is_using_proxy=self.is_using_proxy_check_box.isChecked(),
            proxy_host=self.proxy_host_text_edit.text(),
            proxy_port=self.proxy_port_text_edit.text()
        )
    
    def set_config(self, config: Config):
        self.username_text_edit.setText(config.username)
        self.password_text_edit.setText(config.password)
        self.host_text_edit.setText(config.host)
        self.port_text_edit.setText(str(config.port))
        self.is_using_proxy_check_box.setChecked(config.is_using_proxy)
        self.proxy_host_text_edit.setText(config.proxy_host)
        self.proxy_port_text_edit.setText(str(config.proxy_port))