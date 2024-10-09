import datetime

from pydantic import BaseModel


class ReviewCreate(BaseModel):
    """
    Model de review para criação
    """

    reviewer: str
    review_date: datetime.date
    review_comment: str


class ReviewResponse(BaseModel):
    """
    Model de resposta da review
    """

    id: int
    reviewer: str
    review_date: datetime.date
    review_comment: str
    review_classification: str
