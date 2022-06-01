from PyQt5.QtWidgets import (
    QTableWidget, QTableWidgetItem, QVBoxLayout, QPushButton,
    QLineEdit, QHBoxLayout
)
from app.db.sqlite import SQLite


# data like {
#   'namecolumn': [1,2,3,4],
#   etc
# }
class TableView(QTableWidget):
    def __init__(self, table_name, height=0, length=0):
        self.table_name = table_name
        self.height = height
        self.length = length
        self.data = self.getData()
        QTableWidget.__init__(self, self.height, self.length)
        self.setData()
        self.resizeColumnsToContents()
        self.resizeRowsToContents()

    def getData(self):
        data = {}
        with SQLite() as cur:
            cur.execute(f'select * from {self.table_name}')
            col_names = [tup[0] for tup in cur.description]
            rows = cur.fetchall()
            for i in range(len(col_names)):
                data[col_names[i]] = [row[i] for row in rows]
                self.height = len(data[col_names[i]])
                self.length = len(col_names)
            return data

    def setData(self):
        horHeaders = []
        for n, key in enumerate(self.data.keys()):
            horHeaders.append(key)
            for m, item in enumerate(self.data[key]):
                newItem = QTableWidgetItem(item)
                self.setItem(m, n, newItem)
        self.setHorizontalHeaderLabels(horHeaders)


class AdminGUI(QVBoxLayout):
    def __init__(self, table_name='customers'):
        QVBoxLayout.__init__(self)
        self.table_name = table_name
        self.initUI()

    def initUI(self):
        refreshTableButton = QPushButton('Refresh Table')
        table = TableView(self.table_name)
        line_add = LineAddGUI(self.table_name)
        line_remove = LineRemoveGUI(self.table_name)
        self.addWidget(refreshTableButton)
        self.addWidget(table)
        self.addLayout(line_add)
        self.addLayout(line_remove)


class LineAddGUI(QHBoxLayout):
    def __init__(self, table_name):
        QHBoxLayout.__init__(self)
        self.table_name = table_name
        self.lines_num = self.get_lines_num()
        self.lines = [QLineEdit() for i in range(self.lines_num)]
        self.initUI()

    def get_lines_num(self):
        with SQLite() as cur:
            cur.execute(f'select * from {self.table_name}')
            col_names = [tup[0] for tup in cur.description]
            return len(col_names) - 1

    def initUI(self):
        for line in self.lines:
            self.addWidget(line)

        add_button = QPushButton('Add line')
        add_button.clicked.connect(self.clickAdd)
        self.addWidget(add_button)

    def clickAdd(self):
        text = ' '.join(line.text() for line in self.lines)
        for line in self.lines:
            line.clear()

        print(text)


class LineRemoveGUI(QHBoxLayout):
    def __init__(self, table_name):
        QHBoxLayout.__init__(self)
        self.table_name = table_name
        self.line_id = QLineEdit()
        self.initUI()

    def initUI(self):
        self.addWidget(self.line_id)

        remove_button = QPushButton('Remove by id')
        remove_button.clicked.connect(self.clickRemove)
        self.addWidget(remove_button)

    def clickRemove(self):
        print(self.line_id.text())
        self.line_id.clear()