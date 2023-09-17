
import sys
from PySide2.QtWidgets import *
from PySide2.QtCore import Qt, QSize

from PySide2.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QLabel, QWidget, QDialog, QTextEdit
from PySide2.QtGui import QFont
from PySide2.QtCore import Qt, QSize


class Results_Window(QMainWindow):
    def __init__(self, title):
        super(Results_Window, self).__init__()
        self.setWindowTitle(title)

        # Initialize to 800x600 but make it resizable
        self.resize(800, 600)

        # Create a QPlainTextEdit widget
        self.textbox = QPlainTextEdit()

        # Disable line wrapping
        self.textbox.setLineWrapMode(QPlainTextEdit.NoWrap)

        # Enable horizontal scrollbar
        self.textbox.setHorizontalScrollBarPolicy(Qt.ScrollBarAsNeeded)

        # Set to read-only
        self.textbox.setReadOnly(True)

        # Set monospace font
        font = QFont("Courier")
        self.textbox.setFont(font)

        # Create layout and add widgets
        layout = QVBoxLayout()
        layout.addWidget(self.textbox)

        # Create a central widget for the QMainWindow and set the layout
        central_widget = QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

    def set_results_text(self, text):
        self.textbox.setPlainText(text)

