from .models import db, Review
from libs.utils import settings


class SeedDatabase:
    """
    Seed do banco de dados para testes
    """

    def __init__(self, drop_tables=False):
        """
        Inicializa o SeedDatabase
        :param drop_tables: Se True, as tabelas serão apagadas
        """
        self._db = db
        self.tables = [Review]
        self.drop_tables = drop_tables

        self.reviews = [
            {
                "reviewer": "John Doe",
                "review_date": "2021-01-01",
                "review_comment": "Ótimo produto",
                "review_classification": "positive",
            },
            {
                "reviewer": "Jane Doe",
                "review_date": "2021-01-02",
                "review_comment": "Produto ruim",
                "review_classification": "negative",
            },
            {
                "reviewer": "Alice",
                "review_date": "2021-01-03",
                "review_comment": "Produto médio",
                "review_classification": "neutral",
            },
            {
                "reviewer": "Bob",
                "review_date": "2021-01-04",
                "review_comment": "Excelente produto",
                "review_classification": "positive",
            },
        ]

    def initialize_reviews(self):
        """
        Inicializa os reviews
        """
        for review in self.reviews:
            Review.create(
                reviewer=review["reviewer"],
                review_date=review["review_date"],
                review_comment=review["review_comment"],
                review_classification=review["review_classification"],
            )

    def __enter__(self):
        """
        Inicializa o banco de dados
        """
        self._db.connect()

        if self.drop_tables:
            if settings.ENVIRONMENT not in ["development", "testing"]:
                raise EnvironmentError("Environment must be development or testing to use `drop_tables`")

            self._db.drop_tables(self.tables)

        self._db.create_tables(self.tables)

        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        """
        Fecha o banco de dados
        """
        self._db.close()
