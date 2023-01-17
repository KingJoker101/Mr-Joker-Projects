import os
import sqlite3
import pandas as pd

def xternal():
    os.system('start transaction.xlsx')

def loadExcelData(self, excel_file_dir, worksheet_name, qtwi):
        df = pd.read_excel(excel_file_dir, worksheet_name)
        if df.size == 0:
            return

        df.fillna('', inplace=True)
        self.table.setRowCount(df.shape[0])
        self.table.setColumnCount(df.shape[1])
        self.table.setHorizontalHeaderLabels(df.columns)

        # returns pandas array object
        for row in df.iterrows():
            values = row[1]
            for col_index, value in enumerate(values):
                if isinstance(value, (float, int)):
                    value = '{0:0,.0f}'.format(value)
                tableItem = qtwi(str(value))
                self.table.setItem(row[0], col_index, tableItem)

        self.table.setColumnWidth(2, 300)

def validate_usr(self, usr, pwd, nwd, widg):
    try:
        sqliteConnection = sqlite3.connect('user.db')
        cursor = sqliteConnection.cursor()

        params = (usr,)
        cursor.execute("SELECT * FROM USER WHERE Name = ?", params)

        res = cursor.fetchall()
        r_usr = res[0][0]
        r_pass = res[0][1]

        if str(usr) == str(r_usr) and str(pwd) == str(r_pass):
            print("Login Valid")
            self.load = nwd()
            self.load.show()
            widg.QDialog.close(self)
        else:
            print("Login Failed")

        sqliteConnection.commit()
    except sqlite3.Error as error:
        print('Error occured - ', error)
    finally:    
        if sqliteConnection:
            sqliteConnection.close()
            print('SQLite Connection closed')

def validate_pin(self, usr, pin, nwd, widg):
    try:
        sqliteConnection = sqlite3.connect('user.db')
        cursor = sqliteConnection.cursor()

        params = (usr,)
        cursor.execute("SELECT * FROM USER WHERE Name = ?", params)

        if int(pin) == cursor.fetchall()[0][2]:
            print("Login Valid")
            self.load = nwd()
            self.load.show()
            widg.QDialog.close(self)
        else:
            print("Login Failed")

        sqliteConnection.commit()
    except sqlite3.Error as error:
        print('Error occured - ', error)
    finally:    
        if sqliteConnection:
            sqliteConnection.close()
            print('SQLite Connection closed')

def validate_ssh(self, usr, pub, pri, nwd, widg):
    try:
        sqliteConnection = sqlite3.connect('user.db')
        cursor = sqliteConnection.cursor()

        params = (usr,)
        cursor.execute("SELECT * FROM USER WHERE Name = ?", params)

        res = cursor.fetchall()
        r_pub = res[0][3]
        r_pri = res[0][4]

        if pub == r_pub and pri == r_pri:
            print("Login Valid")
            self.load = nwd()
            self.load.show()
            widg.QDialog.close(self)
        else:
            print("Login Failed")

        sqliteConnection.commit()
    except sqlite3.Error as error:
        print('Error occured - ', error)
    finally:    
        if sqliteConnection:
            sqliteConnection.close()
            print('SQLite Connection closed')