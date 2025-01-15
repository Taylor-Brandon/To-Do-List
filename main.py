tasks = []

def access_task():
    if not tasks:
        print("There are no tasks yet.")
    else:
        print("Current tasks:", tasks)

def add_task():
    new_task = input("What Task would you like to add: ")
    new_task.lower()
    tasks.append(new_task)
    print(f"Task '{new_task}' added successfully!")

def delete_task():
    print(tasks)
    removed_task = input("What tag would you like to remove: ")
    removed_task.lower()
    for task in tasks:
        if task == removed_task:
            tasks.remove(task)
    print("Removed Task")

def initial_prompt():
   print("1. Access Tasks")
   print("2. Add a Task")
   print("3. Delete a Task")

while True:
    initial_prompt()

    first_prompt = input("What Task Would you like to perform?")
    if first_prompt == "1":
        access_task()
    elif first_prompt == '2':
        add_task()
    else:
        delete_task()
