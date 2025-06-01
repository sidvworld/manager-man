import requests

SERVER_IP = "10.0.1.159"

def save_task_table(task_obj):
    try:
        payload = {
            "task_name": task_obj.task_name,
            "task_deadline": task_obj.task_deadline,
            "task_priority": task_obj.task_priority,
            "created_at": task_obj.created_at
        }
        res = requests.post(f"http://10.0.1.159:8000/save_task_table/", json=payload)
        res.raise_for_status()
        print(f"task saved: {task_obj.task_name}, {task_obj.task_deadline}, {task_obj.task_priority}, {task_obj.created_at}")
    except Exception as e:
        print(f"failed to save task{e}")