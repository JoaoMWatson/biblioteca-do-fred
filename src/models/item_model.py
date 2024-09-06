import os
from datetime import datetime

import sqlalchemy as sa
from alchemical import Model
from flask import current_app
from sqlalchemy import orm as orm

from src.date import naive_utcnow
from src.app import db


class Item(Model):
    __tablename__ = 'items'

    id: orm.Mapped[int] = orm.mapped_column(sa.Integer, primary_key=True)
    title: orm.Mapped[str] = orm.mapped_column(sa.String(255), nullable=False)
    gender: orm.Mapped[str] = orm.mapped_column(sa.String(255), nullable=False)
    release_date: orm.Mapped[datetime] = orm.mapped_column(
        sa.DateTime, nullable=False
    )
    timestamp: orm.Mapped[datetime] = orm.mapped_column(
        sa.DateTime, default=naive_utcnow, nullable=False, index=True
    )
    edition: orm.Mapped[str] = orm.mapped_column(sa.String(30), nullable=True)
    # id_author:
    # id_publisher:
