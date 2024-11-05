import pytest
from fastapi.testclient import TestClient

from main import app
from database import SeedDatabase

client = TestClient(app)


@pytest.fixture(scope="module", autouse=True, name="seed")
def seed_database():
    """
    Alimenta o banco de dados com avaliações
    """
    with SeedDatabase(drop_tables=True) as database:
        database.initialize_reviews()
        yield database


def test_read_reviews(seed):
    """
    Testa a leitura de todas as avaliações
    :param seed: SeedDatabase
    """
    response = client.get("/reviews/")
    reviews = response.json()

    assert response.status_code == 200
    assert len(reviews) == len(seed.reviews)

    for i, review in enumerate(reviews):
        assert review["id"] == i + 1
        assert review["reviewer"] == seed.reviews[i]["reviewer"]
        assert review["review_date"] == seed.reviews[i]["review_date"]
        assert review["review_comment"] == seed.reviews[i]["review_comment"]
        assert (
            review["review_classification"] == seed.reviews[i]["review_classification"]
        )


def test_read_review(seed):
    """
    Testa a leitura de uma avaliação específica
    :param seed: SeedDatabase
    """
    response = client.get("/reviews/1")
    review = response.json()

    assert response.status_code == 200
    assert review["id"] == 1
    assert review["reviewer"] == seed.reviews[0]["reviewer"]
    assert review["review_date"] == seed.reviews[0]["review_date"]
    assert review["review_comment"] == seed.reviews[0]["review_comment"]
    assert review["review_classification"] == seed.reviews[0]["review_classification"]


def test_create_review(seed):
    """
    Testa a criação de uma avaliação
    :param seed: SeedDatabase
    """
    new_review = {
        "reviewer": "Charlie",
        "review_date": "2021-01-05",
        "review_comment": "Produto excelente",
    }

    response = client.post("/reviews/", json=new_review)
    review = response.json()

    assert response.status_code == 201
    assert review["reviewer"] == new_review["reviewer"]
    assert review["review_date"] == new_review["review_date"]
    assert review["review_comment"] == new_review["review_comment"]
    assert review["review_classification"] == "Positivo"


def test_read_review_report(seed):
    """
    Testa a leitura do relatório de avaliações
    :param seed: SeedDatabase
    """
    response = client.get(
        "/reviews/report", params={"start_date": "2021-01-01", "end_date": "2021-01-04"}
    )
    report = response.json()

    assert response.status_code == 200
    assert report["report"]["start_date"] == seed.reviews[0]["review_date"]
    assert report["report"]["end_date"] == seed.reviews[-1]["review_date"]
    assert report["report"]["positive_reviews"] == 2
    assert report["report"]["neutral_reviews"] == 1
    assert report["report"]["negative_reviews"] == 1
    assert report["report"]["total_reviews"] == len(seed.reviews)
    assert len(report["reviews"]) == len(seed.reviews)
