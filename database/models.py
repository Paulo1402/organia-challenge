import datetime

from peewee import Model, DateTimeField, TextField, CharField, DateField

from database.database import db
from services.review_classifier import SentimentClassification


class BaseModel(Model):
    """
    Model base para todos os outros
    """

    created_at = DateTimeField(default=datetime.datetime.now)
    updated_at = DateTimeField(default=datetime.datetime.now)

    def save(self, *args, **kwargs) -> bool | int:
        """
        Salva o model no banco de dados
        """
        if self._pk is not None:
            self.updated_at = datetime.datetime.now()

        return super(BaseModel, self).save(*args, **kwargs)

    class Meta:
        """
        Meta informações do model
        """

        database = db


class Review(BaseModel):
    """
    Review Model
    """

    reviewer = CharField()
    review_date = DateField()
    review_comment = TextField()
    review_classification = CharField(
        choices=[(tag, tag.value) for tag in SentimentClassification]
    )
    classification_model = TextField(null=True)
