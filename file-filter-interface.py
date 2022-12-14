import os
import pathlib
import shutil
import sys

from PySide6 import QtWidgets
from PySide6.QtCore import QTimer

class Program_file_filter(QtWidgets.QWidget):

    def __init__(self):
        super(Program_file_filter, self).__init__()
        self.main_function()

    def main_function(self):
        self.interface()
        self.reload()
        self.button.clicked.connect(lambda: self.list.clear())

    def interface(self):
        self.list = QtWidgets.QListWidget()
        self.button = QtWidgets.QPushButton()
        self.button.setText("Очистить лог")

        self.vbox = QtWidgets.QVBoxLayout()
        self.vbox.addWidget(self.list)
        self.vbox.addWidget(self.button)

        self.setLayout(self.vbox)

    def reload(self):
        self.timer = QTimer()
        self.timer.timeout.connect(self.filter_logic)
        self.timer.start(10000)

    def filter_logic(self):
        directory = r"C:\Python project\PySide example\file filter interface"

        folder = [r"C:\Python project\PySide example\file filter interface\Изображения",
                  r"C:\Python project\PySide example\file filter interface\Документы",
                  r"C:\Python project\PySide example\file filter interface\Музыка"
                  ]

        file_types = [(".jpg,", ".png"),
                      (".docx", ".pdf"),
                      (".mp3", ".wav")
                      ]

        for file in os.listdir(directory):
            file_name = os.path.splitext(file)[0]

            for index, file_extensions in enumerate(file_types):
                if pathlib.Path(file).suffix.lower() in file_extensions:
                    if file in os.listdir(folder[index]):
                        self.list.addItem(f"Файл {file_name} уже есть в папке {os.path.basename(folder[index])}")
                    else:
                        shutil.move(src=rf"{directory}\{file}", dst=folder[index])
                        self.list.addItem(f"Файл {file_name} перемещен в папку {os.path.basename(folder[index])}")
        self.list.scrollToBottom()

def application():
    app = QtWidgets.QApplication()
    window = Program_file_filter()
    window.setWindowTitle("Сортировщик файлов")
    window.resize(400, 200)
    window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    application()
