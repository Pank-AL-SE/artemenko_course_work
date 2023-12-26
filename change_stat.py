from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtWidgets import * 
from PyQt5.QtGui import * 
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidget, QTableWidgetItem
from PyQt5.QtCore import Qt,QTimer
import sys
import os
import openpyxl
import sqlite3

class chenge_stat(QMainWindow):
    def __init__(self):
 
        super().__init__()
        

        self.setWindowTitle("Добавление на склад")
        self.setFixedSize(300,150)

        self.add_post = QLineEdit(self)
        self.add_post.move(0, 0)
        self.add_post.resize(300,50)
        self.add_post.setPlaceholderText("Номер заказа")
       

        self.combo_box = QComboBox(self) 
        self.combo_box.move(0, 50)
        self.combo_box.setFixedSize(300,50)
        self.chose_list = ["","Принят в работу", "Производятся работы", "Готов", "Отдан"] 
        self.combo_box.addItems(self.chose_list) 
        self.combo_box.setEditable(True)

        self.btn_save = QtWidgets.QPushButton(self)
        self.btn_save.setText("Изменить статус")
        self.btn_save.move(0,100)
        self.btn_save.setFixedSize(300,50)
        self.btn_save.clicked.connect(self.catch_data)


    def catch_data(self):
        self.db = sqlite3.connect('base.db')
        self.curs = self.db.cursor()
        self.curs.execute("UPDATE zakaz_stat  SET status = '"+self.combo_box.currentText()+"' WHERE number_z = '"+str(self.add_post.text())+"' ")
        QMessageBox.warning(self, 'Success', 'Данные успешно сохранены')
        self.db.commit()
        self.db.close()