"""
Script para crear la base de datos con registros de ejemplo.

Este archivo se utiliza durante el desarrollo y la demostración del
prototipo. Al ejecutarse, elimina los datos anteriores y crea nuevamente
las tablas con un conjunto conocido de cuidadores.
"""

from app import create_app
from app.extensions import db
from app.models import Cuidador


# Crea una instancia de la aplicación para acceder a su configuración.
app = create_app()


# Datos iniciales utilizados para poblar la base SQLite.
CUIDADORES = [
    {
        "nombre": "María Pérez Soto",
        "correo": "maria.perez@example.com",
        "telefono": "+56 9 5555 1001",
        "comuna": "Ñuñoa",
        "especialidad": "Cuidado general",
        "experiencia_anios": 5,
        "tarifa_diaria": 45000,
        "disponible": True,
        "estado_validacion": "Aprobado",
        "descripcion": (
            "Experiencia en acompañamiento, administración de rutinas "
            "y apoyo en actividades diarias."
        ),
    },
    {
        "nombre": "Carlos Rojas Díaz",
        "correo": "carlos.rojas@example.com",
        "telefono": "+56 9 5555 1002",
        "comuna": "Providencia",
        "especialidad": "TENS",
        "experiencia_anios": 8,
        "tarifa_diaria": 60000,
        "disponible": False,
        "estado_validacion": "Aprobado",
        "descripcion": (
            "Técnico en enfermería con experiencia en cuidado "
            "domiciliario de personas mayores."
        ),
    },
    {
        "nombre": "Camila Fuentes Lagos",
        "correo": "camila.fuentes@example.com",
        "telefono": "+56 9 5555 1003",
        "comuna": "Macul",
        "especialidad": "Acompañamiento",
        "experiencia_anios": 2,
        "tarifa_diaria": 38000,
        "disponible": True,
        "estado_validacion": "Pendiente",
        "descripcion": (
            "Acompañamiento, preparación de alimentos simples "
            "y apoyo en actividades recreativas."
        ),
    },
]


# El contexto de aplicación permite utilizar la base de datos
# fuera de una solicitud HTTP.
with app.app_context():
    # Elimina las tablas existentes y todos sus datos.
    db.drop_all()

    # Crea nuevamente las tablas definidas por los modelos.
    db.create_all()

    # Convierte cada diccionario en una instancia de Cuidador.
    cuidadores = [
        Cuidador(**datos)
        for datos in CUIDADORES
    ]

    # Agrega todos los perfiles de ejemplo a la sesión.
    db.session.add_all(cuidadores)

    # Guarda definitivamente los datos en SQLite.
    db.session.commit()

    print("Base de datos creada con datos de ejemplo.")