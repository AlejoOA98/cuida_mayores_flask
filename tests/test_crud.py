"""
Pruebas automatizadas para las operaciones CRUD de cuidadores.

La prueba verifica el flujo completo:

1. Crear un cuidador.
2. Consultar el resultado.
3. Editar sus datos.
4. Eliminar el registro.
5. Confirmar que ya no existe en la base de datos.
"""

from pathlib import Path

from app import create_app
from app.extensions import db
from app.models import Cuidador


def build_app(tmp_path: Path):
    """
    Crea una aplicación Flask aislada para las pruebas.

    La aplicación utiliza una base SQLite temporal, evitando modificar
    la base de datos real del proyecto.

    Args:
        tmp_path: carpeta temporal entregada por pytest.

    Returns:
        Una aplicación Flask configurada en modo de prueba.
    """

    # Define una base de datos temporal.
    database = tmp_path / "test.db"

    # Crea la aplicación con una configuración exclusiva para pruebas.
    app = create_app(
        {
            "TESTING": True,
            "SECRET_KEY": "test",
            "SQLALCHEMY_DATABASE_URI": f"sqlite:///{database}",
        }
    )

    return app


def test_crud_completo(tmp_path):
    """
    Verifica el funcionamiento completo del CRUD.

    La prueba crea un cuidador, modifica sus datos, lo elimina
    y comprueba finalmente que no permanezca en la base de datos.
    """

    # Crea una aplicación y un cliente HTTP de prueba.
    app = build_app(tmp_path)
    client = app.test_client()

    # CREATE:
    # Envía un formulario para registrar un nuevo cuidador.
    respuesta = client.post(
        "/cuidadores/nuevo",
        data={
            "nombre": "Ana López",
            "correo": "ana@example.com",
            "telefono": "+56 9 1111 2222",
            "comuna": "Santiago",
            "especialidad": "Cuidado general",
            "experiencia_anios": "4",
            "tarifa_diaria": "45000",
            "estado_validacion": "Pendiente",
            "descripcion": "Perfil de prueba",
            "disponible": "on",
        },
        follow_redirects=True,
    )

    # Comprueba que la solicitud fue procesada correctamente.
    assert respuesta.status_code == 200

    # Comprueba que el nombre aparece en la respuesta HTML.
    assert b"Ana L" in respuesta.data

    # READ:
    # Obtiene el registro creado directamente desde la base de datos.
    with app.app_context():
        cuidador = db.session.execute(
            db.select(Cuidador)
        ).scalar_one()

        cuidador_id = cuidador.id

    # UPDATE:
    # Envía nuevos datos para modificar el perfil.
    respuesta = client.post(
        f"/cuidadores/{cuidador_id}/editar",
        data={
            "nombre": "Ana López",
            "correo": "ana@example.com",
            "telefono": "+56 9 1111 2222",
            "comuna": "Providencia",
            "especialidad": "TENS",
            "experiencia_anios": "5",
            "tarifa_diaria": "55000",
            "estado_validacion": "Aprobado",
            "descripcion": "Perfil actualizado",
            "disponible": "on",
        },
        follow_redirects=True,
    )

    # Comprueba que la edición fue procesada.
    assert respuesta.status_code == 200

    # Comprueba que los nuevos valores aparecen en la respuesta.
    assert b"Providencia" in respuesta.data
    assert b"Aprobado" in respuesta.data

    # DELETE:
    # Envía la solicitud para eliminar el perfil.
    respuesta = client.post(
        f"/cuidadores/{cuidador_id}/eliminar",
        follow_redirects=True,
    )

    # Comprueba que la eliminación fue procesada correctamente.
    assert respuesta.status_code == 200
    assert b"eliminado correctamente" in respuesta.data

    # Confirma directamente en la base que no queden registros.
    with app.app_context():
        cuidador_eliminado = db.session.execute(
            db.select(Cuidador)
        ).scalar_one_or_none()

        assert cuidador_eliminado is None