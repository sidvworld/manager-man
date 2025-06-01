import requests

def save_task(task_obj):
    try:
        payload = {
            "task_name": task_obj.task_name,
            "task_deadline": task_obj.task_deadline,
            "task_priority": task_obj.task_priority,
            "created_at": task_obj.created_at
        }
        res = requests.post("http://10.0.1.159:8000/save_task/", json=payload)
        res.raise_for_status()
    except Exception as e:
        print(f"failed to print task{e}")