from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtWidgets import * 
from PyQt5.QtGui import * 
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidget, QTableWidgetItem
import sys
from adding_storage import ADD_STORAGE
from adding_zakaz import ADD_zakaz
from change_stat import chenge_stat
from givezak import Give
import sqlite3

class MainWindow(QMainWindow):
    def __init__(self):
 
        super(MainWindow,self).__init__()
        

        self.setWindowTitle("Учет заказов")
        self.setFixedSize(1200,600)
        


        self.btn1 = QtWidgets.QPushButton(self)
        self.btn1.setText("Главная")
        self.btn1.move(0,0)
        self.btn1.setFixedSize(400,100)
        self.btn1.clicked.connect(self.show_main)

        self.btn2 = QtWidgets.QPushButton(self)
        self.btn2.setText("Учет склада")
        self.btn2.move(400,0)
        self.btn2.setFixedSize(400,100)
        self.btn2.clicked.connect(self.show_storage)

        self.btn3 = QtWidgets.QPushButton(self)
        self.btn3.setText("Заказ")
        self.btn3.move(800,0)
        self.btn3.setFixedSize(400,100)
        self.btn3.clicked.connect(self.show_zakaz)



        #mainWindow
        self.table = QTableWidget(self) #Create a table
        self.table.move(0,100)
        self.table.setFixedSize(1200,500)
        self.table.setColumnCount(4)
        self.table.setHorizontalHeaderLabels(["дата"," ФИО ", "Номер Заказа","Статус"])     
        self.horizontalHeader = self.table.horizontalHeader()
        
        self.table.horizontalHeaderItem(0).setToolTip("Date")
        self.table.horizontalHeaderItem(1).setToolTip("FIO")
        self.table.horizontalHeaderItem(2).setToolTip("number_z")
        self.table.horizontalHeaderItem(3).setToolTip("status")
        self.horizontalHeader.resizeSection(0, 200)
        self.horizontalHeader.resizeSection(1, 500)
        self.horizontalHeader.resizeSection(2, 250)
        self.horizontalHeader.resizeSection(3, 250)

        #storage  
        self.table_storage = QTableWidget(self) #Create a table_storage
        self.table_storage.move(0,100)
        self.table_storage.setFixedSize(1200,450)
        self.table_storage.setColumnCount(4)
        self.table_storage.setHorizontalHeaderLabels([" Название материала ", "Поставщик","Код материала","Остаток"])     
        self.horizontalHeader1 = self.table_storage.horizontalHeader()
        
        self.table_storage.horizontalHeaderItem(0).setToolTip("Name")
        self.table_storage.horizontalHeaderItem(1).setToolTip("Give")
        self.table_storage.horizontalHeaderItem(2).setToolTip("Num_stor")
        self.table_storage.horizontalHeaderItem(3).setToolTip("Count")
        self.horizontalHeader1.resizeSection(0, 200)
        self.horizontalHeader1.resizeSection(1, 500)
        self.horizontalHeader1.resizeSection(2, 295)
        self.horizontalHeader1.resizeSection(3, 200)

        self.btn_find_in_storage = QtWidgets.QPushButton(self)
        self.btn_find_in_storage.setText("Поиск по складу")
        self.btn_find_in_storage.move(0,550)
        self.btn_find_in_storage.setFixedSize(300,50)
        self.btn_find_in_storage.clicked.connect(self.find_in_storage)

        self.combo_box = QComboBox(self) 
        self.combo_box.move(300, 550)
        self.combo_box.setFixedSize(300,50)
        self.chose_list = ["","Код материала", "Поставщик", "Остаток"] 
        self.combo_box.addItems(self.chose_list) 
        self.combo_box.setEditable(True)
        self.combo_box.textActivated[str].connect(self.change_name)

        self.find_index = QLineEdit(self)
        self.find_index.move(600, 550)
        self.find_index.resize(300,50)
        self.find_index.setPlaceholderText("Выберите вариант")

        self.btn_print = QtWidgets.QPushButton(self)
        self.btn_print.setText("Добавить на слад")
        self.btn_print.move(900,550)
        self.btn_print.setFixedSize(300,50)
        self.btn_print.clicked.connect(self.switch_add_storage)
        
        
        #zakaz
        self.btn_take = QtWidgets.QPushButton(self)
        self.btn_take.setText("Принять заказ")
        self.btn_take.move(100,225)
        self.btn_take.setFixedSize(300,100)
        self.btn_take.clicked.connect(self.accept_take)

        


        self.btn_change_status = QtWidgets.QPushButton(self)
        self.btn_change_status.setText("Изменить статус")
        self.btn_change_status.move(450,375)
        self.btn_change_status.setFixedSize(300,100)
        self.btn_change_status.clicked.connect(self.chenge_stat)

        self.btn_give = QtWidgets.QPushButton(self)
        self.btn_give.setText("Отдать заказ")
        self.btn_give.move(800,225)
        self.btn_give.setFixedSize(300,100)
        self.btn_give.clicked.connect(self.switch_given)


        #cnlients
        self.table_client = QTableWidget(self) #Create a table_client
        self.table_client.move(0,100)
        self.table_client.setFixedSize(1200,450)
        self.table_client.setColumnCount(4)
        self.table_client.setHorizontalHeaderLabels([" ФИО ", "Номер телефона","Дата рождения","Скидка"])     
        self.horizontalHeader3 = self.table_client.horizontalHeader()
        
        self.table_client.horizontalHeaderItem(0).setToolTip("FIO")
        self.table_client.horizontalHeaderItem(1).setToolTip("Num_tel")
        self.table_client.horizontalHeaderItem(2).setToolTip("Data_rozh")
        self.table_client.horizontalHeaderItem(3).setToolTip("Sell")
        self.horizontalHeader3.resizeSection(0, 200)
        self.horizontalHeader3.resizeSection(1, 500)
        self.horizontalHeader3.resizeSection(2, 295)
        self.horizontalHeader3.resizeSection(3, 200)
        
        self.btn_find_client = QtWidgets.QPushButton(self)
        self.btn_find_client.setText("Поиск")
        self.btn_find_client.move(0,550)
        self.btn_find_client.setFixedSize(300,50)

        self.combo_box_client = QComboBox(self) 
        self.combo_box_client.move(300, 550)
        self.combo_box_client.setFixedSize(300,50)
        self.chose_list = ["","Название материала", "Поставщик", "Остаток"] 
        self.combo_box_client.addItems(self.chose_list) 
        self.combo_box_client.setEditable(True)

        self.find_index_client = QLineEdit(self)
        self.find_index_client.move(600, 550)
        self.find_index_client.resize(300,50)
        self.find_index_client.setPlaceholderText("Выберите вариант")

        self.btn_add_client = QtWidgets.QPushButton(self)
        self.btn_add_client.setText("Добавить клиента")
        self.btn_add_client.move(900,550)
        self.btn_add_client.setFixedSize(300,50)

        

        
        
        self.hide_main()
        self.hide_storage()
        self.hide_zakaz()
        self.hide_client()

        

        
        # self.lbl = QtWidgets.QLabel(self)
        # self.lbl.setText("test")
        # self.lbl.move(0,100)
        # self.lbl.hide()
        # self.lbl.show()  

    def accept_take(self):
        self.mainwindow = ADD_zakaz()
        self.update_data(self.table_storage)
        self.mainwindow.show()

    def hide_main(self):
        self.table.hide()

    def hide_storage(self):
        self.table_storage.hide()
        self.btn_find_in_storage.hide()
        self.combo_box.hide()
        self.find_index.hide()
        self.btn_print.hide()

    def hide_zakaz(self):
        self.btn_take.hide()
        self.btn_give.hide()
        self.btn_change_status.hide()

    def hide_client(self):
        self.table_client.hide()
        self.btn_add_client.hide()
        self.btn_find_client.hide()
        self.combo_box_client.hide()
        self.find_index_client.hide()

    def show_client(self):
        self.hide_main()
        self.hide_storage()
        self.hide_zakaz      
        self.table_client.show()
        self.btn_add_client.show()
        self.btn_find_client.show()
        self.combo_box_client.show()
        self.find_index_client.show()

    def show_zakaz(self):
        self.hide_main()
        self.hide_storage()
        self.hide_client()
        self.btn_take.show()
        self.btn_give.show()
        self.btn_change_status.show()

    
    def show_main(self):
        
        self.hide_storage()
        self.hide_zakaz()
        self.hide_client()
        self.table.show()
        self.update_stat()

    

    def show_storage(self):
        self.update_data(self.table_storage)
        self.hide_main()
        self.hide_zakaz()
        self.hide_client()
        self.table_storage.show() 
        self.btn_find_in_storage.show()   
        self.combo_box.show()
        self.find_index.show()
        self.btn_print.show()

    def change_name(self):
        self.txt = self.combo_box.currentText()
        self.find_index.setPlaceholderText('Введите '+self.txt)

    def update_data(self,table_storage):
        self.db = sqlite3.connect('base.db')
        self.curs = self.db.cursor()
        self.curs.execute("SELECT * FROM storage ")
        self.check = self.curs.fetchall()                     
        cnt = self.table_storage.rowCount()
        while(len(self.check)  > cnt):
            if len(self.check)  > cnt:
                    self.table_storage.insertRow(self.table_storage.rowCount()) 
                    cnt+=1
        for i in range(len(self.check)):           
            for j in range(4):
                item = QTableWidgetItem(self.check[i][j])
                self.table_storage.setItem(i, j, item)

                
    def find_in_storage(self):
        self.db = sqlite3.connect('base.db')
        self.curs = self.db.cursor()    
        if self.combo_box.currentText() == 'Код материала':
            self.curs.execute("SELECT * FROM storage WHERE Num_stor = '"+str(self.find_index.text())+"'")
            self.check = self.curs.fetchall()    
                
            if len(self.check) == 0:
                QMessageBox.warning(self, 'Warning', 'Такого человека не найдено')      
                return 0     
        if self.combo_box.currentText() == 'Поставщик':
            self.curs.execute("SELECT * FROM storage WHERE Give = '"+str(self.find_index.text())+"'")
            self.check = self.curs.fetchall()            
            if len(self.check) == 0:
                QMessageBox.warning(self, 'Warning', 'Такого человека не найдено')      
                return 0  
        if self.combo_box.currentText() == 'Остаток':
            self.curs.execute("SELECT * FROM storage WHERE Count = '"+str(self.find_index.text())+"'")
            self.check = self.curs.fetchall()             
            if len(self.check) == 0:
                QMessageBox.warning(self, 'Warning', 'Такого человека не найдено')      
                return 0 
        self.table_storage.setRowCount(0)
        self.table_storage.setColumnCount(4)
        for i in range(len(self.check)):            
            self.table_storage.insertRow(self.table_storage.rowCount())             
            for j in range(4):                
                item = QTableWidgetItem(self.check[i][j])
                self.table_storage.setItem(i, j, item)

    def switch_add_storage(self):
        self.mainwindow = ADD_STORAGE(self.update_data,self.table_storage)
        self.update_data(self.table_storage)
        self.mainwindow.show()

    def update_stat(self):
        self.db = sqlite3.connect('base.db')
        self.curs = self.db.cursor()
        self.curs.execute("SELECT * FROM zakaz_stat")
        self.check = self.curs.fetchall()
        self.table.setRowCount(0)
        self.table.setColumnCount(4)
        for i in range(len(self.check)):
            self.table.insertRow(self.table.rowCount())
            for j in range(4):
                item = QTableWidgetItem(self.check[i][j])
                self.table.setItem(i, j, item)

    def chenge_stat(self):
        self.mainwindow = chenge_stat()        
        self.mainwindow.show()

    def switch_given(self):
        self.mainwindow = Give()        
        self.mainwindow.show()


    

    









if __name__ == "__main__":
    app = QApplication(sys.argv)
    
    mainwindow = MainWindow()    
    mainwindow.show()
    app.exec()
    