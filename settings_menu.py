import sys
from PySide2.QtWidgets import *
from PySide2.QtCore import Qt, QSize

from PySide2.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QLabel, QWidget, QDialog, QTextEdit
from PySide2.QtGui import QFont
from PySide2.QtCore import Qt, QSize


from environment_variables import *
from pricing_variables import *

class SettingsDialog(QDialog):
    def __init__(self, env_vars, pricing_vars, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Settings")
        self.setFixedSize(800, 600)  # Fixed size for the settings window

        # Main layout for settings
        self.main_layout = QVBoxLayout(self)

        # Two-column layout
        self.two_column_layout = QHBoxLayout()

        self.widget_width = 120

        # Left column
        self.left_layout = QVBoxLayout()

        # EV1
        self.ev1_spinbox = QSpinBox()
        self.ev1_spinbox.setMinimum(1)
        self.ev1_spinbox.setMaximum(2147483647)
        self.ev1_spinbox.setValue(env_vars.total_member_cnt)
        self.ev1_spinbox.valueChanged.connect(lambda value: self.updateValue(env_vars, 'total_member_cnt', value))
        self.ev1_spinbox.setFixedWidth(self.widget_width)
        ev1_label = QLabel("EV1: Total Member Count")
        ev1_label.setToolTip("How many members are initially in the simulation?")
        ev1_hbox = QHBoxLayout()
        ev1_hbox.addWidget(ev1_label)
        ev1_hbox.addWidget(self.ev1_spinbox)
        self.left_layout.addLayout(ev1_hbox)

        # EV2
        self.ev2_spinbox = QSpinBox()
        self.ev2_spinbox.setMinimum(1)
        self.ev2_spinbox.setMaximum(2147483647)
        self.ev2_spinbox.setValue(env_vars.monthly_premium)
        self.ev2_spinbox.valueChanged.connect(lambda value: self.updateValue(env_vars, 'monthly_premium', value))
        self.ev2_spinbox.setFixedWidth(self.widget_width)
        ev2_label = QLabel("EV2: Monthly Premium")
        ev2_label.setToolTip("What is the initial monthly premium?")
        ev2_hbox = QHBoxLayout()
        ev2_hbox.addWidget(ev2_label)
        ev2_hbox.addWidget(self.ev2_spinbox)
        self.left_layout.addLayout(ev2_hbox)

        # EV3
        self.ev3_spinbox = QSpinBox()
        self.ev3_spinbox.setMinimum(25)
        self.ev3_spinbox.setMaximum(75)
        self.ev3_spinbox.setValue(env_vars.chance_of_claim * 100)
        self.ev3_spinbox.valueChanged.connect(lambda value: self.updateValue(env_vars, 'chance_of_claim', value / 100))
        self.ev3_spinbox.setFixedWidth(self.widget_width)
        ev3_label = QLabel("EV3: Chance of Claim")
        ev3_label.setToolTip("What is the chance of a claim each month?")
        ev3_hbox = QHBoxLayout()
        ev3_hbox.addWidget(ev3_label)
        ev3_hbox.addWidget(self.ev3_spinbox)
        self.left_layout.addLayout(ev3_hbox)

        # EV4
        self.ev4_spinbox = QSpinBox()
        self.ev4_spinbox.setMinimum(10)
        self.ev4_spinbox.setMaximum(45)
        self.ev4_spinbox.setValue(env_vars.perc_honest_defectors * 100)
        self.ev4_spinbox.valueChanged.connect(lambda value: self.updateValue(env_vars, 'perc_honest_defectors', value / 100))
        self.ev4_spinbox.setFixedWidth(self.widget_width)
        ev4_label = QLabel("EV4: Percent Honest Defectors")
        ev4_label.setToolTip("What percentage of users are honest defectors?")
        ev4_hbox = QHBoxLayout()
        ev4_hbox.addWidget(ev4_label)
        ev4_hbox.addWidget(self.ev4_spinbox)
        self.left_layout.addLayout(ev4_hbox)

        # EV5
        self.ev5_spinbox = QSpinBox()
        self.ev5_spinbox.setMinimum(10)
        self.ev5_spinbox.setMaximum(30)
        self.ev5_spinbox.setValue(env_vars.perc_low_morale * 100)
        self.ev5_spinbox.valueChanged.connect(lambda value: self.updateValue(env_vars, 'perc_low_morale', value / 100))
        self.ev5_spinbox.setFixedWidth(self.widget_width)
        ev5_label = QLabel("EV5: Percent Low Morale")
        ev5_label.setToolTip("What percentage of users are low morale?")
        ev5_hbox = QHBoxLayout()
        ev5_hbox.addWidget(ev5_label)
        ev5_hbox.addWidget(self.ev5_spinbox)
        self.left_layout.addLayout(ev5_hbox)

        # EV6
        self.ev6_spinbox = QSpinBox()
        self.ev6_spinbox.setMinimum(20)
        self.ev6_spinbox.setMaximum(80)
        self.ev6_spinbox.setValue(env_vars.perc_independent * 100)
        self.ev6_spinbox.valueChanged.connect(lambda value: self.updateValue(env_vars, 'perc_independent', value / 100))
        self.ev6_spinbox.setFixedWidth(self.widget_width)
        ev6_label = QLabel("EV6: Percent Independent")
        ev6_label.setToolTip("What percentage of users are independent?")
        ev6_hbox = QHBoxLayout()
        ev6_hbox.addWidget(ev6_label)
        ev6_hbox.addWidget(self.ev6_spinbox)
        self.left_layout.addLayout(ev6_hbox)

        # EV7
        self.ev7_combobox = QComboBox()
        self.ev7_combobox.addItem("2")
        self.ev7_combobox.addItem("3")
        self.ev7_combobox.setCurrentText(str(env_vars.dependent_thres))  # Set initial value
        self.ev7_combobox.currentIndexChanged.connect(lambda index: self.updateValue(env_vars, 'dependent_thres', int(self.ev7_combobox.currentText())))
        self.ev7_combobox.setFixedWidth(self.widget_width)
        ev7_label = QLabel("EV7: Dependent Threshold")
        ev7_label.setToolTip("What is the member threshold needed for dependent members to defect? (allowed values: 2, 3)")
        ev7_hbox = QHBoxLayout()
        ev7_hbox.addWidget(ev7_label)
        ev7_hbox.addWidget(self.ev7_combobox)
        self.left_layout.addLayout(ev7_hbox)

        # EV9
        self.ev9_textbox = QLineEdit("1/3")
        self.ev9_textbox.setReadOnly(True)
        self.ev9_textbox.setFixedWidth(self.widget_width)
        ev9_label = QLabel("EV9: Low Morale Quit Probability")
        ev9_label.setToolTip("Probability a low-morale member will quit if forced to reorg (Must be 1/3)")
        ev9_hbox = QHBoxLayout()
        ev9_hbox.addWidget(ev9_label)
        ev9_hbox.addWidget(self.ev9_textbox)
        self.left_layout.addLayout(ev9_hbox)

        # EV10
        self.ev10_textbox = QLineEdit(str(env_vars.cov_req)) 
        self.ev10_textbox.setReadOnly(True)
        self.ev10_textbox.setFixedWidth(self.widget_width)
        ev10_label = QLabel("EV10: Coverage Requirement")
        ev10_label.setToolTip("Coverage Requirement. Equal to EV1 * EV2. Is the total value of the claim which the members must pay")
        ev10_hbox = QHBoxLayout()
        ev10_hbox.addWidget(ev10_label)
        ev10_hbox.addWidget(self.ev10_textbox)
        self.left_layout.addLayout(ev10_hbox)

        # EV11 
        self.ev11_spinbox = QSpinBox()
        self.ev11_spinbox.setMinimum(0)
        self.ev11_spinbox.setMaximum(3)
        self.ev11_spinbox.setValue(env_vars.queueing)
        self.ev11_spinbox.valueChanged.connect(lambda value: self.updateValue(env_vars, 'queueing', value))
        self.ev11_spinbox.setFixedWidth(self.widget_width)
        ev11_label = QLabel("EV11: Queuing")
        ev11_label.setToolTip("Number of periods to do queuing for. Queuing delays repayments")
        ev11_hbox = QHBoxLayout()
        ev11_hbox.addWidget(ev11_label)
        ev11_hbox.addWidget(self.ev11_spinbox)
        self.left_layout.addLayout(ev11_hbox)


        # EV12 
        self.ev12_textbox = QLineEdit("10")  # Initialize with 0 or any starting value
        self.ev12_textbox.setReadOnly(True)
        self.ev12_textbox.setFixedWidth(self.widget_width)
        ev12_label = QLabel("EV12: Periods")
        ev12_label.setToolTip("Maximum number of periods the simulation will run for")
        ev12_hbox = QHBoxLayout()
        ev12_hbox.addWidget(ev12_label)
        ev12_hbox.addWidget(self.ev12_textbox)
        self.left_layout.addLayout(ev12_hbox)


        # Right column with QSplitter
        self.right_layout = QVBoxLayout()
        self.splitter = QSplitter(Qt.Vertical)

        self.top_spinbox = QSpinBox()
        self.top_layout = QVBoxLayout()

        pv_info = [
            ("PV1: Premium Increase Floor", "Premium Price Increase Floor", 'prem_inc_floor'),
            ("PV2: Premium Increase Ceiling", "Premium Price Increase Ceiling", 'prem_inc_ceiling'),
            ("PV3: Premium Increase Cumulative", "Premium Price Increase Cumulative", 'prem_inc_cum'),
            ("PV4: Policyholders Leave Floor", "Policyholders Leave Floor", 'ph_leave_floor'),
            ("PV5: Policyholders Leave Ceiling", "Policyholders Leave Ceiling", 'ph_leave_ceiling'),
            ("PV6: Policyholders Leave Cumulative", "Policyholders Leave Cumulative", 'ph_leave_cum')
        ]

        # PV1 - PV6
        for i in range(len(pv_info)):
            self.pv_spinbox = QSpinBox()
            self.pv_spinbox.setMinimum(0)
            self.pv_spinbox.setMaximum(100)
            self.pv_spinbox.setValue(getattr(pricing_vars, pv_info[i][2]) * 100)
            self.pv_spinbox.valueChanged.connect(
                lambda value, var_name=pv_info[i][2]: self.updateValue(pricing_vars, var_name, value / 100)
            )
            self.pv_spinbox.setFixedWidth(self.widget_width)
            pv_label = QLabel(pv_info[i][0])
            pv_label.setToolTip(pv_info[i][1])
            pv_hbox = QHBoxLayout()
            pv_hbox.addWidget(pv_label)
            pv_hbox.addWidget(self.pv_spinbox)
            self.top_layout.addLayout(pv_hbox)

        self.bottom_layout = QVBoxLayout()

        # Other vars:

        # Sample Size
        self.sample_size_spinbox = QSpinBox()
        self.sample_size_spinbox.setMinimum(1)
        self.sample_size_spinbox.setFixedWidth(self.widget_width)
        sample_size_label = QLabel("Sample Size")
        sample_size_label.setToolTip("Number of times the simulation will run")
        sample_size_hbox = QHBoxLayout()
        sample_size_hbox.addWidget(sample_size_label)
        sample_size_hbox.addWidget(self.sample_size_spinbox)
        self.bottom_layout.addLayout(sample_size_hbox)

        self.top_widget = QWidget()
        self.top_widget.setLayout(self.top_layout)

        self.bottom_widget = QWidget()
        self.bottom_widget.setLayout(self.bottom_layout)

        self.splitter.addWidget(self.top_widget)
        self.splitter.addWidget(self.bottom_widget)
        self.splitter.setSizes([360, 240])

        self.right_layout.addWidget(self.splitter)

        # Add left and right layouts to the two-column layout
        self.two_column_layout.addLayout(self.left_layout)
        self.two_column_layout.addLayout(self.right_layout)

        # Add two-column layout to the main layout
        self.main_layout.addLayout(self.two_column_layout)

        # OK and Cancel buttons
        self.button_box = QDialogButtonBox(QDialogButtonBox.Ok)
        self.button_box.accepted.connect(self.accept)
#        self.button_box.rejected.connect(self.reject)
        self.main_layout.addWidget(self.button_box)

    def updateValue(self, obj, attribute_name, value):
        setattr(obj, attribute_name, value)
        
        A = (attribute_name == 'total_member_cnt')
        B = (attribute_name == 'monthly_premium')
        C = isinstance(obj, Environment_Variables)

        if (A or B) and C:
            self.ev10_textbox.setText(str(obj.cov_req))
    
