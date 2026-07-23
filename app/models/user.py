from __future__ import annotations

import uuid
from datetime import datetime

from sqlalchemy import Boolean, DateTime, String, func

from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import Mapped, mapped_column

from app.db.base_class import Base

class User(Base):
    """
    Modelo que representa um usuário do sistema
    """

    __tablename__="users"

    id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid.uuid4,
    )

    name: Mapped[uuid.UUID] = mapped_column(
        String(150),
        nullable=False
    )

    email: Mapped[uuid.UUID] = mapped_column(
        String(255),
        unique=True,
        index=True,
    )

    is_active: Mapped[uuid.UUID] = mapped_column(
        DateTime(timezone=True),
        server_default=func.now(),
        nullable=False,
    )

    on_update: Mapped[uuid.UUID] = mapped_column(
        DateTime(timezone=True),
        server_default=func.now(),
        onupdate=func.now(),
        nullable=False,
    )
