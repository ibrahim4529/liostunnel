from PySide6.QtWidgets import QWidget, QHBoxLayout, QPushButton, QTabWidget, QVBoxLayout, QTextBrowser, QSizePolicy
from PySide6.QtCore import Qt, Slot
from model import Connection, Config
from utils.logger_text import OutLog
from widget import IconButton, ConfigTab, OptionTab
from paramiko.client import SSHClient
import paramiko

class MainPage(QWidget):
    client = SSHClient()
    def __init__(self, connection: Connection) -> None:
        QWidget.__init__(self)
        self.connection= connection
        self.main_layout = QVBoxLayout()
        self.setLayout(self.main_layout)

        self.load_btn = IconButton("load.ico", "Load Config")
        self.save_btn = IconButton("save.ico","Save config")
        self.save_config_as_btn = IconButton("save-as.ico","Save config as")
        self.btn_login = QPushButton("Login")
        self.btn_exit = QPushButton("Exit")
        self.message_text = QTextBrowser()
        self.message_text.setMinimumHeight(300)

        self.config_tab = ConfigTab()
        self.option_tab = OptionTab()

        self.tab_bar = QTabWidget()

        self.setup_ui()
        self.setup_connections()
    
    def setup_ui(self):
        main_hbox_layout = QHBoxLayout()
        btn_hbox_layout = QHBoxLayout()
        main_vbox_layout = QVBoxLayout()

        btn_vbox = QVBoxLayout()
        btn_vbox.setAlignment(Qt.AlignTop)
        btn_vbox.addWidget(self.load_btn)
        btn_vbox.addWidget(self.save_btn)
        btn_vbox.addWidget(self.save_config_as_btn)


        self.tab_bar.addTab(self.config_tab, "Config")
        self.config_tab.set_config(self.connection.config)
        self.tab_bar.addTab(self.option_tab, "Option")

        main_vbox_layout.addWidget(self.tab_bar)
        main_vbox_layout.addWidget(self.message_text)

        main_hbox_layout.addLayout(btn_vbox)
        main_hbox_layout.addLayout(main_vbox_layout)

        btn_hbox_layout.addWidget(self.btn_login)
        btn_hbox_layout.addWidget(self.btn_exit)
    

        self.main_layout.addLayout(main_hbox_layout)
        self.main_layout.addLayout(btn_hbox_layout)

    def setup_connections(self):
        self.config_tab.config_changed.connect(self.on_config_changed)

        self.load_btn.clicked.connect(self.on_load_config)
        self.save_btn.clicked.connect(self.on_save_config)
        self.save_config_as_btn.clicked.connect(self.on_save_config_as)
        self.btn_login.clicked.connect(self.on_login)
        self.btn_exit.clicked.connect(self.on_exit)
    
    @Slot(Config)
    def on_config_changed(self, config: Config):
        print(config)

    def on_load_config(self):
        pass

    def on_save_config(self):
        pass

    def on_save_config_as(self):
        pass

    def on_login(self):
        config = self.config_tab.get_config()
        try:
            self.client.load_system_host_keys()
            self.client.set_missing_host_key_policy(paramiko.AutoAddPolicy)
            self.client.connect(config.host, config.port, config.username, config.password)
            self.client.get_transport().set_keepalive(30)
            self.message_text.setTextColor(Qt.green)
            self.message_text.setText("Login Success")
        except Exception as err:
            self.message_text.setText(str(err))
            return


    def on_exit(self):
        pass