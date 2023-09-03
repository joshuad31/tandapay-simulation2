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

class SettingsDialog:
    def __init__(self, env_vars, pricing_vars, other_vars, widget_width=None):
        self.ev = env_vars
        self.pv = pricing_vars
        self.ov = other_vars
        self.widget_width = widget_width
        
        self.uief = UI_Element_Factory(widget_width)

    def get_two_column_layout(self) -> QHBoxLayout:
        # will store the two columns with all of our options
        two_column_layout = QHBoxLayout()

        # environment variables settings, which will take up left side of the settings menu
        evl = EV_Layout(self.ev, self.widget_width)
        left_layout = evl.get_ev_layout()

        # pv and ov settings will share the right side, with pv top and ov bottom
        pvl = PV_Layout(self.pv, self.widget_width)
        right_top_layout = pvl.get_pv_layout()

        ovl = OV_Layout(self.ov, self.widget_width)
        right_bottom_layout = ovl.get_ov_layout()
       
        # add the layouts to widgets
        right_top_widget = QWidget()
        right_top_widget.setLayout(right_top_layout)
        right_bottom_widget = QWidget()
        right_bottom_widget.setLayout(right_bottom_layout)
        
        # add the right widgets to a splitter, since they will share the right half:
        right_side_splitter = QSplitter(Qt.Vertical)
        right_side_splitter.addWidget(right_top_widget)
        right_side_splitter.addWidget(right_bottom_widget)

        # combine the right side into one cohesive layout:
        right_layout = QVBoxLayout()
        right_layout.addWidget(right_side_splitter)

        # add the left and right columns to the two column layout
        two_column_layout.addLayout(left_layout)
        two_column_layout.addLayout(right_layout)

        return two_column_layout

    def get_ok_cancel_buttons(self) -> QHBoxLayout:
        ok_cancel_layout = QHBoxLayout()
        ok_cancel_layout.setDirection(QHBoxLayout.RightToLeft)
        
        ok_btn = self.uief.make_push_button_element("OK", "Save and close")
        cancel_btn = self.uief.make_push_button_element("Cancel", "Close without saving")
        
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
        ok_cancel = self.get_ok_cancel_buttons()
        main_layout.addLayout(ok_cancel)

        settings_widget.setLayout(main_layout)
        return settings_widget
        


if __name__ == "__main__":
    app = QApplication(sys.argv)
    test_settings = SettingsDialog(Environment_Variables(), Pricing_Variables(), Other_Variables())
    
    dialog = QDialog()
    dialog.setWindowTitle("Settings Dialog")

    layout = QVBoxLayout()
    layout.addWidget(test_settings.get_settings_widget())

    dialog.setLayout(layout)
    dialog.finished.connect(app.quit)

    dialog.exec_()

