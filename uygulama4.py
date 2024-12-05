import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QWidget, QHBoxLayout

class HorizontalLayoutExample(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QHBoxLayout Örneği")
        self.setGeometry(100,100,300,200)
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        h_layout = QHBoxLayout()
        button1 = QPushButton("Buton1")
        button2 = QPushButton("Buton2")
        button3 = QPushButton("Buton3")
        h_layout.addWidget(button1)
        h_layout.addWidget(button2)
        h_layout.addWidget(button3)
        central_widget.setLayout(h_layout)


app = QApplication(sys.argv)
window = HorizontalLayoutExample()
window.show()
sys.exit(app.exec_())