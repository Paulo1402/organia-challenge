import dotenv
from fastapi import FastAPI

from database import SeedDatabase
from routes.reviews import router as reviews_router


API_VERSION = "v1"

dotenv.load_dotenv()

app = FastAPI(root_path=f"/api/{API_VERSION}", title="OrganIA Challenge")
app.include_router(reviews_router, prefix="/reviews", tags=["reviews"])

with SeedDatabase(drop_tables=True) as database:
    database.initialize_reviews()
