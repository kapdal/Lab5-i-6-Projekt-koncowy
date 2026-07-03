import sys
import threading
import sys, os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from PyQt5.QtWidgets import (
    QApplication, QWidget, QPushButton, QFileDialog, QLabel, QVBoxLayout
)
from converter import load_file, save_file

class ConverterUI(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Konwerter XML/JSON/YAML")
        self.resize(400, 200)

        layout = QVBoxLayout()

        self.label = QLabel("Wybierz plik wejściowy i wyjściowy")
        layout.addWidget(self.label)

        self.btn_in = QPushButton("Plik wejściowy")
        self.btn_in.clicked.connect(self.load_input)
        layout.addWidget(self.btn_in)

        self.btn_out = QPushButton("Plik wyjściowy")
        self.btn_out.clicked.connect(self.load_output)
        layout.addWidget(self.btn_out)

        self.btn_convert = QPushButton("Konwertuj")
        self.btn_convert.clicked.connect(self.convert_async)
        layout.addWidget(self.btn_convert)

        self.setLayout(layout)

        self.input_path = None
        self.output_path = None

    def load_input(self):
        self.input_path, _ = QFileDialog.getOpenFileName(self, "Wybierz plik wejściowy")
        if self.input_path:
            self.label.setText(f"Wybrano wejściowy: {self.input_path}")

    def load_output(self):
        self.output_path, _ = QFileDialog.getSaveFileName(self, "Wybierz plik wyjściowy")
        if self.output_path:
            self.label.setText(f"Wybrano wyjściowy: {self.output_path}")

    def convert_async(self):
        thread = threading.Thread(target=self.convert)
        thread.start()

    def convert(self):
        if not self.input_path or not self.output_path:
            self.label.setText("Błąd: wybierz plik wejściowy i wyjściowy")
            return
        try:
            data = load_file(self.input_path)
            save_file(self.output_path, data)
            self.label.setText("Konwersja zakończona sukcesem.")
        except Exception as e:
            self.label.setText(f"Błąd: {e}")

def main():
    app = QApplication(sys.argv)
    window = ConverterUI()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()