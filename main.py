todos = []

while True:
    user_action = input("type add or show")
    match user_action:
        case 'add':
            todo = input("enter a todo: ")
            todos.append(todo)
        case 'show':
            print(todos)
        case 'exit':
            break

test
