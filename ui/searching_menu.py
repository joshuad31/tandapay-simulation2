import sys
from PySide2.QtWidgets import *
from PySide2.QtCore import Qt, QSize

from PySide2.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QLabel, QWidget, QDialog, QTextEdit
from PySide2.QtGui import QFont
from PySide2.QtCore import Qt, QSize

from .ui_element_factory import UI_Element_Factory
from .results_menu import Results_Window
from .ui_context import UI_Context

from stats.searching_attributes import searching_attributes
from simulation.other_variables import OutcomeEnum

class Searching_Menu:
    def __init__(self, ui_context, widget_width=None):
        self.uic = ui_context
        
        self.uief = UI_Element_Factory(widget_width)

        self.dialog = QDialog()
        self.dialog.setWindowTitle("Searching Menu")
       
        self.field1_label = "Target Percent"
        self.field1_tooltip = "What win/loss/draw (select later) percent do you want to search for?"

        self.field2_label = "Outcome to target"
        self.field2_tooltip = "Do you want to search for a percentage of wins, losses, or ties?"

        self.field3_label = "Min value"
        self.field3_tooltip = "Minimum value you want to consider in the linear regression model"

        self.field4_label = "Max value"
        self.field4_tooltip = "Maximum value you want to consider in the linear regression model"

        self.field5_label = "Steps"
        self.field5_tooltip = "How many samples between min/max you want to consider in the linear regression model"

        self.field6_label = "Order"
        self.field6_tooltip = "What order polynomial do you want to use for the linear regression model?"
        
        self.field7_label = "Attribute to search"
        self.field7_tooltip = "What variable do you want to search for?"
       
        self.dialog = None

    def create_menu_dialog(self):
        self.dialog = QDialog()
        self.dialog.setWindowTitle("Searching Menu")
        
        self.layout = QVBoxLayout()

        self.field1_hbox = self.uief.make_float_entry_element(self.field1_label, self.field1_tooltip, 50, 0, 100)
        self.layout.addLayout(self.field1_hbox)
        
        options = [option.name for option in OutcomeEnum]
        self.field2_hbox = self.uief.make_dropdown_entry_element(self.field2_label, options, self.field2_tooltip)
        self.layout.addLayout(self.field2_hbox)

        self.field3_hbox = self.uief.make_float_entry_element(self.field3_label, self.field3_tooltip, 0, 0, 100)
        self.layout.addLayout(self.field3_hbox)

        self.field4_hbox = self.uief.make_float_entry_element(self.field4_label, self.field4_tooltip, 100, 0, 100)
        self.layout.addLayout(self.field4_hbox)

        self.field5_hbox = self.uief.make_numeric_entry_element(self.field5_label, self.field5_tooltip, 20, 5, 100)
        self.layout.addLayout(self.field5_hbox)

        self.field6_hbox = self.uief.make_numeric_entry_element(self.field6_label, self.field6_tooltip, 3, 1, 10)
        self.layout.addLayout(self.field6_hbox)

        self.field7_hbox = self.uief.make_dropdown_entry_element(self.field7_label, searching_attributes, self.field7_tooltip)
        self.layout.addLayout(self.field7_hbox)
        
        self.run_button = self.uief.make_push_button_element("Search", "Perform the search with these parameters", self.run)
        self.layout.addWidget(self.run_button)

        self.dialog.setLayout(self.layout)
        return self.dialog

    def open_searching_menu(self):
        if not self.dialog:
            self.create_menu_dialog()
        
        self.dialog.setModal(False)
        self.dialog.show()
    
    def run(self):
        target_percent = self.uief.getValue(self.field1_label)
        outcome = OutcomeEnum[self.uief.getValue(self.field2_label)]
        min_value = self.uief.getValue(self.field3_label) / 100
        max_value = self.uief.getValue(self.field4_label) / 100
        steps = self.uief.getValue(self.field5_label)
        order = self.uief.getValue(self.field6_label)
        attribute = self.uief.getValue(self.field7_label)

        result_str = self.uic.run_searching(attribute, target_percent, outcome, min_value, max_value, steps, order)
        self.results_window = Results_Window("Search Results")
        self.results_window.set_results_text(result_str)
        self.results_window.setWindowFlags(Qt.Window)
        self.results_window.show()
