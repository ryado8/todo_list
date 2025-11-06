def error_for_list_title(title, lists):
    if any(lst['title'] == title for lst in lists):
        return "The title must be unique."
    elif not 1 <= len(title) <= 100:
        return "The title must be between 1 and 100 characters"
    else:
        return None

def find_list_by_id(list_id, lists):
    return next((lst for lst in lists if lst["id"] == list_id), None)

def find_todo_by_id(todo_id, list):
    return next((todo for todo in list if todo["id"] == todo_id), None)

def error_for_todo(todo):
    if len(todo) == 0:
        return "Title is required."
    elif len(todo) > 100:
        return "The title is too long. Must be 100 characters or less."
    else:
        return None

def delete_todo_by_id(todo_id, lst):
    lst['todos'] = [todo for todo in lst['todos'] if todo['id'] != todo_id]

def complete_todos(lst):
    for todo in lst["todos"]:
        if not todo["completed"]:
            todo["completed"] = True

def delete_todo_list(list_id, session):
    session["lists"] = [lst for lst in session["lists"] if lst["id"] != list_id]

def todos_remaining(lst):
    return sum(1 for todo in lst["todos"] if not todo["completed"])

def is_list_completed(lst):
    return len(lst["todos"]) > 0 and todos_remaining(lst) == 0

def is_todo_completed(todo):
    return todo['completed']

def sort_items(items, select_completed):
    incomplete_items = []
    complete_items = []

    for item in sorted(items, key=lambda item: item['title'].lower()):
        if select_completed(item):
            complete_items.append(item)
        else:
            incomplete_items.append(item)

    return incomplete_items + complete_items