from .. import db
from datetime import datetime
import json

class UserConfig(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    blacklist = db.Column(db.Text, default=json.dumps(["venv", "node_modules", "dist", "build", ".git", "__pycache__", ".idea"]))
    file_blacklist = db.Column(db.Text, default=json.dumps([]))  # Archivos específicos
    extension_blacklist = db.Column(db.Text, default=json.dumps([".tmp", ".log", ".cache", ".DS_Store", "Thumbs.db"]))  # Extensiones
    max_depth = db.Column(db.Integer, default=5)
    show_hidden = db.Column(db.Boolean, default=False)
    sort_option = db.Column(db.String(20), default="name")
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    def get_blacklist(self):
        return json.loads(self.blacklist) if self.blacklist else []

    def set_blacklist(self, bl):
        self.blacklist = json.dumps(bl)

    def get_file_blacklist(self):
        return json.loads(self.file_blacklist) if self.file_blacklist else []

    def set_file_blacklist(self, fbl):
        self.file_blacklist = json.dumps(fbl)

    def get_extension_blacklist(self):
        return json.loads(self.extension_blacklist) if self.extension_blacklist else []

    def set_extension_blacklist(self, ebl):
        self.extension_blacklist = json.dumps(ebl)

    @classmethod
    def get_global_config(cls):
        """Obtener configuración global (siempre la misma para todos)"""
        config = cls.query.first()
        if not config:
            # Crear configuración global por defecto
            default_blacklist = ["venv", "node_modules", "dist", "build", ".git", "__pycache__", ".idea", ".vscode"]
            default_file_blacklist = []
            default_extension_blacklist = [".tmp", ".log", ".cache", ".DS_Store", "Thumbs.db", ".pyc", ".pyo"]
            config = cls(
                blacklist=json.dumps(default_blacklist),
                file_blacklist=json.dumps(default_file_blacklist),
                extension_blacklist=json.dumps(default_extension_blacklist),
                max_depth=5,
                show_hidden=False,
                sort_option='name'
            )
            db.session.add(config)
            db.session.commit()
        else:
            # Si existe pero tiene blacklists vacías, actualizarlas con valores por defecto
            updated = False
            if not config.blacklist or config.blacklist == '[]':
                default_blacklist = ["venv", "node_modules", "dist", "build", ".git", "__pycache__", ".idea", ".vscode"]
                config.blacklist = json.dumps(default_blacklist)
                updated = True
            
            if not config.file_blacklist or config.file_blacklist == '[]':
                config.file_blacklist = json.dumps([])
                updated = True
            
            if not config.extension_blacklist or config.extension_blacklist == '[]':
                default_extension_blacklist = [".tmp", ".log", ".cache", ".DS_Store", "Thumbs.db", ".pyc", ".pyo"]
                config.extension_blacklist = json.dumps(default_extension_blacklist)
                updated = True
            
            if updated:
                db.session.commit()
        return config 