import sys

from PySide2.QtWidgets import *
from PySide2.QtCore import Qt, QSize

from PySide2.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QLabel, QWidget, QDialog, QTextEdit
from PySide2.QtGui import QFont
from PySide2.QtCore import Qt, QSize

from PySide2.QtWidgets import QVBoxLayout, QSpinBox, QLabel, QHBoxLayout, QComboBox, QLineEdit
from PySide2.QtCore import Qt

from typing import List, Optional, Union

class UI_Element_Factory:
    def __init__(self, widget_width=None):
        self.widget_values = {}
        self.widget_width = widget_width

    def getValue(self, label):
        widget = self.widget_values.get(label)
        if widget is None:
            return None  # Return None if the widget is not found

        if isinstance(widget, QSpinBox):
            return widget.value()
        elif isinstance(widget, QComboBox):
            return widget.currentText()
        elif isinstance(widget, QDoubleSpinBox):
            return widget.value()
        else:
            return None  # Return None for unsupported widget types
    
    def make_push_button_element(self, label, tooltip=None, callback=None) -> QPushButton:
        # Create a QPushButton
        button = QPushButton(label)
        
        # Set the tooltip if provided
        if tooltip:
            button.setToolTip(tooltip)

        # Set the button width (optional)
        if self.widget_width:
            button.setFixedWidth(self.widget_width)
        
        # Connect the button's clicked signal to the callback function if provided
        if callback:
            button.clicked.connect(callback)
        
        # Store the widget for later retrieval
        self.widget_values[label] = button
        
        return button

    def make_numeric_entry_element(self, label, tooltip=None, initial_value=None, minimum=0, maximum=2147483647, callback=None) -> QHBoxLayout:
        spinbox = QSpinBox()
        spinbox.setMinimum(minimum)
        spinbox.setMaximum(maximum)
        
        if initial_value is not None:
            spinbox.setValue(initial_value)
        
        if self.widget_width:
            spinbox.setFixedWidth(self.widget_width)
   
        self.widget_values[label] = spinbox  # Store the widget for later retrieval

        label_widget = QLabel(label)
        if tooltip:
            label_widget.setToolTip(tooltip)

        if callback:
            spinbox.valueChanged.connect(callback)

        hbox = QHBoxLayout()
        hbox.addWidget(label_widget)
        hbox.addWidget(spinbox, 0.5)
        return hbox
    
    def make_float_entry_element(self, label, tooltip=None, initial_value=None, minimum=0.0, maximum=1.0, callback=None):
        # Create a QDoubleSpinBox widget
        double_spin_box = QDoubleSpinBox()
        double_spin_box.setMinimum(minimum)
        double_spin_box.setMaximum(maximum)
        double_spin_box.setDecimals(6)
        double_spin_box.setSingleStep(0.01)
        
        # Set its properties
        if tooltip:
            double_spin_box.setToolTip(tooltip)
    
        if initial_value:
            double_spin_box.setValue(initial_value)
        
        if self.widget_width is not None:
            double_spin_box.setFixedWidth(self.widget_width)
        
        # Connect the callback if provided
        if callback:
            double_spin_box.valueChanged.connect(callback)
        
        # Add the widget to the dictionary
        self.widget_values[label] = double_spin_box
        
        # Create a label for the widget
        lbl = QLabel(label)
        
        # Create a horizontal layout and add the label and widget to it
        hbox = QHBoxLayout()
        hbox.addWidget(lbl)
        hbox.addWidget(double_spin_box)
        
        return hbox

    def make_dropdown_entry_element(self, label, options, tooltip=None, initial_value=None, callback=None) -> QHBoxLayout:
        combobox = QComboBox()
        for option in options:
            combobox.addItem(str(option))
        if initial_value:
            combobox.setCurrentText(str(initial_value))
        
        if self.widget_width:
            combobox.setFixedWidth(self.widget_width)
        

        self.widget_values[label] = combobox  # Store the widget for later retrieval

        label_widget = QLabel(label)
        if tooltip:
            label_widget.setToolTip(tooltip)

        if callback:
            spinbox.valueChanged.connect(callback)

        hbox = QHBoxLayout()
        hbox.addWidget(label_widget)
        hbox.addWidget(combobox)
        return hbox

    def make_static_textbox_element(self, label, text, tooltip=None) -> QHBoxLayout:
        textbox = QLineEdit(text)
        textbox.setReadOnly(True)
        
        if self.widget_width:
            textbox.setFixedWidth(self.widget_width)

        label_widget = QLabel(label)
        if tooltip:
            label_widget.setToolTip(tooltip)

        hbox = QHBoxLayout()
        hbox.addWidget(label_widget)
        hbox.addWidget(textbox)
        return hbox

    def make_file_explorer_element(self, label, tooltip=None, initial_path=None, callback=None) -> QHBoxLayout:
        # Create a button that will open the file dialog
        button = QPushButton("Browse...")
        
        # Set the tooltip if provided
        if tooltip:
            button.setToolTip(tooltip)
        
        # Set the button width (optional)
        if self.widget_width:
            button.setFixedWidth(self.widget_width)
        
        # Create a line edit to display the selected file path
        #line_edit = QLineEdit()
        #line_edit.setReadOnly(True)
        
        #if initial_path:
        #    line_edit.setText(initial_path)
        
        # Create a label
        label_widget = QLabel(label)
        
        def open_file_dialog():
            options = QFileDialog.Options()
            file_name, _ = QFileDialog.getOpenFileName(None, "Select File", "", "All Files (*)", options=options)
            if file_name:
                line_edit.setText(file_name)
                self.widget_values[label] = file_name  # Store the selected file path for later retrieval
                
                if callback:
                    callback(file_name)
        
        # Connect the button's clicked signal to open the file dialog
        button.clicked.connect(open_file_dialog)
        
        # Arrange label, line_edit and button in a horizontal layout
        hbox = QHBoxLayout()
        hbox.addWidget(label_widget)
        #hbox.addWidget(line_edit)
        hbox.addWidget(button)
        
        return hbox 
