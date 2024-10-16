import datetime

from fastapi import APIRouter, HTTPException, Response

from schemas.review import (
    ReviewResponse,
    ReviewCreate,
    ReviewReportResponse,
    ReviewReport,
    ReviewUpdate,
)
from database.models import Review
from services.review_classifier import (
    SentimentClassification,
    ReviewClassifierFactory,
    InvalidClassifierError,
    ClassifierError,
)

router = APIRouter()


@router.get("/classifiers", name="Listar classificadores", description="Retorna uma lista de classificadores disponíveis")
async def list_classifiers() -> list[str]:
    """
    Retorna uma lista de classificadores disponíveis

    :return: Lista de classificadores disponíveis
    """
    return ReviewClassifierFactory().classifiers


@router.get(
    "/",
    name="Listar avaliações",
    description="Retorna uma lista de avaliações",
    response_model=list[ReviewResponse],
)
async def read_reviews(response: Response, page: int = 0, page_size: int = 10) -> list[ReviewResponse]:
    """
    Retorna uma lista de avaliações

    :param response: Resposta
    :param page: Página
    :param page_size: Tamanho da página
    :return: Lista de avaliações
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

    response.headers["X-Total-Count"] = str(Review.select().count())
    response.headers["X-Page-Size"] = str(page_size)
    response.headers["X-Page"] = str(page)

    return reviews_list


@router.get(
    "/report",
    name="Relatório de avaliações",
    description="Retorna um relatório de avaliações dentro de um intervalo de datas",
    response_model=ReviewReportResponse,
)
async def report_reviews(
    start_date: datetime.date, end_date: datetime.date = datetime.date.today()
) -> ReviewReportResponse:
    """
    Retorna um relatório de avaliações dentro de um intervalo de datas

    :param start_date: Data inicial
    :param end_date: Data final
    :return: Relatório de avaliações
    """
    reviews = Review.select().where(
        (Review.review_date >= start_date) & (Review.review_date <= end_date)
    )

    positive_reviews = 0
    neutral_reviews = 0
    negative_reviews = 0

    reviews_list = []

    for review in reviews:
        if review.review_classification == SentimentClassification.POSITIVE.value:
            positive_reviews += 1

        if review.review_classification == SentimentClassification.NEUTRAL.value:
            neutral_reviews += 1

        if review.review_classification == SentimentClassification.NEGATIVE.value:
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

    return ReviewReportResponse(
        report=ReviewReport(
            start_date=start_date,
            end_date=end_date,
            positive_reviews=positive_reviews,
            neutral_reviews=neutral_reviews,
            negative_reviews=negative_reviews,
            total_reviews=len(reviews_list),
        ),
        reviews=reviews_list,
    )


@router.get(
    "/{review_id}",
    name="Consultar avaliação",
    description="Retorna uma avaliação específica",
    response_model=ReviewResponse,
)
async def read_review(review_id: int) -> ReviewResponse:
    """
    Retorna uma avaliação específica

    :param review_id: ID da avaliação
    :return: Avaliação
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


@router.post(
    "/",
    name="Criar avaliação",
    description="Cria uma nova avaliação",
    response_model=ReviewResponse,
    status_code=201,
)
async def create_review(
    review: ReviewCreate, classifier: str = "bert"
) -> ReviewResponse:
    """
    Cria uma nova avaliação

    :param review: Avaliação a ser criada
    :param classifier: Classificador a ser utilizado

    :return: Avaliação criada
    """

    try:
        classifier = ReviewClassifierFactory.create_review_classifier(classifier)
        classification = classifier.classify(review.review_comment)
    except InvalidClassifierError:
        available_classifiers = ", ".join(ReviewClassifierFactory().classifiers)

        raise HTTPException(
            status_code=400,
            detail=f"Invalid classifier! Available classifiers: {available_classifiers}",
        )
    except ClassifierError:
        raise HTTPException(
            status_code=500,
            detail="An error occurred while classifying the review",
        )

    review = Review.create(
        reviewer=review.reviewer,
        review_date=review.review_date,
        review_comment=review.review_comment,
        review_classification=classification.value,
    )

    return ReviewResponse(
        id=review.id,
        reviewer=review.reviewer,
        review_date=review.review_date,
        review_comment=review.review_comment,
        review_classification=review.review_classification,
    )

@router.put(
    "/{review_id}",
    name="Atualizar avaliação",
    description="Atualiza uma avaliação existente",
    response_model=ReviewResponse,
)
async def update_review(review_id: int, review: ReviewCreate, classifier: str) -> ReviewResponse:
    """
    Atualiza uma avaliação existente

    :param review_id: ID da avaliação
    :param review: Avaliação a ser atualizada
    :param classifier: Classificador a ser utilizado
    :return: Avaliação atualizada
    """
    old_review = Review.get_or_none(id=review_id)

    if not old_review:
        raise HTTPException(status_code=404, detail="Review not found")

    try:
        classifier = ReviewClassifierFactory.create_review_classifier(classifier)
        classification = classifier.classify(review.review_comment)
    except InvalidClassifierError:
        available_classifiers = ", ".join(ReviewClassifierFactory().classifiers)

        raise HTTPException(
            status_code=400,
            detail=f"Invalid classifier! Available classifiers: {available_classifiers}",
        )
    except ClassifierError:
        raise HTTPException(
            status_code=500,
            detail="An error occurred while classifying the review",
        )

    old_review.reviewer = review.reviewer
    old_review.review_date = review.review_date
    old_review.review_comment = review.review_comment
    old_review.review_classification = classification.value

    old_review.save()

    return ReviewResponse(
        id=review.id,
        reviewer=review.reviewer,
        review_date=review.review_date,
        review_comment=review.review_comment,
        review_classification=classification.value,
    )

@router.delete(
    "/{review_id}",
    name="Deletar avaliação",
    description="Deleta uma avaliação existente",
    status_code=204,
)
async def delete_review(review_id: int):
    """
    Deleta uma avaliação existente

    :param review_id: ID da avaliação
    """
    review = Review.get_or_none(id=review_id)

    if not review:
        raise HTTPException(status_code=404, detail="Review not found")

    review.delete_instance()
