import sys

from PySide2.QtWidgets import *
from PySide2.QtCore import Qt, QSize

from PySide2.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QLabel, QWidget, QDialog, QTextEdit
from PySide2.QtGui import QFont
from PySide2.QtCore import Qt, QSize

from PySide2.QtWidgets import QVBoxLayout, QSpinBox, QLabel, QHBoxLayout, QComboBox, QLineEdit
from PySide2.QtCore import Qt

from ui.ui_element_factory import UI_Element_Factory

class EV_Layout:
    def __init__(self, env_vars, widget_width=None):
        self.env_vars = env_vars
        self.uief = UI_Element_Factory(widget_width) 

        self.ev_label = "Environment Variables"

        self.ev1_label = "EV1: Total Member Count"
        self.ev1_tooltip = "How many members are initially in the simulation?"
        
        self.ev2_label = "EV2: Monthly Premium"
        self.ev2_tooltip = "What is the initial monthly premium?"
        
        self.ev3_label = "EV3: Chance of Claim"
        self.ev3_tooltip = "What is the chance of a claim each month?"

        self.ev4_label = "EV4: Percent Honest Defectors"
        self.ev4_tooltip = "What percentage of users are honest defectors?"

        self.ev5_label = "EV5: Percent Low Morale"
        self.ev5_tooltip = "What percentage of users are low morale?"

        self.ev6_label = "EV6: Percent Independent"
        self.ev6_tooltip = "What percentage of users are independent?"

        self.ev7_label = "EV7: Dependent Threshold"
        self.ev7_tooltip = "What is the member threshold needed for dependent members to defect? (allowed values: 2, 3)"

        self.ev9_label = "EV9: Low Morale Quit Probability"
        self.ev9_tooltip = "Probability a low-morale member will quit if forced to reorg (Must be 1/3)"
        
        self.ev10_label = "EV10: Coverage Requirement"
        self.ev10_tooltip = "Coverage Requirement. Equal to EV1 * EV2. Is the total value of the claim which the members must pay"
        
        self.ev11_label = "EV11: Queuing"
        self.ev11_tooltip = "Number of periods to do queuing for. Queuing delays repayments"

        self.ev12_label = "EV12: Periods"
        self.ev12_tooltip = "Maximum number of periods the simulation will run for"

    def get_env_vars(self):
        self.env_vars.total_member_cnt = self.uief.getValue(self.ev1_label)
        self.env_vars.monthly_premium = self.uief.getValue(self.ev2_label)
        self.env_vars.chance_of_claim = self.uief.getValue(self.ev3_label) / 100
        self.env_vars.perc_honest_defectors = self.uief.getValue(self.ev4_label) / 100
        self.env_vars.perc_low_morale = self.uief.getValue(self.ev5_label) / 100
        self.env_vars.perc_independent = self.uief.getValue(self.ev6_label) / 100
        self.env_vars.dependent_thres = int(self.uief.getValue(self.ev7_label))
        self.env_vars.queueing = self.uief.getValue(self.ev11_label)
        return self.env_vars

    def get_ev_layout(self) -> QVBoxLayout:
        layout = QVBoxLayout()

        header = QLabel("Environment Variables")
        header_font = QFont()
        header_font.setBold(True)
        header_font.setPointSize(14)
        header.setFont(header_font)
        header.setAlignment(Qt.AlignCenter)
        layout.addWidget(header)

        # ev1
        ev1_hbox = self.uief.make_numeric_entry_element(self.ev1_label, self.ev1_tooltip, self.env_vars.total_member_cnt, 0, 1e9)
        layout.addLayout(ev1_hbox)
        
        # ev2
        ev2_hbox = self.uief.make_numeric_entry_element(self.ev2_label, self.ev2_tooltip, self.env_vars.monthly_premium, 0, 1e9)
        layout.addLayout(ev2_hbox)

        # ev3
        ev3_hbox = self.uief.make_float_entry_element(self.ev3_label, self.ev3_tooltip, 100 * self.env_vars.chance_of_claim, 0, 100)
        layout.addLayout(ev3_hbox)

        # ev4
        ev4_hbox = self.uief.make_float_entry_element(self.ev4_label, self.ev4_tooltip, 100 * self.env_vars.perc_honest_defectors, 0, 100)
        layout.addLayout(ev4_hbox)
       
        # ev5
        ev5_hbox = self.uief.make_float_entry_element(self.ev5_label, self.ev5_tooltip, 100 * self.env_vars.perc_low_morale, 0, 100)
        layout.addLayout(ev5_hbox)

        # ev6
        ev6_hbox = self.uief.make_float_entry_element(self.ev6_label, self.ev6_tooltip, 100 * self.env_vars.perc_independent, 0, 100)
        layout.addLayout(ev6_hbox)

        # ev7
        ev7_hbox = self.uief.make_dropdown_entry_element(self.ev7_label, [2, 3], self.ev7_tooltip, self.env_vars.dependent_thres)
        layout.addLayout(ev7_hbox)

        # ev9
#        ev9_hbox = self.uief.make_static_textbox_element(self.ev9_label, "1/3", self.ev9_tooltip)
#        layout.addLayout(ev9_hbox)

        # ev10
#        ev10_hbox = self.uief.make_static_textbox_element(self.ev10_label, str(env_vars.cov_req), self.ev10_tooltip)
#        layout.addLayout(ev10_hbox)

        # ev11
        ev11_hbox = self.uief.make_numeric_entry_element(self.ev11_label, self.ev11_tooltip, self.env_vars.queueing, 0, 3)
        layout.addLayout(ev11_hbox)
        
        # ev12
#        ev12_hbox = self.uief.make_static_textbox_element(self.ev12_label, "10", self.ev12_tooltip)
#        layout.addLayout(ev12_hbox)

        return layout

