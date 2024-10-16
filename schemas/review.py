import datetime

from pydantic import BaseModel


class ReviewCreate(BaseModel):
    """
    Model para criação da avaliação
    """

    reviewer: str
    review_date: datetime.date
    review_comment: str

class ReviewUpdate(BaseModel):
    """
    Model para atualização da avaliação
    """

    review_comment: str

class ReviewResponse(BaseModel):
    """
    Model de resposta da avaliação
    """

    id: int
    reviewer: str
    review_date: datetime.date
    review_comment: str
    review_classification: str


class ReviewReport(BaseModel):
    """
    Model para relatório de avaliações
    """

    start_date: datetime.date
    end_date: datetime.date
    positive_reviews: int
    neutral_reviews: int
    negative_reviews: int
    total_reviews: int


class ReviewReportResponse(BaseModel):
    """
    Model de resposta do relatório de avaliações
    """

    report: ReviewReport
    reviews: list[ReviewResponse]
