from flask import Flask, render_template, request
import os

app = Flask(__name__)

def generate_directory_tree(path, prefix=''):
    tree = ''
    try:
        contents = sorted(os.listdir(path))
        pointers = ['├── ' if i < len(contents) - 1 else '└── ' for i in range(len(contents))]
        
        for pointer, name in zip(pointers, contents):
            full_path = os.path.join(path, name)
            if os.path.isdir(full_path):
                tree += f"{prefix}{pointer}{name}/\n"
                tree += generate_directory_tree(full_path, prefix + ('│   ' if pointer == '├── ' else '    '))
            else:
                tree += f"{prefix}{pointer}{name}\n"
    except PermissionError:
        tree += f"{prefix}Permission denied\n"
    except Exception as e:
        tree += f"{prefix}Error: {str(e)}\n"
    
    return tree

@app.route('/', methods=['GET', 'POST'])
def index():
    tree = ''
    if request.method == 'POST':
        path = request.form['path']
        if os.path.isdir(path):
            base_name = os.path.basename(path)
            tree = f"{base_name}/\n" + generate_directory_tree(path)
        else:
            tree = "Error: Not a valid directory"
    return render_template('index.html', tree=tree)

if __name__ == '__main__':
    app.run(debug=True)