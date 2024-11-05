import sys
import os

# Adiciona o diretório do arquivo main.py ao sys.path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

import dotenv
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from database import SeedDatabase
from routes.reviews import router as reviews_router


API_VERSION = "v1"

dotenv.load_dotenv()

app = FastAPI(
    root_path=f"/api/{API_VERSION}",
    title="OrganIA Challenge",
    description="Desafio OrganIA",
)
# noinspection PyTypeChecker
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.include_router(reviews_router, prefix="/reviews", tags=["reviews"])

# Alimenta o banco de dados com avaliações
with SeedDatabase(drop_tables=True) as database:
    database.initialize_reviews()


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0")
