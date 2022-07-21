from .base import create_db, Session
from .user import User
from .group import Group


def create_database(load_fake_data: bool = True):
    create_db()