import os
from datetime import datetime

import sqlalchemy as sa
from alchemical import Model
from sqlalchemy import orm as orm

from src.date import naive_utcnow


class Author(Model):
    __tablename__ = 'author'

    id: orm.Mapped[int] = orm.mapped_column(sa.Integer, primary_key=True)
    name: orm.Mapped[str] = orm.mapped_column(sa.String(255), nullable=False, index=True, unique=True)
    timestamp: orm.Mapped[datetime] = orm.mapped_column(
        sa.DateTime, default=naive_utcnow, nullable=False, index=True
    )
    origin: orm.Mapped[str] = orm.mapped_column(sa.String(255), nullable=True)
