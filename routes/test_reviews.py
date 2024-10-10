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
    response = client.get("/reviews/")
    reviews = response.json()

    assert response.status_code == 200
    assert len(reviews) == len(seed.reviews)

