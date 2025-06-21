# DirectoryTreeWeb 🌳

DirectoryTreeWeb es una aplicación web moderna y modular basada en Flask que genera representaciones visuales de estructuras de directorios. Los usuarios pueden ingresar una ruta local y la aplicación mostrará el árbol de directorios en una interfaz web elegante y responsive.

## ✨ Características Principales

### 🎨 **Interfaz Moderna**
- **Diseño responsive** con TailwindCSS y paleta de colores profesional
- **Layout de 3 columnas** optimizado para diferentes tamaños de pantalla
- **Cards organizadas** para mejor separación visual de funcionalidades
- **Iconos FontAwesome** para mejor experiencia de usuario
- **Tooltips de accesibilidad** en todos los botones sin texto

### 🌐 **Navegación Completa del Sistema**
- **Explorador de directorios modal** que permite navegar por todo el sistema
- **Detección automática del SO** (Windows: unidades C:\, D:\, etc. | Unix/Linux/Mac: desde /)
- **Navegación jerárquica** con botón para ir al directorio padre
- **Ruta actual visible** en tiempo real
- **Manejo de permisos** con mensajes de error apropiados

### ⚙️ **Configuración Avanzada**
- **Blacklist de carpetas** para excluir directorios específicos (venv, node_modules, etc.)
- **Profundidad máxima configurable** (1-20 niveles)
- **Mostrar archivos ocultos** opcional
- **Opciones de ordenamiento** (nombre, tamaño, fecha de modificación)
- **Configuración global persistente** en base de datos SQLite

### 🔧 **Funcionalidades de Salida**
- **Generación de árbol** con formato ASCII art profesional
- **Copiar al portapapeles** con feedback visual
- **Descargar como archivo** de texto
- **Limpiar salida** con redirección automática
- **Manejo de errores** con mensajes amigables

### 💾 **Gestión de Presets**
- **Guardar configuraciones** localmente en el navegador
- **Cargar presets** previamente guardados
- **Reset a valores por defecto** con un clic
- **Persistencia de configuración** entre sesiones

## 🚀 Instalación y Primer Uso

### Requisitos Previos
- Python 3.7 o superior
- Git (para clonar el repositorio)

### Pasos de Instalación

1. **Clona el repositorio:**
   ```bash
   git clone https://github.com/GeoShaPoH/DirectoryTreeWeb.git
   cd DirectoryTreeWeb
   ```

2. **Crea y activa el entorno virtual:**
   ```bash
   python -m venv venv
   # En Windows:
   venv\Scripts\activate
   # En macOS/Linux:
   source venv/bin/activate
   ```

3. **Instala las dependencias:**
   ```bash
   pip install -r requirements.txt
   ```

4. **⚠️ Inicializa la base de datos (OBLIGATORIO):**
   ```bash
   python init_db.py
   ```
   > **Importante:** Este paso es esencial antes de arrancar la aplicación por primera vez.

5. **Ejecuta la aplicación:**
   ```bash
   # Opción 1: Script automático
   # En Windows:
   run_directory_tree_web.bat
   # En macOS/Linux:
   bash run_directory_tree_web.sh
   
   # Opción 2: Manual
   python app.py
   ```

6. **Abre tu navegador:**
   ```
   http://localhost:5000
   ```

## 📖 Cómo Usar

### Generar un Árbol de Directorios

1. **Ingresa una ruta:**
   - Escribe manualmente la ruta del directorio
   - O usa el botón "Browse" para navegar por el sistema

2. **Configura las opciones** (opcional):
   - **Blacklist:** Agrega carpetas que quieres excluir
   - **Max Depth:** Define la profundidad máxima del árbol
   - **Show Hidden:** Marca para incluir archivos ocultos
   - **Sort By:** Elige el criterio de ordenamiento

3. **Genera el árbol:**
   - Haz clic en "Generate Tree"
   - El resultado se mostrará en el panel principal

4. **Gestiona la salida:**
   - **Copy:** Copia el árbol al portapapeles
   - **Download:** Descarga como archivo .txt
   - **Clear:** Limpia la salida y el campo de entrada

### Gestión de Configuración

- **Save Configuration:** Guarda los cambios en la base de datos
- **Save Preset:** Guarda la configuración actual en el navegador
- **Load Preset:** Carga una configuración previamente guardada
- **Reset to Defaults:** Restaura los valores por defecto

