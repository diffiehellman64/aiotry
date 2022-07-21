from sqlalchemy import Column, Integer, String, ForeignKey

from models.base import Base


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    surname = Column(String)
    name = Column(String)
    patronymic = Column(String)
    age = Column(Integer)
    group = Column(Integer, ForeignKey('groups.id'))

    def __init__(self, full_name: list[str], age: int):
        self.surname = full_name[0]
        self.name = full_name[1]
        self.patronymic = full_name[2]
        self.age = age

    def __repr__(self):
        info: str = f'User [ФИО: {self.surname} {self.name} {self.patronymic}, Возраст: {self.age}]'
        return info