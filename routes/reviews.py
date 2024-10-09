import datetime

from fastapi import APIRouter, HTTPException

from schemas.review import ReviewResponse
from database.models import Review

router = APIRouter()


@router.get("/", response_model=list[ReviewResponse])
async def read_reviews(page: int = 0, page_size: int = 10):
    """
    Retorna uma lista de reviews

    :param page:
    :param page_size:
    :return:
    """
    reviews = Review.select().offset(page).limit(page_size)
    reviews_list = []

    for review in reviews:
        reviews_list.append(
            ReviewResponse(
                id=review.id,
                reviewer=review.reviewer,
                review_date=review.review_date,
                review_comment=review.review_comment,
                review_rating=review.review_rating,
            )
        )

    return reviews_list


@router.get("/report")
async def report_reviews(start_date: datetime.date, end_date: datetime.date):
    """
    Retorna um relatório de reviews

    :param start_date:
    :param end_date:
    :return:
    """
    return {"message": "Reporting all reviews"}


@router.get("/{review_id}")
async def read_review(review_id: int):
    """
    Retorna um review específico

    :param review_id:
    :return:
    """
    review = Review.get_or_none(id=review_id)

    if not review:
        raise HTTPException(status_code=404, detail="Review not found")

    return ReviewResponse(
        id=review.id,
        reviewer=review.reviewer,
        review_date=review.review_date,
        review_comment=review.review_comment,
        review_rating=review.review_rating,
    )


@router.post("/")
async def create_review():
    """
    Cria um novo review

    :return:
    """
    return {"review_id": 2, "content": "Awesome product!"}
