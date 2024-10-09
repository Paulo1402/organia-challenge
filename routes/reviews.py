import datetime

from fastapi import APIRouter, HTTPException

from schemas.review import ReviewResponse, ReviewCreate
from database.models import Review
from services.review_classifier import BertReviewClassifier

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
                review_classification=review.review_classification,
            )
        )

    return reviews_list


@router.get("/report")
async def report_reviews(
    start_date: datetime.date, end_date: datetime.date = datetime.date.today()
):
    """
    Retorna um relatório de reviews

    :param start_date:
    :param end_date:
    :return:
    """
    reviews = Review.select().where(
        (Review.review_date >= start_date) & (Review.review_date <= end_date)
    )

    positive_reviews = 0
    neutral_reviews = 0
    negative_reviews = 0

    reviews_list = []

    for review in reviews:
        if review.review_classification == "positive":
            positive_reviews += 1

        if review.review_classification == "neutral":
            neutral_reviews += 1

        if review.review_classification == "negative":
            negative_reviews += 1

        reviews_list.append(
            ReviewResponse(
                id=review.id,
                reviewer=review.reviewer,
                review_date=review.review_date,
                review_comment=review.review_comment,
                review_classification=review.review_classification,
            )
        )

    return {
        "report": {
            "positive_reviews": positive_reviews,
            "neutral_reviews": neutral_reviews,
            "negative_reviews": negative_reviews,
            "total_reviews": positive_reviews + neutral_reviews + negative_reviews,
        },
        "reviews": reviews_list,
    }


@router.get("/{review_id}", response_model=ReviewResponse)
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
        review_classification=review.review_classification,
    )


@router.post("/", response_model=ReviewResponse)
async def create_review(review: ReviewCreate):
    """
    Cria um novo review

    :param review:
    :return:
    """

    classifier = BertReviewClassifier()
    classification = classifier.classify(review.review_comment)

    review = Review.create(
        reviewer=review.reviewer,
        review_date=review.review_date,
        review_comment=review.review_comment,
        review_classification=classification,
    )

    return ReviewResponse(
        id=review.id,
        reviewer=review.reviewer,
        review_date=review.review_date,
        review_comment=review.review_comment,
        review_classification=review.review_classification,
    )
