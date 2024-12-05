import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QWidget, QFormLayout, QLabel, QLineEdit

class FormLayoutExample(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QHBoxLayout Örneği")
        self.setGeometry(100,100,300,200)
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        f_layout = QFormLayout()
        self.name_label = QLabel("Ad :")
        self.name_input = QLineEdit(self)
        self.email_label = QLabel("Email")
        self.email_input = QLineEdit(self)
        f_layout.addRow(self.name_label, self.name_input)
        f_layout.addRow(self.email_label, self.email_input)
        save_button = QPushButton("KAYDET")
        f_layout.addRow(save_button)
        central_widget.setLayout(f_layout)



app = QApplication(sys.argv)
window = FormLayoutExample()
window.show()
sys.exit(app.exec_())