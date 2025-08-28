from PyQt6.QtWidgets import QWidget, QLabel, QVBoxLayout
from PyQt6.QtCore import Qt
from windowComponents.inputField import InputField
from windowComponents.sendButton import SendButton

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("SVG Button Example")
        self.resize(400, 250)

        # Widgets
        self.label = QLabel("Type your name:")
        self.input_field = InputField()
        self.output_label = QLabel("")

        # Button from component
        self.button = SendButton(self.say_welcome)

        # Layout
        layout = QVBoxLayout()
        layout.setSpacing(15)
        layout.addWidget(self.label, alignment=Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(self.input_field, alignment=Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(self.button, alignment=Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(self.output_label, alignment=Qt.AlignmentFlag.AlignCenter)

        self.setLayout(layout)

    def say_welcome(self):
        name = self.input_field.text().strip()
        if name:
            self.output_label.setText(f"Welcome {name}")
        else:
            self.output_label.setText("Please type your name!")
