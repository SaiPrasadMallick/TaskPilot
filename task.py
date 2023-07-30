# task.py

import datetime

def add_task(username, task, target):
    username = username + "_task.txt"
    with open(username, "a") as f:
        f.write("Task: " + task + "\n")
        f.write("Target: " + target + "\n")
        f.write("Status: Not Started\n")
        f.write("Timestamp: " + str(datetime.datetime.now()) + "\n\n")

def update_task_status(username, completed_tasks, ongoing_tasks, not_started_tasks):
    username = username + "_task.txt"
    with open(username, "a") as f:
        f.write("Timestamp: " + str(datetime.datetime.now()) + "\n")
        f.write("Completed Tasks: " + completed_tasks + "\n")
        f.write("Ongoing Tasks: " + ongoing_tasks + "\n")
        f.write("Not Started Tasks: " + not_started_tasks + "\n\n")

def get_tasks(username):
    username = username + "_task.txt"
    tasks = []
    if os.path.exists(username):
        with open(username, "r") as f:
            lines = f.readlines()
            task = {}
            for line in lines:
                line = line.strip()
                if line.startswith("Task:"):
                    task["task"] = line.replace("Task: ", "")
                elif line.startswith("Target:"):
                    task["target"] = line.replace("Target: ", "")
                elif line.startswith("Status:"):
                    task["status"] = line.replace("Status: ", "")
                elif line.startswith("Timestamp:"):
                    task["timestamp"] = line.replace("Timestamp: ", "")
                    tasks.append(task)
                    task = {}
    return tasks
