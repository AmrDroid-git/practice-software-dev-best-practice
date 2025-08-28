import os

PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))

ASSETS_DIR = os.path.join(PROJECT_ROOT, "assets")

STYLE_DIR = os.path.join(ASSETS_DIR, "styles")
BUTTONS_DIR = os.path.join(ASSETS_DIR, "buttons")

STYLE_QSS = os.path.normpath(os.path.join(STYLE_DIR, "style.qss"))
SEND_ICON = os.path.normpath(os.path.join(BUTTONS_DIR, "send.svg"))
