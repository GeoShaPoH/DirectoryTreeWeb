from app import create_app, db
from app.models import UserConfig
import json

app = create_app()

def migrate_database():
    with app.app_context():
        # Verificar si la tabla existe
        try:
            # Intentar obtener la configuración existente
            config = UserConfig.query.first()
            
            if config:
                print("Configuración existente encontrada. Verificando nuevos campos...")
                
                # Verificar si los nuevos campos existen
                needs_update = False
                
                # Verificar file_blacklist
                if not hasattr(config, 'file_blacklist') or not config.file_blacklist:
                    print("Agregando campo file_blacklist...")
                    config.file_blacklist = json.dumps([])
                    needs_update = True
                
                # Verificar extension_blacklist
                if not hasattr(config, 'extension_blacklist') or not config.extension_blacklist:
                    print("Agregando campo extension_blacklist...")
                    default_extensions = [".tmp", ".log", ".cache", ".DS_Store", "Thumbs.db", ".pyc", ".pyo"]
                    config.extension_blacklist = json.dumps(default_extensions)
                    needs_update = True
                
                if needs_update:
                    db.session.commit()
                    print("Migración completada exitosamente!")
                else:
                    print("La base de datos ya está actualizada.")
            else:
                print("No se encontró configuración existente. Ejecute 'python init_db.py' primero.")
                
        except Exception as e:
            print(f"Error durante la migración: {e}")
            print("Recreando la base de datos...")
            
            # Si hay error, recrear la base de datos
            db.drop_all()
            db.create_all()
            
            # Crear configuración por defecto
            default_blacklist = ["venv", "node_modules", "dist", "build", ".git", "__pycache__", ".idea", ".vscode"]
            default_file_blacklist = []
            default_extension_blacklist = [".tmp", ".log", ".cache", ".DS_Store", "Thumbs.db", ".pyc", ".pyo"]
            
            config = UserConfig(
                blacklist=json.dumps(default_blacklist),
                file_blacklist=json.dumps(default_file_blacklist),
                extension_blacklist=json.dumps(default_extension_blacklist),
                max_depth=5,
                show_hidden=False,
                sort_option='name'
            )
            db.session.add(config)
            db.session.commit()
            print("Base de datos recreada con éxito!")

if __name__ == '__main__':
    migrate_database() 