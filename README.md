# Ingeniería Web: menú a domicilio

## Instalación

Usa Python 3.13, la versión del entorno de desarrollo, y ejecuta estos comandos desde la raíz del repositorio:

```bash
python -m venv .venv
```

Activa el entorno en macOS o Linux:

```bash
source .venv/bin/activate
```

En Windows (PowerShell):

```powershell
.venv\Scripts\Activate.ps1
```

Instala las dependencias y arranca la aplicación:

```bash
python -m pip install -r requirements.txt
cd menu_domicilio
python manage.py migrate
python manage.py runserver
```

Abre http://127.0.0.1:8000/ en el navegador. En algunos sistemas debes usar `python3` en lugar de `python` para crear el entorno virtual.

Para actualizar las dependencias registradas, con el entorno virtual activado y desde la raíz del repositorio:

```bash
python -m pip freeze > requirements.txt
```
