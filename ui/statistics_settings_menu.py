import sys
from PySide2.QtWidgets import *
from PySide2.QtCore import Qt, QSize

from PySide2.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QLabel, QWidget, QDialog, QTextEdit
from PySide2.QtGui import QFont
from PySide2.QtCore import Qt, QSize

sys.path.append('../')
from environment_variables import *
from pricing_variables import *
from other_variables import *

from ui.ev_layout import EV_Layout
from ui.pv_layout import PV_Layout
from ui.ov_layout import OV_Layout
from ui.stats_layout import Stats_Layout

from ui.ui_element_factory import UI_Element_Factory
from config_helper import INI_Handler


class StatisticsSettings:
    def __init__(self, other_vars, ini_handler=None, widget_width=None):
        self.ov = other_vars
        self.widget_width = widget_width
        self.ini_handler = ini_handler
        self.dialog = None
        
        self.sl = Stats_Layout(self.ov, self.widget_width)

        self.uief = UI_Element_Factory(self.widget_width)

    def get_statistics_dialog(self) -> QDialog:
        self.dialog = QDialog()
        self.dialog.setWindowTitle("Statistics")

        layout = self.sl.get_stats_layout()

        self.dialog.setLayout(layout)
        return self.dialog

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ini_handler = INI_Handler("testconfig/settings.ini")
    ov = ini_handler.read_other_variables()

    test_stats = StatisticsSettings(ov, ini_handler)

    dialog = test_stats.get_statistics_dialog()
    dialog.finished.connect(app.quit)

    dialog.exec_()
