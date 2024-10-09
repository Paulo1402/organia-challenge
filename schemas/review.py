import datetime

from pydantic import BaseModel


class ReviewCreate(BaseModel):
    """
    Model de review para criação
    """

    reviewer: str
    review_date: datetime.datetime
    review_comment: int


class ReviewResponse(BaseModel):
    """
    Model de resposta da review
    """

    id: int
    reviewer: str
    review_date: datetime.datetime
    review_comment: int
    review_rating: str