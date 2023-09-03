import sys

from PySide2.QtWidgets import *
from PySide2.QtCore import Qt, QSize

from PySide2.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QLabel, QWidget, QDialog, QTextEdit
from PySide2.QtGui import QFont
from PySide2.QtCore import Qt, QSize

from ui_element_factory import UI_Element_Factory

class PV_Layout:
    def __init__(self, pricing_vars, widget_width=None):
        self.pv = pricing_vars
        self.uief = UI_Element_Factory(widget_width)
        
        self.pv1_label = "PV1: Premium Increase Floor"
        self.pv2_label = "PV2: Policyholders Leave Floor"
        self.pv3_label = "PV3: Premium Increase Ceiling"
        self.pv4_label = "PV4: Policyholders Leave Ceiling"
        self.pv5_label = "PV5: Premium Increase Cumulative"
        self.pv6_label = "PV6: Policyholders Leave Cumulative"
    
    def get_pricing_vars(self):
        self.pv.prem_inc_floor   = self.uief.getValue(self.pv1_label)
        self.pv.ph_leave_floor   = self.uief.getValue(self.pv2_label)
        self.pv.prem_inc_ceiling = self.uief.getValue(self.pv3_label)
        self.pv.ph_leave_ceiling = self.uief.getValue(self.pv4_label)
        self.pv.prem_inc_cum     = self.uief.getValue(self.pv5_label)
        self.pv.ph_leave_cum     = self.uief.getValue(self.pv6_label)

        return self.pv

    def get_pv_layout(self) -> QVBoxLayout:
        layout = QVBoxLayout()
        
        pv1_hbox = self.uief.make_numeric_entry_element(self.pv1_label, self.pv1_label, self.pv.prem_inc_floor * 100, 0, 100)
        pv2_hbox = self.uief.make_numeric_entry_element(self.pv2_label, self.pv2_label, self.pv.ph_leave_floor * 100, 0, 100)
        pv3_hbox = self.uief.make_numeric_entry_element(self.pv3_label, self.pv3_label, self.pv.prem_inc_ceiling * 100, 0, 100)
        pv4_hbox = self.uief.make_numeric_entry_element(self.pv4_label, self.pv4_label, self.pv.ph_leave_ceiling * 100, 0, 100)
        pv5_hbox = self.uief.make_numeric_entry_element(self.pv5_label, self.pv5_label, self.pv.prem_inc_cum * 100, 0, 100)
        pv6_hbox = self.uief.make_numeric_entry_element(self.pv6_label, self.pv6_label, self.pv.ph_leave_cum * 100, 0, 100)

        layout.addLayout(pv1_hbox) 
        layout.addLayout(pv2_hbox) 
        layout.addLayout(pv3_hbox) 
        layout.addLayout(pv4_hbox) 
        layout.addLayout(pv5_hbox) 
        layout.addLayout(pv6_hbox)

        return layout
