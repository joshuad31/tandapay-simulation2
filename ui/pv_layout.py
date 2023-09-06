import sys

from PySide2.QtWidgets import *
from PySide2.QtCore import Qt, QSize

from PySide2.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QLabel, QWidget, QDialog, QTextEdit
from PySide2.QtGui import QFont
from PySide2.QtCore import Qt, QSize

from ui.ui_element_factory import UI_Element_Factory

class PV_Layout:
    def __init__(self, pricing_vars, widget_width=None):
        self.pv = pricing_vars
        self.uief = UI_Element_Factory(widget_width)
        
        self.pv1_label  = "Change Floor (no refund)" 
        self.pv2_label  = "Change Ceiling (no refund)"
        self.pv3_label  = "Policyholders Leave Floor (no refund)"
        self.pv4_label  = "Policyholders Leave Ceiling (no refund)"
        self.pv5_label  = "Change Floor (refund)" 
        self.pv6_label  = "Change Ceiling (refund)"
        self.pv7_label  = "Policyholders Leave Floor (refund)"    
        self.pv8_label  = "Policyholders Leave Ceiling (refund)"
        self.pv9_label  = "Change Floor (3mo avg)" 
        self.pv10_label = "Change Ceiling (3mo avg)"
        self.pv11_label = "Policyholders Leave Floor (3mo avg)"
        self.pv12_label = "Policyholders Leave Ceiling (3mo avg)"

    def get_pricing_vars(self):
        self.pv.noref_change_floor       = self.uief.getValue(self.pv1_label)  / 100
        self.pv.noref_change_ceiling     = self.uief.getValue(self.pv2_label)  / 100
        self.pv.noref_ph_leave_floor     = self.uief.getValue(self.pv3_label)  / 100
        self.pv.noref_ph_leave_ceiling   = self.uief.getValue(self.pv4_label)  / 100
        self.pv.refund_change_floor      = self.uief.getValue(self.pv5_label)  / 100
        self.pv.refund_change_ceiling    = self.uief.getValue(self.pv6_label)  / 100
        self.pv.refund_ph_leave_floor    = self.uief.getValue(self.pv7_label)  / 100
        self.pv.refund_ph_leave_ceiling  = self.uief.getValue(self.pv8_label)  / 100
        self.pv.avg_3mo_change_floor     = self.uief.getValue(self.pv9_label)  / 100
        self.pv.avg_3mo_change_ceiling   = self.uief.getValue(self.pv10_label) / 100
        self.pv.avg_3mo_ph_leave_floor   = self.uief.getValue(self.pv11_label) / 100
        self.pv.avg_3mo_ph_leave_ceiling = self.uief.getValue(self.pv12_label) / 100
        return self.pv

    def get_pv_layout(self) -> QVBoxLayout:
        layout = QVBoxLayout()
        
        pv1_hbox  = self.uief.make_numeric_entry_element(self.pv1_label,  self.pv1_label,  self.pv.noref_change_floor       * 100, 0, 100)
        pv2_hbox  = self.uief.make_numeric_entry_element(self.pv2_label,  self.pv2_label,  self.pv.noref_change_ceiling     * 100, 0, 100)
        pv3_hbox  = self.uief.make_numeric_entry_element(self.pv3_label,  self.pv3_label,  self.pv.noref_ph_leave_floor     * 100, 0, 100)
        pv4_hbox  = self.uief.make_numeric_entry_element(self.pv4_label,  self.pv4_label,  self.pv.noref_ph_leave_ceiling   * 100, 0, 100)
        pv5_hbox  = self.uief.make_numeric_entry_element(self.pv5_label,  self.pv5_label,  self.pv.refund_change_floor      * 100, 0, 100)
        pv6_hbox  = self.uief.make_numeric_entry_element(self.pv6_label,  self.pv6_label,  self.pv.refund_change_ceiling    * 100, 0, 100)
        pv7_hbox  = self.uief.make_numeric_entry_element(self.pv7_label,  self.pv7_label,  self.pv.refund_ph_leave_floor    * 100, 0, 100)
        pv8_hbox  = self.uief.make_numeric_entry_element(self.pv8_label,  self.pv8_label,  self.pv.refund_ph_leave_ceiling  * 100, 0, 100)
        pv9_hbox  = self.uief.make_numeric_entry_element(self.pv9_label,  self.pv9_label,  self.pv.avg_3mo_change_floor     * 100, 0, 100)
        pv10_hbox = self.uief.make_numeric_entry_element(self.pv10_label, self.pv10_label, self.pv.avg_3mo_change_ceiling   * 100, 0, 100)
        pv11_hbox = self.uief.make_numeric_entry_element(self.pv11_label, self.pv11_label, self.pv.avg_3mo_ph_leave_floor   * 100, 0, 100)
        pv12_hbox = self.uief.make_numeric_entry_element(self.pv12_label, self.pv12_label, self.pv.avg_3mo_ph_leave_ceiling * 100, 0, 100)

        layout.addLayout(pv1_hbox) 
        layout.addLayout(pv2_hbox) 
        layout.addLayout(pv3_hbox) 
        layout.addLayout(pv4_hbox) 
        layout.addLayout(pv5_hbox) 
        layout.addLayout(pv6_hbox)
        layout.addLayout(pv7_hbox) 
        layout.addLayout(pv8_hbox) 
        layout.addLayout(pv9_hbox) 
        layout.addLayout(pv10_hbox) 
        layout.addLayout(pv11_hbox) 
        layout.addLayout(pv12_hbox)

        return layout
