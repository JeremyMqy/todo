import functions
import time

now = time.strftime("%b %d, %Y %H:%M:%S")
print("It's", now)

while True:
    user_action = input("Type add, show, edit, complete, or exit")
    user_action = user_action.strip()

    if user_action.startswith("add"):
        todo = user_action[4:]
        todos = functions.get_todos()
        todos.append(todo + "\n")
        functions.write_todos(todos)
    elif user_action.startswith("show"):
        todos = functions.get_todos()
        for index, item in enumerate(todos):
            item = item.strip("\n")

