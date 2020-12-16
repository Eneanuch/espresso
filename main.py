from PyQt5.QtWidgets import QMainWindow, QApplication, QTableWidgetItem, QHeaderView, QPushButton, QLabel, QMessageBox
from PyQt5 import uic
from sqlite3 import connect
from sys import argv, exit
from PyQt5 import QtCore, QtGui, QtWidgets


class AddEditDes(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(364, 265)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.add_edit = QtWidgets.QPushButton(self.centralwidget)
        self.add_edit.setGeometry(QtCore.QRect(10, 190, 75, 23))
        self.add_edit.setObjectName("add_edit")
        self.name_sort = QtWidgets.QLineEdit(self.centralwidget)
        self.name_sort.setGeometry(QtCore.QRect(10, 10, 113, 20))
        self.name_sort.setObjectName("name_sort")
        self.power = QtWidgets.QLineEdit(self.centralwidget)
        self.power.setGeometry(QtCore.QRect(10, 40, 113, 20))
        self.power.setObjectName("power")
        self.ground = QtWidgets.QLineEdit(self.centralwidget)
        self.ground.setGeometry(QtCore.QRect(10, 70, 113, 20))
        self.ground.setObjectName("ground")
        self.desc = QtWidgets.QLineEdit(self.centralwidget)
        self.desc.setGeometry(QtCore.QRect(10, 100, 113, 20))
        self.desc.setObjectName("desc")
        self.price = QtWidgets.QLineEdit(self.centralwidget)
        self.price.setGeometry(QtCore.QRect(10, 130, 113, 20))
        self.price.setObjectName("price")
        self.volume = QtWidgets.QLineEdit(self.centralwidget)
        self.volume.setGeometry(QtCore.QRect(10, 160, 113, 20))
        self.volume.setObjectName("volume")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(140, 10, 171, 16))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(140, 40, 101, 16))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(140, 70, 151, 16))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(140, 100, 111, 16))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(140, 130, 101, 16))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(140, 160, 111, 16))
        self.label_6.setObjectName("label_6")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 364, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Add\\Edit"))
        self.add_edit.setText(_translate("MainWindow", "Add/Edit"))
        self.label.setText(_translate("MainWindow", "Название сорта"))
        self.label_2.setText(_translate("MainWindow", "Степень обжарки"))
        self.label_3.setText(_translate("MainWindow", "(0) Молотый/(1) в зернах"))
        self.label_4.setText(_translate("MainWindow", "Описание"))
        self.label_5.setText(_translate("MainWindow", "Цена"))
        self.label_6.setText(_translate("MainWindow", "Обьем упаковки"))


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 599)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.main_table = QtWidgets.QTableWidget(self.centralwidget)
        self.main_table.setGeometry(QtCore.QRect(10, 10, 781, 511))
        self.main_table.setObjectName("main_table")
        self.main_table.setColumnCount(0)
        self.main_table.setRowCount(0)
        self.b_add = QtWidgets.QPushButton(self.centralwidget)
        self.b_add.setGeometry(QtCore.QRect(10, 530, 75, 23))
        self.b_add.setObjectName("b_add")
        self.b_edit = QtWidgets.QPushButton(self.centralwidget)
        self.b_edit.setGeometry(QtCore.QRect(90, 530, 75, 23))
        self.b_edit.setObjectName("b_edit")
        self.l_status = QtWidgets.QLabel(self.centralwidget)
        self.l_status.setGeometry(QtCore.QRect(230, 530, 561, 20))
        self.l_status.setObjectName("l_status")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Espresso"))
        self.b_add.setText(_translate("MainWindow", "Add"))
        self.b_edit.setText(_translate("MainWindow", "Edit"))
        self.l_status.setText(_translate("MainWindow", "OK"))


class AddEdit(QMainWindow, AddEditDes):
    def __init__(self, win, cur, con, *args):
        super().__init__()
        self.args = args
        self.cur = cur
        self.con = con
        self.a = 0
        self.setupUi(self)
        self.add_edit.clicked.connect(self.add_edit_act)
        self.win = win
        self.fill_ui()

    def add_edit_act(self):
        try:
            if self.args:
                # print(*self.cur.execute("SELECT * FROM main WHERE id=1"))
                self.a = self.cur.execute(f'UPDATE main'
                                          f" SET name='{self.name_sort.text()}',"
                                          f' power={self.power.text()},'
                                          f' ground={self.ground.text()},'
                                          f" description='{self.desc.text()}',"
                                          f' price={self.price.text()},'
                                          f' volume={self.volume.text()}'
                                          f' WHERE id={self.args[0]}').fetchall()
                # print(*self.cur.execute("SELECT * FROM main WHERE id=1"))
            else:
                self.a = self.cur.execute(f'INSERT INTO main '
                                          f'(name, power, ground, description, price, volume)'
                                          f' VALUES("{self.name_sort.text()}", {self.power.text()},'
                                          f' {self.ground.text()}, "{self.desc.text()}",'
                                          f' {self.price.text()}, {self.volume.text()});')
        except Exception as e:
            QMessageBox.about(self, f'Error', f'{e}')
        self.con.commit()
        self.close()
        self.win.load_table()

    def fill_ui(self):
        try:
            if self.args:
                # print(self.args)
                self.name_sort.setText(self.args[1])
                self.power.setText(self.args[2])
                self.ground.setText(self.args[3])
                self.desc.setText(self.args[4])
                self.price.setText(self.args[5])
                self.volume.setText(self.args[6])
        except Exception as e:
            QMessageBox.about(self, f'Error', f'{e}')


class Main(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()

        self.draw_circle = 0

        self.con = 0
        self.cur = 0
        self.a = 0
        self.setupUi(self)
        self.load_table()
        self.connect_ui()

    def connect_ui(self):
        self.b_add.clicked.connect(self.b_add_act)
        self.b_edit.clicked.connect(self.b_edit_act)

    def b_add_act(self):
        self.a = AddEdit(self, cur=self.cur, con=self.con)
        self.a.show()

    def b_edit_act(self):
        # print([self.main_table.item(self.main_table.currentRow(), i).text() for i in range(7)])
        self.a = AddEdit(self, self.cur, self.con, *[self.main_table.item(self.main_table.currentRow(), i).text() for i in range(7)])
        self.a.show()

    def load_table(self):
        self.con = connect("data/coffee.sqlite")
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
