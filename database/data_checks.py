import sqlite3

def see_table(table):
    con = sqlite3.connect('database/tasks.db')
    cur = con.cursor()

    cur.execute(f"SELECT * FROM {table}")
    rows = cur.fetchall()
    for row in rows:
        print(row)

    con.close()

see_table("tasks_table")