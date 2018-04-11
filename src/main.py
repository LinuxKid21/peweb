from flask import Flask
import sqlite3

application = Flask(__name__)
sql_connection = sqlite3.connect('website.db')
sql_cursor = sql_connection.cursor()
sql_cursor.execute('create table if not exists pages (Title TEXT, Content TEXT)')
sql_connection.commit()

@application.route('/<page_name>')
def route_pages(page_name):
    return 'Hello World! It\'s totally radical, ' + page_name

@application.route('/')
def route_main():
    return route_pages('home')