## 🏗️ Estructura del Proyecto

```
DirectoryTreeWeb/
├── app/                          # Aplicación principal
│   ├── __init__.py              # Inicialización de Flask
│   ├── config/                  # Configuración
│   │   ├── __init__.py
│   │   └── config.py           # Configuración de la app
│   ├── models/                  # Modelos de datos
│   │   ├── __init__.py
│   │   └── user_config.py      # Modelo de configuración global
│   ├── routes/                  # Rutas y endpoints
│   │   ├── __init__.py
│   │   ├── main.py             # Rutas principales
│   │   └── api.py              # API para navegación y árboles
│   ├── services/               # Servicios de negocio
│   │   ├── __init__.py
│   │   └── tree_generator.py   # Generador de árboles
│   └── utils/                  # Utilidades
│       └── __init__.py
├── templates/                   # Plantillas HTML
│   └── index.html              # Interfaz principal
├── static/                     # Archivos estáticos
│   └── favicon.svg             # Icono de la aplicación
├── app.py                      # Punto de entrada principal
├── run.py                      # Script de ejecución
├── init_db.py                  # Inicialización de base de datos
├── requirements.txt            # Dependencias de Python
├── run_directory_tree_web.bat  # Script de inicio (Windows)
├── run_directory_tree_web.sh   # Script de inicio (Unix/Linux)
└── README.md                   # Este archivo
```

## 🗄️ Base de Datos

- **SQLite** por defecto (configurable en `app/config/config.py`)
- **Tabla única:** `user_config` para configuración global
- **Inicialización automática** con `python init_db.py`
- **Migraciones** disponibles con Flask-Migrate

## 🔧 Configuración Avanzada

### Variables de Entorno
```bash
# Clave secreta para Flask
SECRET_KEY=tu_clave_secreta_aqui

# URL de la base de datos (opcional)
DATABASE_URL=sqlite:///instance/app.db
```

### Personalización
- **Colores:** Modifica las clases de TailwindCSS en `templates/index.html`
- **Blacklist por defecto:** Edita en `app/models/user_config.py`
- **Configuración de Flask:** Ajusta en `app/config/config.py`

## 🤝 Contribuciones

¡Las contribuciones son bienvenidas! Por favor:

1. **Fork** el repositorio
2. **Crea una rama** para tu feature (`git checkout -b feature/AmazingFeature`)
3. **Commit** tus cambios (`git commit -m 'Add some AmazingFeature'`)
4. **Push** a la rama (`git push origin feature/AmazingFeature`)
5. **Abre un Pull Request**

### Guías de Contribución
- Mantén el código limpio y bien documentado
- Sigue las convenciones de Python (PEP 8)
- Agrega tests para nuevas funcionalidades
- Actualiza la documentación según sea necesario

## 🐛 Reportar Problemas

Si encuentras un bug o tienes una sugerencia:

1. **Busca** en los issues existentes
2. **Crea un nuevo issue** con:
   - Descripción clara del problema
   - Pasos para reproducir
   - Información del sistema operativo
   - Capturas de pantalla (si aplica)

## 📄 Licencia

Este proyecto está bajo la **Licencia Apache 2.0**. Esta licencia proporciona:

- **Protección de propiedad intelectual** más robusta que MIT
- **Permite uso comercial** y distribución
- **Requiere atribución** y preservación de copyright
- **Protección de patentes** explícita
- **Contribuciones claramente definidas** para evitar conflictos

Ver el archivo [LICENSE](LICENSE) para los términos completos.

### ¿Por qué Apache 2.0?

La Licencia Apache 2.0 es ideal para proyectos que quieren:
- Mantener el código abierto y colaborativo
- Proteger mejor la propiedad intelectual del autor original
- Permitir uso comercial sin restricciones
- Definir claramente qué constituye una contribución
- Proporcionar protección de patentes explícita

## 👨‍💻 Autor

**GeoShaPoh** - [GitHub](https://github.com/GeoShaPoH)

## 🙏 Agradecimientos

- **Flask** por el framework web
- **TailwindCSS** por el sistema de diseño
- **FontAwesome** por los iconos
- **SQLAlchemy** por el ORM
- **Comunidad open source** por las herramientas y librerías utilizadas

---

⭐ **Si este proyecto te es útil, considera darle una estrella en GitHub!**