from PyQt5.QtWidgets import QMainWindow, QApplication,  QTableWidgetItem, QHeaderView
from PyQt5 import uic
from sqlite3 import connect
from sys import argv, exit


class Main(QMainWindow):
    def __init__(self):
        super().__init__()

        self.draw_circle = 0

        uic.loadUi('main.ui', self)
        self.load_table()

    def load_table(self):
        con = connect("coffee.sqlite")
        cur = con.cursor()
        some = cur.execute("SELECT * FROM main").fetchall()
        self.main_table.setRowCount(0)
        self.main_table.setColumnCount(len(some[0]))
        self.main_table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.main_table.setHorizontalHeaderLabels([description[0] for description in cur.description])
        for i, row in enumerate(some):
            self.main_table.setRowCount(self.main_table.rowCount() + 1)
            for j, elem in enumerate(row):
                self.main_table.setItem(i, j, QTableWidgetItem(str(elem)))


if __name__ == "__main__":
    app = QApplication(argv)
    ex = Main()
    ex.show()
    exit(app.exec_())