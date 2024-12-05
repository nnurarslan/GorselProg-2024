import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QWidget, QTextEdit, QVBoxLayout, QSpinBox, QRadioButton, QCheckBox, QLabel, QLineEdit, QComboBox, QSlider

class MultipleWidgetExample2(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Multiple widgets")
        self.setGeometry(100,100,400,300)
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        layout = QVBoxLayout()
        self.lineEdit = QLineEdit(self)
        self.lineEdit.setPlaceholderText("Adınızı girin..")
        layout.addWidget(self.lineEdit)
        self.cb = QCheckBox("Abonelik Onayı")
        layout.addWidget(self.cb)
        self.combobox = QComboBox(self)
        self.combobox.addItems(["istanbul","ankara","kütahya"])
        layout.addWidget(self.combobox)
        self.result_label = QLabel("SONUÇ BURADA GÖZÜKECEK")
        layout.addWidget(self.result_label)
        self.btn = QPushButton("GÖSTER")
        self.btn.clicked.connect(self.on_button_click)
        layout.addWidget(self.btn)
        central_widget.setLayout(layout)

    def on_button_click(self):
        name = self.lineEdit.text()
        is_checked = self.cb.isChecked()
        combo_selection = self.combobox.currentText()
        result = f"ad {name}\n abonelik: {is_checked}"
        self.result_label.setText(result)

app = QApplication(sys.argv)
window = MultipleWidgetExample2()
window.show()
sys.exit(app.exec_())