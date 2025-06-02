import sqlite3

def insert_sample_data():
    con = sqlite3.connect('old_database/tasks.db')
    cur = con.cursor()
    cur.execute("""
                INSERT INTO tasks_table (task_name, task_deadline, task_priority, created_at)
                VALUES ('Sample Task 1', '05/31/2025', 'High', '2023-09-01 12:00:00')
                """)
    
    con.commit()
    con.close()

def delete_sample_data():
    con = sqlite3.connect('old_database/tasks.db')
    cur = con.cursor()
    cur.execute("DELETE FROM tasks_table WHERE task_name = 'Sample Task 1'")
    con.commit()
    con.close()

def delete_current_data(table):
    getuser_input = input("delete all data (y/n): ")
    if getuser_input.lower() == 'y':
        con = sqlite3.connect('old_database/tasks.db')
        cur = con.cursor()
        cur.execute(f"DELETE FROM {table}")
        con.commit()
        con.close()
        print("all data deleted")
    else:
        pass

def see_table(table):
    con = sqlite3.connect('old_database/tasks.db')
    cur = con.cursor()
    cur.execute(f"SELECT * FROM {table}")
    rows = cur.fetchall()
    for row in rows:
        print(row)
    con.close()

def reset_sequence(table):
    get_user_input = input("reset sequence (y/n): ")
    if get_user_input.lower() == 'y':
        con = sqlite3.connect('old_database/tasks.db')
        cur = con.cursor()
        cur.execute(f"UPDATE SQLITE_SEQUENCE SET SEQ=0 WHERE NAME='{table}'")
        con.commit()
        con.close()
        print(f"id for {table} reset")
    else:
        pass

# insert_sample_data()
see_table("tasks_table")
delete_current_data("tasks_table")
reset_sequence("tasks_table")

#delete_sample_data()