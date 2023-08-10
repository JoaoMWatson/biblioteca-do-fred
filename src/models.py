from datetime import datetime

from sqlalchemy import String, Integer, ForeignKey
from sqlalchemy import orm as so
from src.app import db

from typing import Optional

class Item(db.Model):
    __tablename__ = 'itens'

    id: so.Mapped[int] = so.mapped_column(Integer, primary_key=True)
    title: so.Mapped[str] = so.mapped_column(String(255), index=True)
    author: so.Mapped[str] = so.mapped_column(String(255), index=True)
    number: so.Mapped[str] = so.mapped_column(String(3), nullable=True)
    collection_id: so.Mapped[int] = so.mapped_column(ForeignKey('collection.id'), 
                                             index=True)
    collection: so.Mapped['Collection'] = so.relationship(back_populates='collection')

