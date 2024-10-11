import dotenv
from fastapi import FastAPI

from database import SeedDatabase
from routes.reviews import router as reviews_router


API_VERSION = "v1"

dotenv.load_dotenv()

app = FastAPI(
    root_path=f"/api/{API_VERSION}",
    title="OrganIA Challenge",
    description="Desafio OrganIA",
)
app.include_router(reviews_router, prefix="/reviews", tags=["reviews"])

# Alimenta o banco de dados com avaliações
with SeedDatabase(drop_tables=True) as database:
    database.initialize_reviews()
