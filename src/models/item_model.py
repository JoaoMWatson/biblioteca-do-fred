import os
from datetime import datetime

import sqlalchemy as sa
from alchemical import Model
from sqlalchemy import orm as orm

from src.date import naive_utcnow


class Item(Model):
    __tablename__ = 'items'

    id: orm.Mapped[int] = orm.mapped_column(sa.Integer, primary_key=True)
    title: orm.Mapped[str] = orm.mapped_column(sa.String(255), nullable=False)
    category: orm.Mapped[int] = orm.mapped_column(sa.Integer, nullable=False, index=True) # ENUM: 1-> livro 2-> revista 3-> manga 4-> HQ 5-> outro
    gender: orm.Mapped[str] = orm.mapped_column(sa.String(70), nullable=False)
    release_date: orm.Mapped[datetime] = orm.mapped_column(
        sa.DateTime, nullable=False
    )
    timestamp: orm.Mapped[datetime] = orm.mapped_column(
        sa.DateTime, default=naive_utcnow, nullable=False, index=True
    )
    edition: orm.Mapped[str] = orm.mapped_column(sa.String(30), nullable=True)
    # id_author:
    # id_publisher:
