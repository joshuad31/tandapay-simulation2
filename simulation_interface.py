import sys
from PySide2.QtWidgets import *
from PySide2.QtCore import Qt, QSize

from PySide2.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QLabel, QWidget, QDialog, QTextEdit
from PySide2.QtGui import QFont
from PySide2.QtCore import Qt, QSize

from environment_variables import *
from pricing_variables import *
from system_record import *
from user_record import *

from settings_menu import *

from simulation import *

class MainMenu(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Main Menu")
        self.setFixedSize(300, 300)

        layout = QVBoxLayout()

        title = QLabel("TandaPay")
        title_font = QFont()
        title_font.setBold(True)
        title_font.setPointSize(18)
        title.setFont(title_font)
        title.setAlignment(Qt.AlignCenter)

        layout.addWidget(title)
        layout.addStretch(1)

        self.run_simulation_btn = QPushButton("Run Simulation")
        self.run_simulation_btn.clicked.connect(self.run_simulation)
        layout.addWidget(self.run_simulation_btn)

        self.history_btn = QPushButton("History")
        self.history_btn.clicked.connect(self.history)
        layout.addWidget(self.history_btn)

        # create variables that could be changed in settings
        self.env_vars = Environment_Variables()
        self.pricing_vars = Pricing_Variables() 
        self.simulation_info = Simulation_Info()

        self.settings_btn = QPushButton("Settings")
        self.settings_btn.clicked.connect(self.open_settings)
        layout.addWidget(self.settings_btn)

        self.about_btn = QPushButton("About")
        self.about_btn.clicked.connect(self.open_about)
        layout.addWidget(self.about_btn)

        self.quit_btn = QPushButton("Quit")
        self.quit_btn.clicked.connect(self.quit_program)
        layout.addWidget(self.quit_btn)

        central_widget = QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)


    def run_simulation(self):
        # keep track of the number of wins/losses/draws
        num_wins = 0
        num_draws = 0
        num_losses = 0
        
        # run it n times
        for i in range(self.simulation_info.sample_size):
            result = self.run_simulation_once()

            if result == ResultsEnum.WIN:
                num_wins += 1
            elif result == ResultsEnum.DRAW:
                num_draws += 1
            else:
                num_losses += 1

        # display the results
        results_str = f"""
        num_wins = {num_wins}
        num_draws = {num_draws}
        num_losses = {num_losses}
        total (sample size): {self.simulation_info.sample_size}
        """

        self.window = ResultsWindow("Simulation Results")
        self.window.set_results_text(results_str)
        self.window.show()

    def run_simulation_once(self):
        # initialize user list
        user_list = [User_Record(self.env_vars) for _ in range(self.env_vars.total_member_cnt)]
        
        # perform subgroup setup
        data = subgroup_setup(len(user_list), user_list)
        num_four_member_groups = data[0]
        
        # initialize system record:
        sys_record = System_Record(self.env_vars.total_member_cnt)

        # assign roles
        role_assignment(self.env_vars, user_list, num_four_member_groups * 4)

        # run the simulation and return the result
        return run_simulation(self.env_vars, sys_record, self.pricing_vars, user_list)

    def history(self):
        self.window = PlaceholderWindow("History")
        self.window.show()

    def open_settings(self):
        self.settings_dialog = SettingsDialog(self.env_vars, self.pricing_vars, self.simulation_info, self)
        self.settings_dialog.show()

    def open_about(self):
        self.about_window = AboutWindow()
        self.about_window.show()

    def quit_program(self):
        sys.exit()

class AboutWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("About")
        self.setFixedSize(800, 600)

        layout = QVBoxLayout()

        # Define your HTML content here
        html_content = """
        <h1>About TandaPay</h1>
        <p><a href="https://yourwebsite.com">Link to project</a></p>
        <p>License info...</p>
        """

        text_edit = QTextEdit()
        text_edit.setHtml(html_content)
        text_edit.setReadOnly(True)  # Make it read-only
#        text_edit.setStyleSheet("background-color: white;")  # Set white background

        # Add to layout
        layout.addWidget(text_edit)

        central_widget = QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

class PlaceholderWindow(QMainWindow):
    def __init__(self, title):
        super().__init__()
        self.setWindowTitle(title)
        self.setFixedSize(800, 600)
        label = QLabel("Results will be shown here.")
        label.setAlignment(Qt.AlignCenter)
        self.setCentralWidget(label)

class ResultsWindow(QMainWindow):
    def __init__(self, title):
        super(ResultsWindow, self).__init__()
        self.setWindowTitle(title)
        self.setFixedSize(800, 600)

        # Create a QPlainTextEdit widget
        self.textbox = QPlainTextEdit()

        # Set to read-only
        self.textbox.setReadOnly(True)

        # Set monospace font
        font = QFont("Courier")
        self.textbox.setFont(font)

        # Set white background color
#        self.textbox.setStyleSheet("background-color: white;")

        # Create layout and add widgets
        layout = QVBoxLayout()
        layout.addWidget(self.textbox)

        # Create a central widget for the QMainWindow and set the layout
        central_widget = QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

        # Add a margin around the textbox
#        layout.setContentsMargins(20, 20, 20, 20)

    def set_results_text(self, text):
        self.textbox.setPlainText(text)    

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainMenu()
    window.show()
    sys.exit(app.exec_())

