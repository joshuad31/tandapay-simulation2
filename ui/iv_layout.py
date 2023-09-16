import sys
from PySide2.QtWidgets import *
from PySide2.QtCore import Qt, QSize

from PySide2.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QLabel, QWidget, QDialog, QTextEdit
from PySide2.QtGui import QFont
from PySide2.QtCore import Qt, QSize

from .ev_layout import EV_Layout
from .pv_layout import PV_Layout
from .ov_layout import OV_Layout

from .ui_element_factory import UI_Element_Factory
from .ui_context import UI_Context

class IV_Layout:
    def __init__(self, ui_context):
        self.uic = ui_context
        self.evl = EV_Layout(self.uic.ev_obj)
        self.pvl = PV_Layout(self.uic.pv_obj)
        self.ovl = OV_Layout(self.uic.ov_obj)

    def get_iv_layout(self) -> QHBoxLayout:
        # add them all to the settings menu layout
        two_column_layout = QHBoxLayout()
        
        # left side
        left_top_layout = self.evl.get_ev_layout()
        left_bottom_layout = self.ovl.get_ov_layout()
        left_combined_layout = QVBoxLayout()
        left_combined_layout.addLayout(left_top_layout)
        left_combined_layout.addLayout(left_bottom_layout)
        
        # right side
        right_layout = self.pvl.get_pv_layout()
        
        # finalize layout
        two_column_layout.addLayout(left_combined_layout)
        two_column_layout.addLayout(right_layout)
        
        return two_column_layout

    def save(self):
        self.uic.ev_obj = self.evl.get_env_vars()
        self.uic.ov_obj = self.ovl.get_other_vars()
        self.uic.pv_obj = self.pvl.get_pricing_vars()
