import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QWidget, QTextEdit, QVBoxLayout, QSpinBox, QRadioButton, QCheckBox, QLabel, QLineEdit, QComboBox, QSlider

class MultipleWidgetExample(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Multiple widgets")
        self.setGeometry(100,100,600,500)
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        layout = QVBoxLayout()
        self.label = QLabel("Bir metin yazın:")
        layout.addWidget(self.label)
        self.line_edit = QLineEdit(self)
        layout.addWidget(self.line_edit)
        self.button = QPushButton("Butona tıkla")
        self.button.clicked.connect(self.on_button_click)
        layout.addWidget(self.button)

        self.checkbox = QCheckBox("Onay Kutusu")
        layout.addWidget(self.checkbox)

        self.combobox = QComboBox(self)
        self.combobox.addItems(["Python","C++","Java"])
        layout.addWidget(self.combobox)

        self.slider = QSlider(self)
        self.slider.setOrientation(1)
        self.slider.setRange(0,100)
        layout.addWidget(self.slider)

        self.rb1 = QRadioButton("Seçenek 1")
        self.rb2 = QRadioButton("Seçenek 2")
        layout.addWidget(self.rb1)
        layout.addWidget(self.rb2)

        self.spin_box = QSpinBox(self)
        self.spin_box.setRange(0,100)
        layout.addWidget(self.spin_box)

        self.text_edit = QTextEdit(self)
        layout.addWidget(self.text_edit)

        central_widget.setLayout(layout)
    def on_button_click(self):
        input_text = self.line_edit.text()
        print(input_text)
        checkbox_state = "işaretlendi" if self.checkbox.isChecked() else "işaretlenmedi"
        selected_lang = self.combobox.currentText()
        slider_value = self.slider.value()
        radio_selection = "Seçenek 1" if self.rb1.isChecked() else "Seçenek 2"
        spin_value = self.spin_box.value()
        self.label.setText(f"Metin : {input_text}\n Onay kutusu: {checkbox_state}\n"
                           f"Seçilen dil: {selected_lang}\n Slider değeri:{slider_value}\n"
                           f"Radyo buton seçimi: {radio_selection}\n"
                           f"SpinBox değeri {spin_value}")

app = QApplication(sys.argv)
window = MultipleWidgetExample()
window.show()
sys.exit(app.exec_())