from app import create_app
from app.extensions import db
from app.models import Cuidador

app = create_app()

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
        "descripcion": "Experiencia en acompañamiento, administración de rutinas y apoyo en actividades diarias.",
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
        "descripcion": "Técnico en enfermería con experiencia en cuidado domiciliario de personas mayores.",
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
        "descripcion": "Acompañamiento, preparación de alimentos simples y apoyo en actividades recreativas.",
    },
]

with app.app_context():
    db.drop_all()
    db.create_all()
    db.session.add_all([Cuidador(**datos) for datos in CUIDADORES])
    db.session.commit()
    print("Base de datos creada con datos de ejemplo.")
