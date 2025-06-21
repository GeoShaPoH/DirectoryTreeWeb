from flask import Blueprint, request, jsonify
from ..models.user_config import UserConfig
from ..services.tree_generator import generate_tree
import os

api_bp = Blueprint('api', __name__)

@api_bp.route('/tree', methods=['POST'])
def api_tree():
    data = request.json
    path = data.get('path')
    config = UserConfig.get_global_config()
    if not path or not os.path.isdir(path):
        return jsonify({'error': 'Invalid directory'}), 400
    tree = os.path.basename(path) + '/\n' + generate_tree(
        path,
        blacklist=config.get_blacklist(),
        max_depth=config.max_depth,
        show_hidden=config.show_hidden,
        sort_option=config.sort_option
    )
    return jsonify({'tree': tree})

@api_bp.route('/browse', methods=['POST'])
def api_browse():
    data = request.json
    path = data.get('path', '.')
    
    # Si es la primera vez o se solicita la raíz, mostrar unidades disponibles
    if path == '.' or path == '/':
        if os.name == 'nt':  # Windows
            import string
            from ctypes import windll
            drives = []
            bitmask = windll.kernel32.GetLogicalDrives()
            for letter in string.ascii_uppercase:
                if bitmask & 1:
                    drives.append(f"{letter}:\\")
                bitmask >>= 1
            return jsonify({'directories': drives, 'is_root': True})
        else:  # Unix/Linux/Mac
            return jsonify({'directories': ['/'], 'is_root': True})
    
    # Validar que el path existe y es un directorio
    if not os.path.isdir(path):
        return jsonify({'error': 'Invalid directory'}), 400
    
    try:
        items = os.listdir(path)
        dirs = []
        
        # Filtrar solo directorios y ordenarlos
        for item in items:
            item_path = os.path.join(path, item)
            if os.path.isdir(item_path):
                dirs.append(item)
        
        # Ordenar alfabéticamente
        dirs.sort()
        
        # Agregar opción para ir al directorio padre si no estamos en la raíz
        parent_path = None
        if path != '/' and path != 'C:\\' and len(path) > 1:
            parent_path = os.path.dirname(path)
            if parent_path == path:  # En caso de rutas como C:\
                parent_path = None
        
        return jsonify({
            'directories': dirs, 
            'current_path': path,
            'parent_path': parent_path,
            'is_root': False
        })
        
    except PermissionError:
        return jsonify({'error': 'Permission denied'}), 403
    except Exception as e:
        return jsonify({'error': str(e)}), 500 