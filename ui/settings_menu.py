import sys
from PySide2.QtWidgets import *
from PySide2.QtCore import Qt, QSize

from PySide2.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QLabel, QWidget, QDialog, QTextEdit
from PySide2.QtGui import QFont
from PySide2.QtCore import Qt, QSize

from .stats_layout import Stats_Layout
from .iv_layout import IV_Layout

from .ui_element_factory import UI_Element_Factory
from .ui_context import UI_Context

class Settings_Menu:
    def __init__(self, ui_context, widget_width=None):
        # ui context which will contain information about the objects the settings menu will modify
        self.uic = ui_context
        # make a ui element factory for creating UI elements
        self.uief = UI_Element_Factory(widget_width)
        
        # get layout for initial values:
        self.iv_layout = IV_Layout(self.uic, widget_width)
        self.stats_layout = Stats_Layout(self.uic, widget_width)

    def get_settings_layout(self) -> QHBoxLayout:
        layout = self.iv_layout.get_iv_layout()
        layout.addLayout(self.stats_layout.get_stats_layout())
        return layout

    def get_ok_cancel_layout(self) -> QHBoxLayout:
        ok_cancel_layout = QHBoxLayout()
        ok_cancel_layout.setAlignment(Qt.AlignRight)

        ok_btn = self.uief.make_push_button_element("OK", "Save and close", self.save_and_close)
        cancel_btn = self.uief.make_push_button_element("Cancel", "Close without saving", self.dialog.reject)
        
        ok_cancel_layout.addWidget(cancel_btn)
        ok_cancel_layout.addWidget(ok_btn)

        return ok_cancel_layout

    def open_settings_menu(self):
        self.dialog = QDialog()
        self.dialog.setWindowTitle("Settings Menu")
        
        layout = QVBoxLayout()
        layout.addLayout(self.get_settings_layout())
        layout.addLayout(self.get_ok_cancel_layout()) 

        self.dialog.setLayout(layout)
        self.dialog.exec_()

    def save_and_close(self):
        self.iv_layout.save()
        self.stats_layout.save() 
        self.dialog.accept()

