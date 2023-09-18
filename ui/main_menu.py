import sys
from PySide2.QtWidgets import *
from PySide2.QtCore import Qt, QSize

from PySide2.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QLabel, QWidget, QDialog, QTextEdit
from PySide2.QtGui import QFont
from PySide2.QtCore import Qt, QSize

from .ui_element_factory import UI_Element_Factory
from .ui_context import UI_Context
from .settings_menu import Settings_Menu
from .results_menu import Results_Window

class Main_Menu(QMainWindow):
    def __init__(self, ui_context: UI_Context):
        # initialize the main menu's window
        super().__init__()
        self.setWindowTitle("Tandapay Simulation")
        self.resize(300, 360)

        # create ui element factory for creating UI elements
        self.uief = UI_Element_Factory()
        
        # will store all the callbacks for buttons in the main menu
        self.uic = ui_context

        # set up layout for the main menu
        self.layout = QVBoxLayout()
        
        # create the title at the top of the menu
        self.title = self.get_title_widget()
        self.layout.addWidget(self.title)
        self.layout.addStretch(1)
        
        # make buttons for main menu
        self.run_simulation_btn = self.uief.make_push_button_element("Run Simulation", None, self.run_simulation)
        self.layout.addWidget(self.run_simulation_btn)

        self.run_statistics_btn = self.uief.make_push_button_element("Run Statistics", None, self.run_statistics)
        self.layout.addWidget(self.run_statistics_btn)

        self.run_debug_btn = self.uief.make_push_button_element("Run Debug", None, self.run_debug)
        self.layout.addWidget(self.run_debug_btn)

        self.settings_btn = self.uief.make_push_button_element("Settings", None, self.settings)
        self.layout.addWidget(self.settings_btn)

        self.history_btn = self.uief.make_push_button_element("History", None, self.uic.history)
        self.layout.addWidget(self.history_btn)

        self.about_btn = self.uief.make_push_button_element("About", None, self.uic.about)
        self.layout.addWidget(self.about_btn)
    
        self.quit_btn = self.uief.make_push_button_element("Quit", None, sys.exit)
        self.layout.addWidget(self.quit_btn)

        # finally, set this as the central widget. The central widget
        # is simply the QT widget that occupies all the space in the main window
        self.central_widget = QWidget()
        self.central_widget.setLayout(self.layout)
        self.setCentralWidget(self.central_widget)

    def run_simulation(self):
        result_str = self.uic.run_simulation()
        self.results_window = Results_Window("Simulation Results")
        self.results_window.set_results_text(result_str)
        self.results_window.show()

    def run_statistics(self):
        result_str = self.uic.run_statistics()
        self.results_window = Results_Window("Statistics Results")
        self.results_window.set_results_text(result_str)
        self.results_window.show()

    def run_debug(self):
        result_str = self.uic.run_debug()
        self.results_window = Results_Window("Debug Results")
        self.results_window.set_results_text(result_str)
        self.results_window.show()

    def settings(self):
        self.settings_menu = Settings_Menu(self.uic, 150)
        self.settings_menu.open_settings_menu()

    def get_title_widget(self) -> QLabel:
        title = QLabel("Tandapay")
        title_font = QFont()
        title_font.setBold(True)
        title_font.setPointSize(18)
        title.setFont(title_font)
        title.setAlignment(Qt.AlignCenter)
        return title

