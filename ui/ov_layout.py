import sys

from PySide2.QtWidgets import *
from PySide2.QtCore import Qt, QSize

from PySide2.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QLabel, QWidget, QDialog, QTextEdit
from PySide2.QtGui import QFont
from PySide2.QtCore import Qt, QSize

from ui_element_factory import UI_Element_Factory

class OV_Layout:
    def __init__(self, other_vars, widget_width=None):
        self.ov = other_vars
        self.uief = UI_Element_Factory(widget_width)

        self.ov1_label = "Sample Size"
        self.ov2_label = "Settings Path"

    def get_other_vars(self):
        self.ov.sample_size = self.uief.getValue(self.ov1_label)
        self.ov.settings_path = self.uief.getValue(self.ov2_label)
        return self.ov

    def get_ov_layout(self, settings_import_callback=None):
        layout = QVBoxLayout()

        ov1_hbox = self.uief.make_numeric_entry_element(self.ov1_label, self.ov1_label, 1, 0, 1e9)
        layout.addLayout(ov1_hbox)

        return layout
