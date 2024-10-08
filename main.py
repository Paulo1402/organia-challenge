from typing import Union

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.post("/reviews")
def classify_reviews() -> Union[str, int]:
    return "positive"


@app.get("/reviews")
def get_reviews() -> Union[str, list]:
    return ["review1", "review2"]


@app.get("/reviews/report")
def get_reviews_report(start_date: str, end_date: str):
    return {"start_date": start_date, "end_date": end_date}


@app.get("/reviews/{review_id}")
def get_review(review_id: int):
    return {"review_id": review_id}


