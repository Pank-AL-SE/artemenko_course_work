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

class ADD_STORAGE(QMainWindow):
    def __init__(self,foo,table):
 
        super().__init__()
        
        self.foo = foo 
        self.table = table
        self.setWindowTitle("Добавление на склад")
        self.setFixedSize(300,200)

        self.add_post = QLineEdit(self)
        self.add_post.move(0, 0)
        self.add_post.resize(300,50)
        self.add_post.setPlaceholderText("Поставщик")
       

        self.name_count = QLineEdit(self)
        self.name_count.move(0, 50)
        self.name_count.resize(300,50)
        self.name_count.setPlaceholderText("Название материала")

        self.count = QLineEdit(self)
        self.count.move(0, 100)
        self.count.resize(300,50)
        self.count.setPlaceholderText("Количество")

        self.btn_save_storage = QtWidgets.QPushButton(self)
        self.btn_save_storage.setText("Добавить на склад")
        self.btn_save_storage.move(0,150)
        self.btn_save_storage.setFixedSize(300,50)
        self.btn_save_storage.clicked.connect(self.catch_data)

        #c.execute("INSERT INTO  VALUES('1','test','test','test','test')")



    def catch_data(self):
        if len(self.add_post.text()) == 0:
            QMessageBox.warning(self, 'Warning', 'Введите поставщика')
            return 0
        if len(self.name_count.text()) == 0:
            QMessageBox.warning(self, 'Warning', 'Введите название материала')
            return 0
        try:
            int(self.count.text())
        except:
            QMessageBox.warning(self, 'Warning', 'количество не число')
            return 0
        if len(self.count.text()) == 0:
            QMessageBox.warning(self, 'Warning', 'Введите количество материала')
            return 0
        self.db = sqlite3.connect('base.db')
        self.curs = self.db.cursor()
        
        
        try:
            self.db = sqlite3.connect('base.db')
            self.curs = self.db.cursor()
            self.curs.execute("SELECT * FROM matireal WHERE Name = '"+self.name_count.text()+"'")
            self.check = self.curs.fetchall() 
            if len(self.check) == 0:
                
                try:
                    self.curs.execute("SELECT * FROM matireal")
                    self.num = len(self.curs.fetchall())+1
                    print(self.num)
                    self.curs.execute("INSERT INTO matireal VALUES('"+self.name_count.text()+"','"+str(self.num)+"')")
                    self.curs.execute("INSERT INTO storage VALUES('"+self.name_count.text()+"','"+self.add_post.text()+"','"+str(self.num)+"','"+self.count.text()+"')")
                    
                except:
                    self.num = 1
                    self.curs.execute("INSERT INTO matireal VALUES('"+self.name_count.text()+"','"+str(self.num)+"')")
                    self.curs.execute("INSERT INTO storage VALUES('"+self.name_count.text()+"','"+self.add_post.text()+"','"+str(self.num)+"','"+self.count.text()+"')")
                    
            else:
                self.num = self.check[0][1] 
                
                
                self.curs.execute("SELECT * FROM storage WHERE Name = '"+self.name_count.text()+"'")
                self.check = self.curs.fetchall()
                if len(self.check) == 0:
                    self.curs.execute("INSERT INTO storage VALUES('"+self.name_count.text()+"','"+self.add_post.text()+"','"+str(self.num)+"','"+self.count.text()+"')")
                else:
                    self.curs.execute("SELECT * FROM storage WHERE Name = '"+self.name_count.text()+"'")
                    self.check = self.curs.fetchall()
                    print(self.check[0][3])

                    self.curs.execute("UPDATE storage  SET Count = '"+str(int(self.check[0][3])+int(self.count.text()))+"' WHERE Num_stor = '"+str(self.num)+"' ")  
            

            self.db.commit()
            self.db.close()
            QMessageBox.warning(self, 'Success', 'Данные успешно сохранены')
            self.foo(self.table)
        except:
            QMessageBox.warning(self, 'Warning', 'Данные не сохранены')
            return 0

            

        

        