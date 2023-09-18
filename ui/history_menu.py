from PySide2.QtWidgets import QDialog, QVBoxLayout, QListWidget, QListWidgetItem
from PySide2.QtCore import Qt

from .results_menu import Results_Window

class History_Menu(QDialog):
    def __init__(self, ui_context, parent=None):
        super(History_Menu, self).__init__(parent)

        self.setWindowTitle("Results History")
        
        self.db = ui_context.history_db_obj # database
        
        self.layout = QVBoxLayout()
        self.list_widget = QListWidget()
        
        self.populate_results()
        
        self.list_widget.itemDoubleClicked.connect(self.show_result)
        
        self.layout.addWidget(self.list_widget)
        
        self.setLayout(self.layout)
        
    def populate_results(self):
        results = self.db.get_results()
        for result in results:
            item = QListWidgetItem(f"{result[1]} - {result[2]} ({result[3]})")
            item.setData(Qt.UserRole, result[0])  # Store the unique ID as user data
            self.list_widget.addItem(item)
        
    def show_result(self, item):
        result_id = item.data(Qt.UserRole)
        contents = self.db.get_result_by_id(result_id)
        self.results_window = Results_Window(item.text())
        self.results_window.set_results_text(contents)
        self.results_window.show()

