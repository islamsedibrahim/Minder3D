from PySide6.QtWidgets import (
    QWidget,
    QTableWidget,
    QTableWidgetItem,
    QHeaderView,
)

from sovUtils import time_and_log

from ui_sovInfoTablePanelWidget import Ui_InfoTablePanelWidget


class InfoTablePanelWidget(QWidget, Ui_InfoTablePanelWidget):
    def __init__(self, gui, state, parent=None):
        super().__init__(parent)
        self.setupUi(self)

        self.gui = gui
        self.state = state

        self.infoTableWidget.setRowCount(3)
        self.infoTableWidget.setColumnCount(2)
        self.infoTableWidget.setItem(0, 0, QTableWidgetItem("Pixel Coordinate"))
        self.infoTableWidget.setItem(1, 0, QTableWidgetItem("  Image Value"))
        self.infoTableWidget.setItem(2, 0, QTableWidgetItem("  Overlay Value"))
        self.infoTableWidget.setEditTriggers(QTableWidget.NoEditTriggers)
        self.infoTableWidget.setSelectionMode(QTableWidget.NoSelection)
        self.infoTableWidget.setShowGrid(True)
        #self.infoTableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeToContents)
        #self.infoTableWidget.verticalHeader().setSectionResizeMode(QHeaderView.ResizeToContents)
        self.infoTableWidget.verticalHeader().hide()

    @time_and_log
    def update_image(self):
        pass

    @time_and_log
    def update_pixel(self):
        pos_str = ', '.join([f"{x:0.1f}" for x in self.state.current_pixel])
        self.infoTableWidget.setItem(0, 1, QTableWidgetItem(pos_str))
        self.infoTableWidget.setItem(1, 1, QTableWidgetItem("0"))
        self.infoTableWidget.setItem(2, 1, QTableWidgetItem("0"))
