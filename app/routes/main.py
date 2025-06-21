from flask import Blueprint, render_template, request, redirect, url_for, flash
from ..models.user_config import UserConfig
from ..services.tree_generator import generate_tree
from .. import db
import os
import json

main_bp = Blueprint('main', __name__)

@main_bp.route('/', methods=['GET', 'POST'])
def index():
    config = UserConfig.get_global_config()
    tree = ''
    error = ''
    if request.method == 'POST':
        path = request.form.get('path')
        if os.path.isdir(path):
            tree = os.path.basename(path) + '/\n' + generate_tree(
                path,
                blacklist=config.get_blacklist(),
                file_blacklist=config.get_file_blacklist(),
                extension_blacklist=config.get_extension_blacklist(),
                max_depth=config.max_depth,
                show_hidden=config.show_hidden,
                sort_option=config.sort_option
            )
        else:
            error = 'Error: Not a valid directory'
    return render_template('index.html', tree=tree, config=config, error=error)

@main_bp.route('/clear', methods=['GET'])
def clear_tree():
    """Limpiar el árbol y redirigir a la página principal sin datos del formulario"""
    return redirect(url_for('main.index'))

@main_bp.route('/config', methods=['POST'])
def update_config():
    config = UserConfig.get_global_config()
    data = request.form
    config.max_depth = int(data.get('max_depth', config.max_depth))
    config.show_hidden = bool(data.get('show_hidden', config.show_hidden))
    config.sort_option = data.get('sort_option', config.sort_option)
    
    # Actualizar blacklists
    blacklist = data.get('blacklist')
    if blacklist:
        config.set_blacklist(json.loads(blacklist))
    
    file_blacklist = data.get('file_blacklist')
    if file_blacklist:
        config.set_file_blacklist(json.loads(file_blacklist))
    
    extension_blacklist = data.get('extension_blacklist')
    if extension_blacklist:
        config.set_extension_blacklist(json.loads(extension_blacklist))
    
    db.session.commit()
    flash('Configuración actualizada', 'success')
    return redirect(url_for('main.index')) 