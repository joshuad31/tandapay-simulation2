import sys
from PySide2.QtWidgets import *
from PySide2.QtCore import Qt, QSize

from PySide2.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QLabel, QWidget, QDialog, QTextEdit
from PySide2.QtGui import QFont
from PySide2.QtCore import Qt, QSize

from environment_variables import *
from pricing_variables import *

from settings_menu import *

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
        self.window = PlaceholderWindow("Run Simulation")
        self.window.show()

    def history(self):
        self.window = PlaceholderWindow("History")
        self.window.show()

    def open_settings(self):
        self.settings_dialog = SettingsDialog(self.env_vars, self.pricing_vars, self)
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


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainMenu()
    window.show()
    sys.exit(app.exec_())

