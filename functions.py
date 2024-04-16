FILEPATH = "todos_item.txt"

def get_todos(filepath = FILEPATH):
    with open(filepath, 'r') as file_local:
        todos_local = file_local.readline()
    return  todos_local

def write_todos(todo_arg, filepath = FILEPATH):
    with open(filepath, "w") as file:
        file.writelines(todo_arg)

if __name__ == "__main__":
    print("Hello")
    print(get_todos())
