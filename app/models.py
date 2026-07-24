"""
Modelos de datos utilizados por la aplicación.

Actualmente la plataforma cuenta con el modelo Cuidador, que representa
los perfiles almacenados en la base de datos SQLite.
"""

from datetime import datetime

from sqlalchemy import Boolean, DateTime, Integer, String, Text
from sqlalchemy.orm import Mapped, mapped_column

from .extensions import db


class Cuidador(db.Model):
    """
    Representa a un cuidador registrado en la plataforma.

    Cada instancia de esta clase corresponde a un registro de la tabla
    cuidadores y puede ser creada, consultada, editada o eliminada
    mediante las operaciones CRUD.
    """

    # Nombre de la tabla en la base de datos.
    __tablename__ = "cuidadores"

    # Identificador único del registro.
    id: Mapped[int] = mapped_column(primary_key=True)

    # Datos personales y de contacto.
    nombre: Mapped[str] = mapped_column(
        String(120),
        nullable=False,
    )

    correo: Mapped[str] = mapped_column(
        String(120),
        unique=True,
        nullable=False,
        index=True,
    )

    telefono: Mapped[str] = mapped_column(
        String(30),
        nullable=False,
    )

    comuna: Mapped[str] = mapped_column(
        String(80),
        nullable=False,
        index=True,
    )

    # Información profesional del cuidador.
    especialidad: Mapped[str] = mapped_column(
        String(100),
        nullable=False,
        index=True,
    )

    experiencia_anios: Mapped[int] = mapped_column(
        Integer,
        nullable=False,
        default=0,
    )

    tarifa_diaria: Mapped[int] = mapped_column(
        Integer,
        nullable=False,
    )

    descripcion: Mapped[str] = mapped_column(
        Text,
        nullable=False,
        default="",
    )

    # Estado del perfil dentro de la plataforma.
    disponible: Mapped[bool] = mapped_column(
        Boolean,
        nullable=False,
        default=True,
    )

    estado_validacion: Mapped[str] = mapped_column(
        String(20),
        nullable=False,
        default="Pendiente",
    )

    # Fecha automática en que se creó el registro.
    creado_en: Mapped[datetime] = mapped_column(
        DateTime,
        nullable=False,
        default=datetime.utcnow,
    )

    def __repr__(self) -> str:
        """
        Retorna una representación legible del cuidador.

        Esta representación es útil al inspeccionar objetos desde
        la consola o durante la depuración.
        """

        return f"<Cuidador {self.nombre}>"