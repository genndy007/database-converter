from PyQt5.QtWidgets import (
    QMenuBar, QAction, QWidget, QGridLayout, QLabel,
)

from app.gui.admin import AdminGUI
from app.db.migrate import migrate_sqlite_to_pg, migrate_pg_to_mysql

class Menu:
    @staticmethod
    def bar(parent: QWidget):
        menubar = QMenuBar()
        file_menu = menubar.addMenu('File')
        file_menu.addAction(Action.quit(parent))

        table_menu = menubar.addMenu('Table')
        table_menu.addAction('Customers')
        table_menu.addAction('Suppliers')
        table_menu.addAction('Hardwares')
        table_menu.addAction('Purchases')

        migrate_menu = menubar.addMenu('Migrate')
        migrate_menu.addAction(Action.sqlite_to_pg(parent))
        migrate_menu.addAction(Action.pg_to_mysql(parent))

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
    def sqlite_to_pg(parent):
        action = QAction('SQLite to PostgreSQL', parent)
        action.triggered.connect(migrate_sqlite_to_pg)
        return action

    @staticmethod
    def pg_to_mysql(parent):
        action = QAction('PostgreSQL to MySQL', parent)
        action.triggered.connect(migrate_pg_to_mysql)
        return action



class AboutWindow(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        layout = QGridLayout()
        self.setLayout(layout)

        self.setWindowTitle('About')
        about_text = 'This program is written by Kochev Hennadii in 2022'
        layout.addWidget(QLabel(about_text))