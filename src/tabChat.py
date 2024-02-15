from PySide6.QtCore import Qt
from PySide6.QtWidgets import QWidget

from ui_tabChat import Ui_tabChatWidget


class TabChatWidget(QWidget, Ui_tabChatWidget):
    def __init__(self, gui, state, parent=None):
        super().__init__(parent)
        self.setupUi(self)

        self.gui = gui
        self.state = state

        self.chatGoButton.clicked.connect(
            self.go
        )

    def go(self):
        print("click")