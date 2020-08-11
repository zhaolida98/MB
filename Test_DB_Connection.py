import logging



from pprint import pprint
from base.selenium_driver import SeleniumDriver
from Utils.configreader import db

class dataBaseConnection(SeleniumDriver):


    def __init__(self):

        try:
            conn = SeleniumDriver.createConnection(self)
            print(conn)

            conn.autocommit = True
            cursor = conn.cursor()

        except Exception as err:
            print("psycopg2 connect() ERROR:", err)





    def createTable(self):
        create_table_command = "Create table delivery.pet(id INTEGER, name VARCHAR(100), age INTEGER NOT NULL)"
        self.cursor.execute(create_table_command)

    def insertNewRecord(self):
        new_record = ("1","Jimmy","1")
        insert_command = "INSERT INTO delivery.pet(id,name,age) VALUES('"+new_record[0]+"','"+new_record[1]+"'," \
                                                                                                            "'"+new_record[2]+"')"
        pprint(insert_command)
        self.cursor.execute(insert_command)

    def dropTable(self):
        drop_table_command = "DROP table pet"
        self.cursor.execute(drop_table_command)



db = dataBaseConnection()
#db.createTable()
#db.dropTable()
