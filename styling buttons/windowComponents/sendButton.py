from PyQt6.QtWidgets import QPushButton
from PyQt6.QtGui import QIcon
from PyQt6.QtCore import QSize, Qt
import config

class SendButton(QPushButton):
    def __init__(self, on_click_callback):
        super().__init__("Send")   # <-- button text here

        # Load SVG icon
        icon = QIcon(config.SEND_ICON)
        self.setIcon(icon)
        self.setIconSize(QSize(24, 24))

        # Adjust button size
        self.setFixedHeight(50)

        # Put icon to the left of the text
        self.setLayoutDirection(Qt.LayoutDirection.LeftToRight)

        # Connect action
        self.clicked.connect(on_click_callback)
