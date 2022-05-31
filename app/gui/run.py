import sys
from PyQt5 import QtWidgets

from app.gui.mainwindow import MainWindow

def run():
    app = QtWidgets.QApplication(sys.argv)
    mainWindow = MainWindow()
    mainWindow.show()
    sys.exit(app.exec_())