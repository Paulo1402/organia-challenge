import dotenv
from fastapi import FastAPI

from database import init_db
from routes.reviews import router as reviews_router


API_VERSION = "v1"

dotenv.load_dotenv()

app = FastAPI(root_path=f'/api/{API_VERSION}', title='OrganIA Challenge')
app.include_router(reviews_router, prefix='/reviews', tags=['reviews'])

init_db()
