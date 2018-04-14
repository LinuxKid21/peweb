import sqlite3
from random import SystemRandom

sql_connection = sqlite3.connect('website.db')
sql_cursor = sql_connection.cursor()

name = input('User Name: ')
bio = input('User Bio: ')
email = input('User Email: ')
rank = int(input('User Rank(0=no, 1=post restrict, 2=post free, 3=admin): '))
assert(name)
assert(bio)
assert(email)
assert(rank >= 0 and rank <= 3)

sr = SystemRandom()
salt = sr.choice(range(10000000,99999999))

sql_cursor.execute('insert into users values (?, ?, ?, ?, ?)', \
    (name, bio, str(salt), email, rank))
sql_connection.commit()


