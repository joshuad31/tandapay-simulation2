import sys

from PySide2.QtWidgets import QApplication
from .main_menu import Main_Menu

from .ui_context import UI_Context

def initialize(ui_context):
    app = QApplication(sys.argv)
    main_menu = Main_Menu(ui_context)
    main_menu.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    initialize(UI_Context())
