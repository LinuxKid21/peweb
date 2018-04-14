import sqlite3

sql_connection = sqlite3.connect('website.db')
sql_cursor = sql_connection.cursor()
sql_cursor.execute('create table if not exists pages (Title TEXT, Content TEXT)')

# Rank is:
# 0 for no privaledge (before email is verified)
# 1 for signed up via email and can now post comments, but they need to be approved
# 2 for signed up via email and can post comments freely (as I have approved of them)
# 3 for adminisrator who can approve/deny comments as defined above and write/edit pages.
# The '3' can only be done via the add_user.py script in the tools
sql_cursor.execute('create table if not exists users (Name TEXT, Bio TEXT, Salt TEXT, Email TEXT PRIMARY KEY, Rank INTEGER)')
sql_connection.commit()

