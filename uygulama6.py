import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QWidget, QGridLayout, QLabel, QLineEdit

class GridLayoutExample(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Grid Layout Örneği")
        self.setGeometry(100,100,300,200)
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        layout = QGridLayout()
        layout.addWidget(QPushButton("Buton 1"),0, 0)
        layout.addWidget(QPushButton("Buton 2"),0, 1)
        layout.addWidget(QPushButton("Buton 3"),1, 0)
        layout.addWidget(QPushButton("Buton 4"),1, 1)
        central_widget.setLayout(layout)



app = QApplication(sys.argv)
window = GridLayoutExample()
window.show()
sys.exit(app.exec_())