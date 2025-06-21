from .. import db
from datetime import datetime
import json

class UserConfig(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    blacklist = db.Column(db.Text, default=json.dumps(["venv", "node_modules", "dist", "build", ".git", "__pycache__", ".idea"]))
    max_depth = db.Column(db.Integer, default=5)
    show_hidden = db.Column(db.Boolean, default=False)
    sort_option = db.Column(db.String(20), default="name")
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    def get_blacklist(self):
        return json.loads(self.blacklist) if self.blacklist else []

    def set_blacklist(self, bl):
        self.blacklist = json.dumps(bl)

    @classmethod
    def get_global_config(cls):
        """Obtener configuración global (siempre la misma para todos)"""
        config = cls.query.first()
        if not config:
            # Crear configuración global por defecto
            default_blacklist = ["venv", "node_modules", "dist", "build", ".git", "__pycache__", ".idea", ".vscode"]
            config = cls(
                blacklist=json.dumps(default_blacklist),
                max_depth=5,
                show_hidden=False,
                sort_option='name'
            )
            db.session.add(config)
            db.session.commit()
        else:
            # Si existe pero tiene blacklist vacía, actualizarla con valores por defecto
            if not config.blacklist or config.blacklist == '[]':
                default_blacklist = ["venv", "node_modules", "dist", "build", ".git", "__pycache__", ".idea", ".vscode"]
                config.blacklist = json.dumps(default_blacklist)
                db.session.commit()
        return config 