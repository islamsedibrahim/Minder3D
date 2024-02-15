import sys

from PySide6.QtCore import Qt
from PySide6.QtWidgets import QApplication

from ptvWindow import PTVWindow


if __name__ == "__main__":
    app = QApplication(sys.argv)

    pytubeview = PTVWindow()

    if len(sys.argv)>1:
        pytubeview.load_image(sys.argv[1])

    sys.exit(app.exec())
