import sqlite3
import os

def local_init_db():
    os.makedirs('local_db', exist_ok=True)
    con = sqlite3.connect('local_db/tasks.db')
    cur = con.cursor()

    cur.execute("""
                CREATE TABLE IF NOT EXISTS tasks_table (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    task_name TEXT NOT NULL,
                    task_deadline TEXT,
                    task_priority TEXT,
                    created_at TEXT NOT NULL
                )
                """)
    
    con.commit()
    con.close()

def local_save_task(task_obj):
    con = sqlite3.connect('database/tasks.db')
    cur = con.cursor()

    cur.execute("""
                INSERT INTO tasks_table (task_name, task_deadline, task_priority, created_at)
                VALUES (?, ?, ?, ?)
                """, (task_obj.task_name, task_obj.task_deadline, task_obj.task_priority, task_obj.created_at))
    
    con.commit()
    con.close()
    
local_init_db()