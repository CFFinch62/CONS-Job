
import sys
import os

# Add project root to sys.path to allow imports from consjob package
current_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.dirname(current_dir)
if project_root not in sys.path:
    sys.path.insert(0, project_root)

from PyQt6.QtWidgets import QApplication
from PyQt6.QtGui import QIcon
from consjob.app import MainWindow

def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

def main():
    app = QApplication(sys.argv)
    app.setApplicationName("CONS Job")
    app.setOrganizationName("CONS Job")
    
    # Set Application Icon - try multiple formats for cross-platform support
    icon_formats = ["consjob_icon.png", "consjob_icon.svg", "consjob_icon.ico"]
    for icon_name in icon_formats:
        icon_path = resource_path(os.path.join("images", icon_name))
        if os.path.exists(icon_path):
            app.setWindowIcon(QIcon(icon_path))
            break
    
    window = MainWindow()
    window.show()
    
    sys.exit(app.exec())

if __name__ == "__main__":
    main()
