import sqlite3#imports database library

connection = sqlite3.connect('login.db')#initializes database connection
c=connection.cursor()

login = input("login")
password = input('password?')

c.execute('''CREATE TABLE logins
            (username,password,email)''')#creates table with 3 columns

truepass = c.execute('SELECT ? FROM logins WHERE symbol=username', login)#retrieves tru value

if password == truepass:#possible authentication
    print('Valid')

else:
    print('nah')

c.execute('INSERT INTO stocks VALUES (pradyungn,oooooooo,pradyungn@gmail.com')

connection.commit()
connection.close()

