import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QWidget, QVBoxLayout

class VerticalLayoutExample(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QVBoxLayout Örneği")
        self.setGeometry(100,100,300,200)
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        layout = QVBoxLayout()
        button1 = QPushButton("Buton 1")
        button2 = QPushButton("Buton 2")
        button3 = QPushButton("Buton 3")
        layout.addWidget(button1)
        layout.addWidget(button2)
        layout.addWidget(button3)
        central_widget.setLayout(layout)


app = QApplication(sys.argv)
window = VerticalLayoutExample()
window.show()
sys.exit(app.exec_())