import sqlite3
db = sqlite3.connect('base.db')
c = db.cursor()


#create
# c.execute("""
#       CREATE TABLE zakaz_stat (
#           Data text,
#           FIO text,
#           number_z text,
#           status text)
          
#   """)


# c.execute("""
#       CREATE TABLE zakaz (
#             Number text,
#             Name text,
#             Count text,
#             Opis text)""")

# c.execute("""
#       CREATE TABLE storage (
#             Name text,
#             Give text,
#             Num_stor text,
#             Count text
         
# )
#    """)

# c.execute("""
#       CREATE TABLE matireal (
#             Name text,
#             number text
         
# )
#   """)

# c.execute("""
#       CREATE TABLE client (
#             FIO text,
#             Num_tel text,
#             Data_rozh text,
#             num text,
#             Sell text
#          )
#   """)



#ADD
#c.execute("INSERT INTO workers VALUES('1','test','test','test','test')")

#change
#c.execute("UPDATE workers SET num = '0' WHERE rowid = 1 ")

#find from * we can put name of titles <>
#c.execute("DELETE FROM zakaz_stat WHERE number_z = '18'")
c.execute("SELECT * FROM zakaz_stat")



#choose all print
print(c.fetchall())

#save
db.commit()
db.close()