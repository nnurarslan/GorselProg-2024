import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit

class LayoutExample(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Layout Örneği")
        self.setGeometry(100,100,500,400)
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        #Ana yerleşim (layout) oluşturuyoruz. (DİKEY)
        main_layout = QVBoxLayout()
        #Birinci grup için yatay layout
        h_layout = QHBoxLayout()
        #Yatay layouta ekleyeceğimiz widgetlar
        self.label = QLabel("Kullanıcı Adı:")
        self.line_edit = QLineEdit(self)
        h_layout.addWidget(self.label)
        h_layout.addWidget(self.line_edit)
        #Yatay layoutu ana dikey layouta ekliyoruz
        main_layout.addLayout(h_layout)
        #İkinci grup dikey layouta bir buton
        self.button=QPushButton("gönder")
        main_layout.addWidget(self.button)
        #Üçüncü grup yatay layout kullanarak iki buton
        button_layout = QHBoxLayout()
        self.button1 = QPushButton("BTN1")
        self.button2 = QPushButton("BTN2")
        button_layout.addWidget(self.button1)
        button_layout.addWidget(self.button2)
        #Yatay buton layoutunu ana dikey layouta ekliyoruz
        main_layout.addLayout(button_layout)
        central_widget.setLayout(main_layout)




app = QApplication(sys.argv)
window = LayoutExample()
window.show()
sys.exit(app.exec_())