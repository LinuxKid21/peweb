import sqlite3

sql_connection = sqlite3.connect('website.db')
sql_cursor = sql_connection.cursor()
sql_cursor.execute('create table if not exists pages (Title TEXT, Content TEXT)')
sql_cursor.execute('create table if not exists users (Name TEXT, Bio TEXT, Salt TEXT, Email TEXT PRIMARY KEY)')
sql_connection.commit()

