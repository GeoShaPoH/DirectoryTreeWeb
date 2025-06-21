import os

def generate_tree(path, blacklist=None, max_depth=5, show_hidden=False, sort_option="name", current_depth=0):
    if blacklist is None:
        blacklist = ["venv", "node_modules", "dist", "build", ".git", "__pycache__", ".idea"]
    tree = ''
    try:
        if current_depth > max_depth:
            return tree
        contents = os.listdir(path)
        if not show_hidden:
            contents = [c for c in contents if not c.startswith('.')]
        contents = [c for c in contents if c not in blacklist]
        if sort_option == "name":
            contents.sort()
        elif sort_option == "size":
            contents.sort(key=lambda x: os.path.getsize(os.path.join(path, x)))
        elif sort_option == "date":
            contents.sort(key=lambda x: os.path.getmtime(os.path.join(path, x)))
        pointers = ['├── ' if i < len(contents) - 1 else '└── ' for i in range(len(contents))]
        for pointer, name in zip(pointers, contents):
            full_path = os.path.join(path, name)
            if os.path.isdir(full_path):
                tree += f"{pointer}{name}/\n"
                tree += ("    " if pointer == '└── ' else "│   ") + generate_tree(full_path, blacklist, max_depth, show_hidden, sort_option, current_depth + 1)
            else:
                tree += f"{pointer}{name}\n"
    except PermissionError:
        tree += "Permission denied\n"
    except Exception as e:
        tree += f"Error: {str(e)}\n"
    return tree 