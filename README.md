# Cuida a tus Mayores — CRUD con Flask

Prototipo  para la **Sumativa 2 de Taller de Desarrollo Web y Móvil**. 

## Dentro de las funcionalidades

- Posibildiad de crear perfiles de cuidadores.
- Listar, buscar y filtrar cuidadores.
- Consultar el detalle de un perfil.
- Editar antecedentes, disponibilidad y estado de validación.
- Eliminar registros con confirmación.
- Dashboard con indicadores básicos.
- Validaciones de formulario y mensajes de resultado.
- Base de datos local SQLite.

## Tecnologías

- Python 3.11 
- Flask.
- Flask-SQLAlchemy.
- SQLite.
- HTML, CSS y Jinja.

## Instalación en Windows

1. Abre PowerShell o CMD dentro de la carpeta del proyecto.
2. Crea un entorno virtual:

```powershell
py -m venv .venv
```

3. Actívalo:

```powershell
.venv\Scripts\activate
```

4. Instala las dependencias:

```powershell
pip install -r requirements.txt
```

5. Crea la base de datos con datos de ejemplo:

```powershell
python seed.py
```

6. Ejecuta la aplicación:

```powershell
python run.py
```

7. Abre en el navegador:

```text
http://127.0.0.1:5000
```

## Prueba rápida del CRUD

1. Entra a **Cuidadores**.
2. Presiona **Nuevo cuidador** y registra un perfil.
3. Abre el detalle del registro creado.
4. Edita la comuna o el estado de validación.
5. Elimina el registro desde la pantalla de confirmación.

## Estructura y patrón

El proyecto usa:

- **Application Factory:** crea la aplicación dentro de `create_app()`.
- **Blueprint:** agrupa las rutas del módulo `cuidadores`.
- **Modelo:** `Cuidador` representa la tabla principal.
- **Vistas y controladores:** las rutas reciben solicitudes, ejecutan la lógica y renderizan plantillas.
- **Plantillas Jinja:** presentan los datos en HTML.

Esta separación corresponde a una adaptación sencilla del patrón **MVC**:

- Modelo: `app/models.py`.
- Vista: `app/templates/`.
- Controlador: `app/cuidadores/routes.py`.

## Pruebas automatizadas opcionales

Instala pytest:

```powershell
pip install pytest
```

Ejecuta:

```powershell
pytest -q
```
