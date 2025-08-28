import sys
import time
from PyQt6.QtWidgets import QApplication
from mainWindow.mainWindow import MainWindow
import config

def load_stylesheet(app, path=config.STYLE_QSS):
    try:
        with open(path, "r") as f:
            app.setStyleSheet(f.read())
    except FileNotFoundError:
        print(f"⚠️ Could not find style file at {path}")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    load_stylesheet(app)

    # small delay before showing window
    time.sleep(0.2)

    window = MainWindow()
    window.show()
    sys.exit(app.exec())
