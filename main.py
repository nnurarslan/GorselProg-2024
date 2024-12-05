import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("PyQt Örneği")
        label = QLabel("Merhaba PyQt!")
        self.setCentralWidget(label)

app = QApplication(sys.argv)
window = MainWindow()
window.show()
sys.exit(app.exec_())