from PyQt5.QtWidgets import (
    QMenuBar, QAction, QWidget, QGridLayout, QLabel,
)

from app.gui.admin import AdminGUI


class Menu:
    @staticmethod
    def bar(parent: QWidget):
        menubar = QMenuBar()
        file_menu = menubar.addMenu('File')
        file_menu.addAction(Action.quit(parent))

        table_menu = menubar.addMenu('Table')
        table_menu.addAction(Action.customers(parent))
        table_menu.addAction('Suppliers')
        table_menu.addAction('Hardwares')
        table_menu.addAction('Purchases')

        help_menu = menubar.addMenu('Help')
        help_menu.addAction(Action.about(parent))

        return menubar


class Action:
    @staticmethod
    def about(parent: QWidget):
        action = QAction('About', parent)
        action.setShortcut('Shift+F1')
        action.setStatusTip('About program')
        def show_about():
            parent.aboutWindow = AboutWindow()
            parent.aboutWindow.show()

        action.triggered.connect(show_about)
        return action


    @staticmethod
    def quit(parent: QWidget):
        action = QAction('Exit', parent)
        action.setShortcut('Ctrl+Q')
        action.setStatusTip('Exit program')
        action.triggered.connect(parent.close)
        return action

    @staticmethod
    def customers(parent):
        action = QAction('Customers', parent)
        # action.setShortcut('Alt+C')
        # action.setStatusTip('Open Customers Menu')
        # def add_layout():
        #     parent.layout.addLayout(AdminGUI('suppliers'), 1, 0)
        # action.triggered.connect(add_layout)
        return action


class AboutWindow(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        layout = QGridLayout()
        self.setLayout(layout)

        self.setWindowTitle('About')
        about_text = 'This program is written by Kochev Hennadii in 2022'
        layout.addWidget(QLabel(about_text))