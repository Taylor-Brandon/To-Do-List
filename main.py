tasks = []

def access_task():
    if not tasks:
        print("There are no tasks yet.")
    else:
        print("Current tasks:", tasks)
    new_task = input("What Task would you like to add: ")
    tasks.append(new_task)
    print(f"Task '{new_task}' added successfully!")

def initial_prompt():
   print("1. Access Tasks")
   print("2. Add a Task")
   print("3. Delete a Task")

while True:
    initial_prompt()

    first_prompt = input("What Task Would you like to perform?")
    if first_prompt == "1":
        access_task()
    else:
        print("ok")
