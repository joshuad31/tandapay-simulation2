import sys
from PySide2.QtWidgets import (QApplication, QWidget, QVBoxLayout, QHBoxLayout, 
                               QPushButton, QLineEdit, QFileDialog, QTabWidget, QLabel, QSpinBox)

class CustomUI(QWidget):
    
    environment_variable_descriptions = [
        ("EV1: Total number of members"             , 100 ),
        ("EV2: Monthly Premium"                     , 100 ), 
        ("EV3: Chance of Claim"                     , 25  ),
        ("EV4: Percentage of honest defectors"      , 10  ),
        ("EV5: Percentage of low-morale members"    , 10  ),
        ("EV6: Percentage of independent members"   , 20  ),
        ("EV7: Dependent Threshold"                 , 2   ),
        ("EV9: Low Morale Quit Probability"         , 33  ) 
    ]

    def __init__(self):
        super().__init__()

        

    def browse_file(self):
        file_path, _ = QFileDialog.getOpenFileName(self, "Open File")
        if file_path:
            self.file_path_edit.setText(file_path)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = CustomUI()
    window.show()
    sys.exit(app.exec_())

