# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'pytubeviewvStdnY.ui'
##
## Created by: Qt User Interface Compiler version 6.5.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QHeaderView, QLabel,
    QMainWindow, QMenu, QMenuBar, QSizePolicy,
    QSlider, QStatusBar, QTabWidget, QTableWidget,
    QTableWidgetItem, QTextEdit, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1052, 615)
        self.loadImageMenuItem = QAction(MainWindow)
        self.loadImageMenuItem.setObjectName(u"loadImageMenuItem")
        self.saveImageMenuItem = QAction(MainWindow)
        self.saveImageMenuItem.setObjectName(u"saveImageMenuItem")
        self.saveOverlayMenuItem = QAction(MainWindow)
        self.saveOverlayMenuItem.setObjectName(u"saveOverlayMenuItem")
        self.saveModelsMenuItem = QAction(MainWindow)
        self.saveModelsMenuItem.setObjectName(u"saveModelsMenuItem")
        self.loadSceneMenuItem = QAction(MainWindow)
        self.loadSceneMenuItem.setObjectName(u"loadSceneMenuItem")
        self.saveSceneMenuItem = QAction(MainWindow)
        self.saveSceneMenuItem.setObjectName(u"saveSceneMenuItem")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setGeometry(QRect(220, 400, 531, 171))
        self.tabVisualization = QWidget()
        self.tabVisualization.setObjectName(u"tabVisualization")
        self.verticalLayoutWidget_3 = QWidget(self.tabVisualization)
        self.verticalLayoutWidget_3.setObjectName(u"verticalLayoutWidget_3")
        self.verticalLayoutWidget_3.setGeometry(QRect(9, 9, 501, 131))
        self.tabVisualizationLayout = QVBoxLayout(self.verticalLayoutWidget_3)
        self.tabVisualizationLayout.setObjectName(u"tabVisualizationLayout")
        self.tabVisualizationLayout.setContentsMargins(0, 0, 0, 0)
        self.tabWidget.addTab(self.tabVisualization, "")
        self.tabPreprocess = QWidget()
        self.tabPreprocess.setObjectName(u"tabPreprocess")
        self.verticalLayoutWidget_7 = QWidget(self.tabPreprocess)
        self.verticalLayoutWidget_7.setObjectName(u"verticalLayoutWidget_7")
        self.verticalLayoutWidget_7.setGeometry(QRect(10, 10, 511, 121))
        self.tabPreProcessLayout = QVBoxLayout(self.verticalLayoutWidget_7)
        self.tabPreProcessLayout.setObjectName(u"tabPreProcessLayout")
        self.tabPreProcessLayout.setContentsMargins(0, 0, 0, 0)
        self.tabWidget.addTab(self.tabPreprocess, "")
        self.tabLungAI = QWidget()
        self.tabLungAI.setObjectName(u"tabLungAI")
        self.verticalLayoutWidget_6 = QWidget(self.tabLungAI)
        self.verticalLayoutWidget_6.setObjectName(u"verticalLayoutWidget_6")
        self.verticalLayoutWidget_6.setGeometry(QRect(10, 0, 511, 121))
        self.tabLungAILayout = QVBoxLayout(self.verticalLayoutWidget_6)
        self.tabLungAILayout.setObjectName(u"tabLungAILayout")
        self.tabLungAILayout.setContentsMargins(0, 0, 0, 0)
        self.tabWidget.addTab(self.tabLungAI, "")
        self.objectComboBox = QComboBox(self.centralwidget)
        self.objectComboBox.setObjectName(u"objectComboBox")
        self.objectComboBox.setGeometry(QRect(60, 407, 141, 26))
        self.objectLabel = QLabel(self.centralwidget)
        self.objectLabel.setObjectName(u"objectLabel")
        self.objectLabel.setGeometry(QRect(10, 407, 49, 20))
        self.objectInfoLabel = QLabel(self.centralwidget)
        self.objectInfoLabel.setObjectName(u"objectInfoLabel")
        self.objectInfoLabel.setGeometry(QRect(10, 520, 49, 16))
        self.objectColorLabel = QLabel(self.centralwidget)
        self.objectColorLabel.setObjectName(u"objectColorLabel")
        self.objectColorLabel.setGeometry(QRect(10, 439, 49, 24))
        self.objectColorComboBox = QComboBox(self.centralwidget)
        self.objectColorComboBox.setObjectName(u"objectColorComboBox")
        self.objectColorComboBox.setGeometry(QRect(60, 437, 141, 26))
        self.objectFormLabel = QLabel(self.centralwidget)
        self.objectFormLabel.setObjectName(u"objectFormLabel")
        self.objectFormLabel.setGeometry(QRect(10, 490, 49, 20))
        self.objectOpacityLabel = QLabel(self.centralwidget)
        self.objectOpacityLabel.setObjectName(u"objectOpacityLabel")
        self.objectOpacityLabel.setGeometry(QRect(10, 466, 49, 20))
        self.objectOpacitySlider = QSlider(self.centralwidget)
        self.objectOpacitySlider.setObjectName(u"objectOpacitySlider")
        self.objectOpacitySlider.setGeometry(QRect(60, 467, 141, 20))
        self.objectOpacitySlider.setOrientation(Qt.Horizontal)
        self.objectFormComboBox = QComboBox(self.centralwidget)
        self.objectFormComboBox.setObjectName(u"objectFormComboBox")
        self.objectFormComboBox.setGeometry(QRect(60, 487, 141, 26))
        self.objectInfoText = QTextEdit(self.centralwidget)
        self.objectInfoText.setObjectName(u"objectInfoText")
        self.objectInfoText.setGeometry(QRect(60, 520, 141, 51))
        font = QFont()
        font.setPointSize(7)
        self.objectInfoText.setFont(font)
        self.objectInfoText.setMouseTracking(False)
        self.objectInfoText.setAcceptDrops(False)
        self.objectInfoText.setUndoRedoEnabled(False)
        self.objectInfoText.setReadOnly(True)
        self.verticalLayoutWidget_2 = QWidget(self.centralwidget)
        self.verticalLayoutWidget_2.setObjectName(u"verticalLayoutWidget_2")
        self.verticalLayoutWidget_2.setGeometry(QRect(400, 10, 351, 351))
        self.tabView3DLayout = QVBoxLayout(self.verticalLayoutWidget_2)
        self.tabView3DLayout.setObjectName(u"tabView3DLayout")
        self.tabView3DLayout.setContentsMargins(0, 0, 0, 0)
        self.tableWidget = QTableWidget(self.centralwidget)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setGeometry(QRect(760, 10, 281, 221))
        self.verticalLayoutWidget_4 = QWidget(self.centralwidget)
        self.verticalLayoutWidget_4.setObjectName(u"verticalLayoutWidget_4")
        self.verticalLayoutWidget_4.setGeometry(QRect(760, 240, 281, 121))
        self.tabScreenCaptureLayout = QVBoxLayout(self.verticalLayoutWidget_4)
        self.tabScreenCaptureLayout.setObjectName(u"tabScreenCaptureLayout")
        self.tabScreenCaptureLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayoutWidget_5 = QWidget(self.centralwidget)
        self.verticalLayoutWidget_5.setObjectName(u"verticalLayoutWidget_5")
        self.verticalLayoutWidget_5.setGeometry(QRect(760, 370, 281, 201))
        self.tabChatLayout = QVBoxLayout(self.verticalLayoutWidget_5)
        self.tabChatLayout.setObjectName(u"tabChatLayout")
        self.tabChatLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayoutWidget_8 = QWidget(self.centralwidget)
        self.verticalLayoutWidget_8.setObjectName(u"verticalLayoutWidget_8")
        self.verticalLayoutWidget_8.setGeometry(QRect(10, 10, 391, 351))
        self.tabView2DLayout = QVBoxLayout(self.verticalLayoutWidget_8)
        self.tabView2DLayout.setObjectName(u"tabView2DLayout")
        self.tabView2DLayout.setContentsMargins(0, 0, 0, 0)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1052, 22))
        self.menuMIDAS_Qt = QMenu(self.menubar)
        self.menuMIDAS_Qt.setObjectName(u"menuMIDAS_Qt")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuMIDAS_Qt.menuAction())
        self.menuMIDAS_Qt.addAction(self.loadSceneMenuItem)
        self.menuMIDAS_Qt.addAction(self.loadImageMenuItem)
        self.menuMIDAS_Qt.addSeparator()
        self.menuMIDAS_Qt.addAction(self.saveSceneMenuItem)
        self.menuMIDAS_Qt.addAction(self.saveImageMenuItem)
        self.menuMIDAS_Qt.addSeparator()
        self.menuMIDAS_Qt.addAction(self.saveOverlayMenuItem)
        self.menuMIDAS_Qt.addAction(self.saveModelsMenuItem)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(2)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.loadImageMenuItem.setText(QCoreApplication.translate("MainWindow", u"Load Image", None))
        self.saveImageMenuItem.setText(QCoreApplication.translate("MainWindow", u"Save Image", None))
        self.saveOverlayMenuItem.setText(QCoreApplication.translate("MainWindow", u"Save Overlay", None))
        self.saveModelsMenuItem.setText(QCoreApplication.translate("MainWindow", u"Save Models", None))
        self.loadSceneMenuItem.setText(QCoreApplication.translate("MainWindow", u"Load Scene", None))
        self.saveSceneMenuItem.setText(QCoreApplication.translate("MainWindow", u"Save Scene", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabVisualization), QCoreApplication.translate("MainWindow", u"Visualization", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabPreprocess), QCoreApplication.translate("MainWindow", u"PreProcess", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabLungAI), QCoreApplication.translate("MainWindow", u"Lung AI", None))
#if QT_CONFIG(accessibility)
        self.objectComboBox.setAccessibleName("")
#endif // QT_CONFIG(accessibility)
        self.objectComboBox.setCurrentText("")
        self.objectLabel.setText(QCoreApplication.translate("MainWindow", u"Object:", None))
        self.objectInfoLabel.setText(QCoreApplication.translate("MainWindow", u"Info:", None))
        self.objectColorLabel.setText(QCoreApplication.translate("MainWindow", u"Color:", None))
#if QT_CONFIG(accessibility)
        self.objectColorComboBox.setAccessibleName("")
#endif // QT_CONFIG(accessibility)
        self.objectColorComboBox.setCurrentText("")
        self.objectFormLabel.setText(QCoreApplication.translate("MainWindow", u"Form:", None))
        self.objectOpacityLabel.setText(QCoreApplication.translate("MainWindow", u"Opacity:", None))
#if QT_CONFIG(accessibility)
        self.objectFormComboBox.setAccessibleName("")
#endif // QT_CONFIG(accessibility)
        self.objectFormComboBox.setCurrentText("")
        self.menuMIDAS_Qt.setTitle(QCoreApplication.translate("MainWindow", u"File", None))
    # retranslateUi

