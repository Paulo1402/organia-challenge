from .models import *


def init_db():
    """
    Inicializa o banco de dados
    """
    db.connect()

    tables = [Review]

    db.drop_tables(tables)
    db.create_tables(tables)

    db.close()
