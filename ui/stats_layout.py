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

from ui.ui_element_factory import UI_Element_Factory
from config_helper import INI_Handler

class Stats_Layout:
    def __init__(self, other_vars, widget_width=None):
        self.ov = other_vars
        self.uief = UI_Element_Factory(widget_width)

        self.ov1_label = "Trial Sample Size"
        self.ov1_tooltip = "Number of simulation runs to use in each trial"

        self.ov2_label = "Trial Count"
        self.ov2_tooltip = "Number of trials to perform (Minimum: 30)"

        self.ov3_label = "Alpha"
        self.ov3_tooltip = "Chance of error you're willing to accept. Example: if you want 95% confidence, select an alpha of 5%"

        self.ov4_label = "Test Type"
        self.ov4_tooltip = "Type of hypothesis test to perform."

        self.ov5_label = "Outcome to test"
        self.ov5_tooltip = "which outcome do you want to test?"

        self.ov6_label = "Value to test"
        self.ov6_tooltip = "which value do you want to test against? (should be a percentage. Accepts decimal values, such as 66.67)"

    def get_stats_vars(self) -> Other_Variables:
        self.ov.trial_sample_size   = self.uief.getValue(self.ov1_label)
        self.ov.trial_count         = self.uief.getValue(self.ov2_label)
        self.ov.alpha               = self.uief.getValue(self.ov3_label) / 100
        self.ov.test_condition      = TestTypeEnum(self.uief.getValue(self.ov4_label))
        self.ov.test_outcome        = OutcomeEnum(self.uief.getValue(self.ov5_label))
        self.ov.value_to_test       = self.uief.getValue(self.ov6_label)
        return self.ov

    def get_stats_layout(self) -> QVBoxLayout:
        layout = QVBoxLayout()

        self.ov1_hbox = self.uief.make_numeric_entry_element(self.ov1_label, self.ov1_tooltip, self.ov.trial_sample_size)
        layout.addLayout(self.ov1_hbox)

        self.ov2_hbox = self.uief.make_numeric_entry_element(self.ov2_label, self.ov2_tooltip, self.ov.trial_count, 30, 2147483647)
        layout.addLayout(self.ov2_hbox)

        self.ov3_hbox = self.uief.make_numeric_entry_element(self.ov3_label, self.ov3_tooltip, self.ov.alpha * 100, 0, 100)
        layout.addLayout(self.ov3_hbox)

        options = [option.name for option in TestTypeEnum]
        self.ov4_hbox = self.uief.make_dropdown_entry_element(self.ov4_label, options, self.ov4_tooltip, self.ov.test_condition.name)
        layout.addLayout(self.ov4_hbox)
        
        options = [option.name for option in OutcomeEnum]
        self.ov5_hbox = self.uief.make_dropdown_entry_element(self.ov5_label, options, self.ov5_tooltip, self.ov.test_outcome.name)
        layout.addLayout(self.ov5_hbox)

        self.ov6_hbox = self.uief.make_float_entry_element(self.ov6_label, self.ov6_tooltip, self.ov.value_to_test, 0.0, 100.0)
        layout.addLayout(self.ov6_hbox)

        return layout
