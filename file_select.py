from PySide6.QtWidgets import QWidget, QLabel, QLineEdit, QPushButton

class FileSelect(QWidget):
    def __init__(self, file):
        super().__init__()
        self.file = file
        self.setWindowTitle("Select file:")
        self.setGeometry(200,200, 350, 150)

        label = QLabel("Enter file name:", self)
        label.setGeometry(20, 20, 310, 30)

        self.file_input = QLineEdit(self)
        self.file_input.setGeometry(20, 50, 310, 30)

        confirm_btn = QPushButton("Open the file", self)
        confirm_btn.setGeometry(130, 100, 120, 30)
        confirm_btn.clicked.connect(self.confirm_selection)

    def confirm_selection(self):
        file_name = self.file_input.text().strip()
        if file_name:
            self.file.selected_file = file_name
            self.file.read()
            self.close()