import sys
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QWidget, QPushButton, QAction, QGridLayout
from PyQt5.QtCore import QSize
from PyQt5.QtGui import QIcon

from app.gui.menubar import Menu
from app.gui.admin import TableView
from app.gui.admin import AdminGUI


class MainWindow(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        layout = QGridLayout()
        self.setLayout(layout)

        self.MIN_WIDTH = 400
        self.MIN_HEIGHT = 200
        self.setMinimumSize(QSize(self.MIN_WIDTH, self.MIN_HEIGHT))
        self.setWindowTitle('Database Converter-Browser')

        menubar = Menu.bar(self)
        layout.addWidget(menubar, 0, 0)

        adminGUI = AdminGUI()
        layout.addLayout(adminGUI, 1, 0)
