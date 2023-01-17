import sqlite3
from string import printable
from random import randint

def userInfo(self, name, pin, widg) -> dict:
    username = name[0:3] + str(randint(111,999))

    # GENERATING PASSWORD FOR USER
    password = ""
    for i in range(randint(10, 32)):
        # password = password + printable[randint(0, 61)]
        password = password + printable[randint(0, 61)]
    
    # CREATING 4-DIGIT PIN
    while len(pin) != 4:
        print("Pin not valid")
        pin = input("Create your pin: ")
        if len(pin) == 4:
            print(f'Your pin has been set to {pin}')
    # while True:
    #     if len(pin) == 4:
    #         print(f'Your pin has been set to {pin}')
    #         widg.QDialog.close(self)
    #         break
    #     else:
    #         print("Pin not valid!")
    #         break

    # GENERATING SSH KEYS
    public_key = ""
    for i in range(451):
        public_key = public_key + printable[randint(0, 61)]
    
    private_key = ""
    for i in range(451):
        private_key = private_key + printable[randint(0, 61)]

    try:
        sqliteConnection = sqlite3.connect('user.db')
        cursor = sqliteConnection.cursor()

        try:
            table = """ CREATE TABLE USER (
                Name CHAR(55) NOT NULL,
                Password VARCHAR(500) NOT NULL,
                PIN INT(10) NOT NULL,
                Public VARCHAR(600) NOT NULL,
                Private VARCHAR(600) NOT NULL
            ); """
            cursor.execute(table)
        except:
            pass

        params = (username, password, pin, str(public_key), str(private_key))

        cursor.execute("INSERT INTO USER VALUES (?, ?, ?, ?, ?)", params)
        sqliteConnection.commit()
    except sqlite3.Error as error:
        print('Error occured - ', error)
    finally:    
        if sqliteConnection:
            sqliteConnection.close()
            print('SQLite Connection closed')

    return {'user': username,
     'pwd': password,
     'pin': pin,
     'publickey': public_key,
     'privatekey': private_key}
