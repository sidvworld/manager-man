import requests
from local_db.local_db_task import local_init_db, local_save_task

SERVER_IP = "10.0.1.159"

def save_task_table(task_obj):
    try:
        payload = {
            "task_name": task_obj.task_name,
            "task_deadline": task_obj.task_deadline,
            "task_priority": task_obj.task_priority,
            "created_at": task_obj.created_at
        }
        res = requests.post("http://10.0.1.159:8000/save_tasks_table/", json=payload, timeout=7)
        res.raise_for_status()
        print(f"task saved: {task_obj.task_name}, {task_obj.task_deadline}, {task_obj.task_priority}, {task_obj.created_at}")
    except Exception as e:
        print(f"failed to save task to server, redirecting to local storage: {e}")
        try:
            local_init_db()
            local_save_task(task_obj)
        except Exception as le:
            print(f"failed to save task locally: {le}")
