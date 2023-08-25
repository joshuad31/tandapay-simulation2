import sys
from PySide2.QtWidgets import *
from PySide2.QtCore import Qt, QSize


import sys
from PySide2.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QLabel, QWidget, QDialog, QTextEdit
from PySide2.QtGui import QFont
from PySide2.QtCore import Qt, QSize

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

        self.single_run_btn = QPushButton("Single Run")
        self.single_run_btn.clicked.connect(self.single_run)
        layout.addWidget(self.single_run_btn)

        self.matrix_run_btn = QPushButton("Matrix Run")
        self.matrix_run_btn.clicked.connect(self.matrix_run)
        layout.addWidget(self.matrix_run_btn)

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

    def single_run(self):
        self.window = PlaceholderWindow("Single Run")
        self.window.show()

    def matrix_run(self):
        self.window = PlaceholderWindow("Matrix Run")
        self.window.show()

    def open_settings(self):
        self.settings_dialog = SettingsDialog(self)
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

class SettingsDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Settings")
        self.setFixedSize(800, 600)  # Fixed size for the settings window

        # Main layout for settings
        self.main_layout = QVBoxLayout(self)

        # Tabs for Single and Matrix run variables
        self.tabs = QTabWidget()
        self.single_run_tab = QWidget()
        self.matrix_run_tab = QWidget()
        about_dialog = QDialog(self)
        about_dialog.setWindowTitle("About")
        layout = QVBoxLayout()
        text_edit = QTextEdit()
        text_edit.setPlainText("About content here...\nLink to project...\nLicense info...")
        layout.addWidget(text_edit)
        about_dialog.setLayout(layout)
        about_dialog.exec_()

        # Single Run Tab
        self.layout_single_run = QVBoxLayout(self.single_run_tab)
        self.single_run_spinbox = QSpinBox()
        self.layout_single_run.addWidget(self.single_run_spinbox)
        self.tabs.addTab(self.single_run_tab, "Single Run Variables")

        # Matrix Run Tab
        self.layout_matrix_run = QVBoxLayout(self.matrix_run_tab)
        self.matrix_run_spinbox = QSpinBox()
        self.layout_matrix_run.addWidget(self.matrix_run_spinbox)
        self.tabs.addTab(self.matrix_run_tab, "Matrix Run Variables")

        self.main_layout.addWidget(self.tabs)

        # OK and Cancel buttons
        self.button_box = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel)
        self.button_box.accepted.connect(self.accept)
        self.button_box.rejected.connect(self.reject)
        self.main_layout.addWidget(self.button_box)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainMenu()
    window.show()
    sys.exit(app.exec_())

