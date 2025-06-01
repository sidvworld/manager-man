import sqlite3

def see_data():
    con = sqlite3.connect('database/tasks.db')
    cur = con.cursor()

    cur.execute("SELECT * FROM tasks_table")

    con.commit()
    con.close()

see_data()