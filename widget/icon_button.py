from PySide6.QtWidgets import QPushButton
from PySide6.QtGui import QIcon
from PySide6.QtCore import QSize

class IconButton(QPushButton):
    def __init__(self, icon: str, text: str):
        QPushButton.__init__(self, text=text)
        self.setIcon(QIcon(":/images/" + icon))
        self.setIconSize(QSize(32, 32))