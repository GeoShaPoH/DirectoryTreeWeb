import os

def generate_tree(path, blacklist=None, file_blacklist=None, extension_blacklist=None, max_depth=5, show_hidden=False, sort_option="name", current_depth=0):
    if blacklist is None:
        blacklist = ["venv", "node_modules", "dist", "build", ".git", "__pycache__", ".idea"]
    if file_blacklist is None:
        file_blacklist = []
    if extension_blacklist is None:
        extension_blacklist = [".tmp", ".log", ".cache", ".DS_Store", "Thumbs.db"]
    
    tree = ''
    try:
        if current_depth > max_depth:
            return tree
        contents = os.listdir(path)
        if not show_hidden:
            contents = [c for c in contents if not c.startswith('.')]
        
        # Filtrar directorios por blacklist
        contents = [c for c in contents if c not in blacklist]
        
        # Separar archivos y directorios para aplicar filtros específicos
        files = []
        directories = []
        
        for item in contents:
            full_path = os.path.join(path, item)
            if os.path.isdir(full_path):
                directories.append(item)
            else:
                # Aplicar filtros de archivos
                should_include = True
                
                # Verificar si el archivo está en la blacklist de archivos
                if item in file_blacklist:
                    should_include = False
                
                # Verificar si la extensión está en la blacklist de extensiones
                if should_include:
                    file_ext = os.path.splitext(item)[1].lower()
                    if file_ext in extension_blacklist:
                        should_include = False
                
                if should_include:
                    files.append(item)
        
        # Combinar directorios y archivos
        contents = directories + files
        
        # Aplicar ordenamiento
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
                tree += ("    " if pointer == '└── ' else "│   ") + generate_tree(full_path, blacklist, file_blacklist, extension_blacklist, max_depth, show_hidden, sort_option, current_depth + 1)
            else:
                tree += f"{pointer}{name}\n"
    except PermissionError:
        tree += "Permission denied\n"
    except Exception as e:
        tree += f"Error: {str(e)}\n"
    return tree 