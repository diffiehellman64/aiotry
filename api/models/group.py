from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from models.base import Base


class Group(Base):
    __tablename__ = 'groups'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    user = relationship('User')

    def __repr__(self):
        return f'Группа [ID: {self.id}, Название: {self.name}]'