from PyQt5.QtWidgets import QMenuBar, QAction, QWidget, QGridLayout


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
        help_menu.addAction()

        return menubar


class Action:
    @staticmethod
    def about():


    @staticmethod
    def quit(parent: QWidget):
        action = QAction('Exit', parent)
        action.setShortcut('Ctrl+Q')
        action.setStatusTip('Exit program')
        action.triggered.connect(parent.close)
        return action

    @staticmethod
    def customers(parent: QWidget):
        action = QAction('Customers', parent)
        action.setShortcut('Alt+C')
        action.setStatusTip('Open Customers Menu')
        return action


class AboutWindow(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        layout = QGridLayout()
        self.setLayout(layout)

        self.setWindowTitle('About')