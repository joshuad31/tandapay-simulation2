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

from ev_layout import EV_Layout
from pv_layout import PV_Layout
from ov_layout import OV_Layout

from ui_element_factory import UI_Element_Factory
from config_helper import INI_Handler

class SettingsDialog:
    def __init__(self, env_vars, pricing_vars, other_vars, ini_handler=None, widget_width=None):
        self.ev = env_vars
        self.pv = pricing_vars
        self.ov = other_vars
        self.widget_width = widget_width
        self.ini_handler = ini_handler
        self.dialog = None

        self.pvl = PV_Layout(self.pv, self.widget_width)
        self.evl = EV_Layout(self.ev, self.widget_width)
        self.ovl = OV_Layout(self.ov, self.widget_width)

        self.uief = UI_Element_Factory(widget_width)

    def get_two_column_layout(self) -> QHBoxLayout:
        # will store the two columns with all of our options
        two_column_layout = QHBoxLayout()

        # pricing variables settings, which will take up right side of the settings menu
        right_layout = self.pvl.get_pv_layout()

        # ev and ov settings will share the left side, with pv top and ov bottom
        left_top_layout = self.evl.get_ev_layout()
        left_bottom_layout = self.ovl.get_ov_layout()
       
        # add the layouts to widgets
        left_top_widget = QWidget()
        left_top_widget.setLayout(left_top_layout)
        left_bottom_widget = QWidget()
        left_bottom_widget.setLayout(left_bottom_layout)
        
        # add the left widgets to a splitter, since they will share the left half:
        left_side_splitter = QSplitter(Qt.Vertical)
        left_side_splitter.addWidget(left_top_widget)
        left_side_splitter.addWidget(left_bottom_widget)

        # combine the left side into one cohesive layout:
        left_layout = QVBoxLayout()
        left_layout.addWidget(left_side_splitter)

        # add the right and left columns to the two column layout
        two_column_layout.addLayout(left_layout)
        two_column_layout.addLayout(right_layout)

        return two_column_layout

    def get_ok_cancel_buttons(self) -> QHBoxLayout:
        ok_cancel_layout = QHBoxLayout()
        ok_cancel_layout.setDirection(QHBoxLayout.RightToLeft)
        
        ok_btn = self.uief.make_push_button_element("OK", "Save and close", self.save_and_close)
        cancel_btn = self.uief.make_push_button_element("Cancel", "Close without saving", self.dialog.reject)
        
        ok_cancel_layout.addWidget(ok_btn)
        ok_cancel_layout.addWidget(cancel_btn)

        return ok_cancel_layout

    def get_settings_widget(self) -> QWidget: 
        settings_widget = QWidget()
        
        # will store the settings menu as a whole, including the
        # two column layout, but also the OK/Cancel buttons below it
        main_layout = QVBoxLayout()
        
        # contains the settings for all of the EVs, PVs, and OVs
        two_column_layout = self.get_two_column_layout()
        
        # add two column layout to the main layout
        main_layout.addLayout(two_column_layout)
        
        # add the ok and cancel buttons to the bottom
        if self.dialog is not None:
            ok_cancel = self.get_ok_cancel_buttons()
            main_layout.addLayout(ok_cancel)

        settings_widget.setLayout(main_layout)
        return settings_widget

    def save_and_close(self):
        self.ev = self.evl.get_env_vars()      
        self.ov = self.ovl.get_other_vars()
        self.pv = self.pvl.get_pricing_vars()

        if self.ini_handler is not None:
            self.ini_handler.write_pricing_variables(self.pv)
            self.ini_handler.write_environment_variables(self.ev)

        if self.dialog is not None:
            self.dialog.accept()
        
    def get_settings_dialog(self) -> QDialog:
        self.dialog = QDialog()
        self.dialog.setWindowTitle("Settings Dialog")
        
        layout = QVBoxLayout()
        layout.addWidget(self.get_settings_widget())

        self.dialog.setLayout(layout)
        return self.dialog

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ini_handler = INI_Handler("testconfig/settings.ini")
    ev = ini_handler.read_environment_variables()
    pv = ini_handler.read_pricing_variables()

    test_settings = SettingsDialog(ev, pv, Other_Variables(), ini_handler)
    
    dialog = test_settings.get_settings_dialog()
    dialog.finished.connect(app.quit)

    dialog.exec_()

