from PyQt5.QtWidgets import QMainWindow, QApplication, QTableWidgetItem, QHeaderView, QPushButton, QLabel, QMessageBox
from PyQt5 import uic
from sqlite3 import connect
from sys import argv, exit


class AddEdit(QMainWindow):
    def __init__(self, cur, *args):
        super().__init__()
        self.args = args
        self.cur = cur
        uic.loadUi('addEditCoffeeForm.ui', self)
        self.add_edit.clicked.connect(self.add_edit_act)
        self.fill_ui()

    def add_edit_act(self):
        try:
            if self.args:
                self.cur.execute(f'UPDATE main'
                                 f' SET name="{self.name_sort.text()}",'
                                 f' power={self.power.text()},'
                                 f' ground={self.ground.text()},'
                                 f' description="{self.desc.text()}",'
                                 f' price={self.price.text()},'
                                 f' volume={self.volume.text()}'
                                 f' WHERE id={self.args[0]}').fetchall()
        except Exception as e:
            QMessageBox.about(self, f'Error', f'{e}')

    def fill_ui(self):
        if self.args:
            # print(self.args)
            self.name_sort.setText(self.args[1])
            self.power.setText(self.args[2])
            self.ground.setText(self.args[3])
            self.desc.setText(self.args[4])
            self.price.setText(self.args[5])
            self.volume.setText(self.args[6])


class Main(QMainWindow):
    def __init__(self):
        super().__init__()

        self.draw_circle = 0

        self.con = 0
        self.cur = 0
        self.a = 0
        uic.loadUi('main.ui', self)
        self.load_table()
        self.connect_ui()

    def connect_ui(self):
        self.b_add.clicked.connect(self.b_add_act)
        self.b_edit.clicked.connect(self.b_edit_act)

    def b_add_act(self):
        self.a = AddEdit(cur=self.cur)
        self.a.show()

    def b_edit_act(self):
        # print([self.main_table.item(self.main_table.currentRow(), i).text() for i in range(7)])
        self.a = AddEdit(self.cur, *[self.main_table.item(self.main_table.currentRow(), i).text() for i in range(7)])
        self.a.show()

    def load_table(self):
        self.con = connect("coffee.sqlite")
        self.cur = self.con.cursor()
        some = self.cur.execute("SELECT * FROM main").fetchall()
        self.main_table.setRowCount(0)
        self.main_table.setColumnCount(len(some[0]))
        self.main_table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.main_table.setHorizontalHeaderLabels([description[0] for description in self.cur.description])
        for i, row in enumerate(some):
            self.main_table.setRowCount(self.main_table.rowCount() + 1)
            for j, elem in enumerate(row):
                self.main_table.setItem(i, j, QTableWidgetItem(str(elem)))


if __name__ == "__main__":
    app = QApplication(argv)
    ex = Main()
    ex.show()
    exit(app.exec_())