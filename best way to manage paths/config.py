import os
import importlib.util

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Database paths
DB_DIR = os.path.join(BASE_DIR, "databases", "persons")
DB_PATH = os.path.join(DB_DIR, "persons.db")
os.makedirs(DB_DIR, exist_ok=True)

# Assets + Components paths
STYLE_PATH = os.path.join(BASE_DIR, "assets", "generalStyle.py")
INPUT_COMPONENT_PATH = os.path.join(BASE_DIR, "windowComponents", "inputComponent.py")
TABLE_COMPONENT_PATH = os.path.join(BASE_DIR, "windowComponents", "tableComponent.py")

def load_style():
    spec = importlib.util.spec_from_file_location("generalStyle", STYLE_PATH)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module.STYLE

def load_component(path, module_name):
    spec = importlib.util.spec_from_file_location(module_name, path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module
