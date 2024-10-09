from .models import *


def initialize_reviews():
    """
    Inicializa os reviews
    """
    reviews = [
        {
            "reviewer": "John Doe",
            "review_date": "2021-01-01",
            "review_comment": "Ótimo produto",
            "review_rating": "positive",
        },
        {
            "reviewer": "Jane Doe",
            "review_date": "2021-01-02",
            "review_comment": "Produto ruim",
            "review_rating": "negative",
        },
        {
            "reviewer": "Alice",
            "review_date": "2021-01-03",
            "review_comment": "Produto médio",
            "review_rating": "neutral",
        },
        {
            "reviewer": "Bob",
            "review_date": "2021-01-04",
            "review_comment": "Excelente produto",
            "review_rating": "positive",
        },
    ]

    for review in reviews:
        Review.create(
            reviewer=review["reviewer"],
            review_date=review["review_date"],
            review_comment=review["review_comment"],
            review_classification=review["review_rating"],
        )


def init_db():
    """
    Inicializa o banco de dados
    """
    db.connect()

    tables = [Review]

    db.drop_tables(tables)
    db.create_tables(tables)

    initialize_reviews()

    db.close()
