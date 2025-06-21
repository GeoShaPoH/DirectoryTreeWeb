from app import create_app, db
from app.models import UserConfig

app = create_app()

with app.app_context():
    # Crear todas las tablas
    db.create_all()
    print("Base de datos inicializada correctamente!")
    
    # Verificar si existe configuración global
    config = UserConfig.query.first()
    if not config:
        print("Creando configuración global por defecto...")
        config = UserConfig()
        db.session.add(config)
        db.session.commit()
        print("Configuración global creada!")
    else:
        print("Configuración global ya existe.") 