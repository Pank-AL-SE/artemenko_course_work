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
import datetime

class ADD_zakaz(QMainWindow):
    def __init__(self):
 
        super().__init__()
        
       
        self.setWindowTitle("Добавление на заказа")
        self.setFixedSize(300,300)

        self.FIO = QLineEdit(self)
        self.FIO.move(0, 0)
        self.FIO.resize(300,50)
        self.FIO.setPlaceholderText("ФИО покупателя")
       

        self.mat = QLineEdit(self)
        self.mat.move(0, 50)
        self.mat.resize(300,50)
        self.mat.setPlaceholderText("Материал")
        self.count = QLineEdit(self)
        self.count.move(0, 100)
        self.count.resize(300,50)
        self.count.setPlaceholderText("Количество")

        self.combo_box = QComboBox(self) 
        self.combo_box.move(0, 150)
        self.combo_box.setFixedSize(300,50)
        self.chose_list = ["","Принят в работу", "Производятся работы", "Готов", "Отдан"] 
        self.combo_box.addItems(self.chose_list) 
        self.combo_box.setEditable(True)

        self.opis = QLineEdit(self)
        self.opis.move(0, 200)
        self.opis.resize(300,50)
        self.opis.setPlaceholderText("Описание")

        self.btn_save = QtWidgets.QPushButton(self)
        self.btn_save.setText("Создать заказ")
        self.btn_save.move(0,250)
        self.btn_save.setFixedSize(300,50)
        self.btn_save.clicked.connect(self.catch_data)


    def catch_data(self):
        self.db = sqlite3.connect('base.db')
        self.curs = self.db.cursor()
        if len(self.FIO.text()) == 0:
            QMessageBox.warning(self, 'Warning', 'Введите ФИО')
            return 0
        if len(self.mat.text()) == 0:
            QMessageBox.warning(self, 'Warning', 'Введите материал')
            return 0
        if len(self.count.text()) == 0:
            QMessageBox.warning(self, 'Warning', 'Введите количество материала')
            return 0
        if len(self.combo_box.currentText()) == 0:
            QMessageBox.warning(self, 'Warning', 'Введите статус заказа')
            return 0
        if len(self.opis.text()) == 0:
            QMessageBox.warning(self, 'Warning', 'Добавьте описание')
            return 0
        
        self.curs.execute("SELECT * FROM zakaz")
        self.num = len(self.curs.fetchall())+1
        self.curs.execute("SELECT Count FROM storage WHERE Name = '"+self.mat.text()+"'")
        count = int(self.curs.fetchall()[0][0])
        print()
        if count < int(self.count.text()):
            QMessageBox.warning(self, 'Warning', 'Количество на складе меньше чем требуется')
            return 0
        today = datetime.datetime.today()
        self.curs.execute("INSERT INTO zakaz_stat VALUES('"+today.strftime("%d.%m.%Y")+"','"+self.FIO.text()+"','"+str(self.num)+"','"+self.combo_box.currentText()+"')")        
        self.curs.execute("INSERT INTO zakaz VALUES('"+str(self.num)+"','"+self.mat.text()+"','"+self.count.text()+"','"+self.opis.text()+"')")
        
        
        self.curs.execute("UPDATE storage  SET Count = '"+str(count-int(self.count.text()))+"' WHERE Name = '"+str(self.mat.text())+"' ")
        QMessageBox.warning(self, 'Warning', 'Заказ добавлен')
        self.db.commit()
        self.db.close()