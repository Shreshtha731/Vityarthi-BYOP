import argparse
import json
import os
from datetime import datetime

# Where we save the data so it doesn't delete when the terminal closes
TODO_FILE = "tasks_db.json"

# Just some basic colors to make the terminal output look nicer
GREEN = '\033[92m'
YELLOW = '\033[93m'
RED = '\033[91m'
RESET = '\033[0m'

def load_tasks():
    # If the file isn't there yet, just return an empty list
    if not os.path.exists(TODO_FILE):
        return []
    try:
        with open(TODO_FILE, "r") as file:
            return json.load(file)
    except json.JSONDecodeError:
        # Failsafe in case the JSON gets messed up somehow
        return [] 

def save_tasks(tasks):
    # Dump everything back into the JSON file
    with open(TODO_FILE, "w") as file:
        json.dump(tasks, file, indent=4)

def add_task(title, deadline):
    tasks = load_tasks()
    
    # Figure out the next ID number to use
    if not tasks:
        task_id = 1
    else:
        task_id = max(t['id'] for t in tasks) + 1
    
    new_task = {
        "id": task_id,
        "title": title,
        "deadline": deadline,
        "status": "Pending",
        "created_at": datetime.now().strftime("%Y-%m-%d")
    }
    
    tasks.append(new_task)
    save_tasks(tasks)
    print(f"{GREEN}Success!{RESET} Added: '{title}' (Due: {deadline})")

def view_tasks(pending_only=False):
    tasks = load_tasks()
    if not tasks:
        print(f"{YELLOW}Nothing to do right now.{RESET}")
        return

    print("\n----------------------------------------")
    print("ID   | Status     | Deadline     | Task")
    print("----------------------------------------")
    
    count = 0
    for t in tasks:
        # Skip completed ones if the user only wants to see pending tasks
        if pending_only and t['status'] == 'Completed':
            continue
            
        count += 1
        color = GREEN if t['status'] == "Completed" else YELLOW
        box = "[x]" if t['status'] == "Completed" else "[ ]"
        
        # Formatting the columns so they line up in the terminal
        print(f"{t['id']:<4} | {color}{box}{RESET}        | {t['deadline']:<12} | {t['title']}")
        
    if pending_only and count == 0:
        print(f"{GREEN}You're all caught up!{RESET}")
    print("----------------------------------------\n")

def complete_task(task_id):
    tasks = load_tasks()
    found = False
    
    for t in tasks:
        if t["id"] == task_id:
            t["status"] = "Completed"
            found = True
            break
            
    if found:
        save_tasks(tasks)
        print(f"{GREEN}Awesome.{RESET} Task {task_id} is done.")
    else:
        print(f"{RED}Error:{RESET} Couldn't find a task with ID {task_id}.")

def main():
    parser = argparse.ArgumentParser(description="A simple terminal to-do list.")
    parser.add_argument("-a", "--add", type=str, help="Add a task (put it in quotes)")
    parser.add_argument("-d", "--due", type=str, default="Whenever", help="Set a deadline")
    parser.add_argument("-v", "--view", action="store_true", help="See all tasks")
    parser.add_argument("-p", "--pending", action="store_true", help="See only unfinished tasks")
    parser.add_argument("-c", "--complete", type=int, help="Mark a task as done using its ID")

    args = parser.parse_args()

    # Figure out what the user typed and run the right function
    if args.add:
        add_task(args.add, args.due)
    elif args.view:
        view_tasks()
    elif args.pending:
        view_tasks(pending_only=True)
    elif args.complete:
        complete_task(args.complete)
    else:
        # Show the help menu if they just run the file by itself
        parser.print_help()

if __name__ == "__main__":
    main()