from PyQt6.QtWidgets import QLineEdit

class InputField(QLineEdit):
    def __init__(self):
        super().__init__()
        self.setPlaceholderText("Enter your name")
