from peewee import PostgresqlDatabase

from libs.utils import settings

db = PostgresqlDatabase(
    settings.POSTGRES_DB,
    user=settings.POSTGRES_USER,
    password=settings.POSTGRES_PASSWORD,
    host=settings.POSTGRES_HOST,
    port=settings.POSTGRES_PORT,
)
