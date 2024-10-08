import datetime

from peewee import *

from database.database import db


class BaseModel(Model):
    """
    Model base para todos os modelos
    """
    created_at = DateTimeField(default=datetime.datetime.now)
    updated_at = DateTimeField(default=datetime.datetime.now)

    def save(self, *args, **kwargs):
        """
        Salva o modelo no banco de dados
        """
        if self._pk is not None:
            self.updated_at = datetime.datetime.now()

        return super(BaseModel, self).save(*args, **kwargs)

    class Meta:
        """
        Meta informações do modelo
        """
        database = db


class Review(BaseModel):
    """
    Modelo de avaliação
    """
    customer_name = CharField()
    review_date = TextField()
    review_comment = IntegerField()
