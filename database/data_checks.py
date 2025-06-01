import sqlite3

def insert_sample_data():
    con = sqlite3.connect('database/tasks.db')
    cur = con.cursor()
    cur.execute("""
                INSERT INTO tasks_table (task_name, task_deadline, task_priority, created_at)
                VALUES ('Sample Task 1', '05/31/2025', 'High', '2023-09-01 12:00:00')
                """)
    
    con.commit()
    con.close()

def delete_sample_data():
    con = sqlite3.connect('database/tasks.db')
    cur = con.cursor()
    cur.execute("DELETE FROM tasks_table WHERE task_name = 'Sample Task 1'")
    con.commit()
    con.close()

def see_table(table):
    con = sqlite3.connect('database/tasks.db')
    cur = con.cursor()
    cur.execute(f"SELECT * FROM {table}")
    rows = cur.fetchall()
    for row in rows:
        print(row)
    con.close()

#insert_sample_data()
see_table("tasks_table")
#delete_sample_data()