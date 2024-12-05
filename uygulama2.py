import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton

class MainWindow2(QMainWindow):
    def __init__(self):
        super().__init__()
        #Pencere baslıgını ayarlayalım
        self.setWindowTitle("Buton Örneği")
        self.button = QPushButton("BUTONA TIKLA")
        self.button.clicked.connect(self.button_clicked)
        self.setCentralWidget(self.button)

    def button_clicked(self):
        print("Butona tıklandı")

app = QApplication(sys.argv)
window = MainWindow2()
window.show()
sys.exit(app.exec_())