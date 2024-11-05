from abc import ABC, abstractmethod
from enum import Enum

from transformers import pipeline


class InvalidClassifierError(Exception):
    """
    Exceção para classificador inválido
    """

    pass


class ClassifierError(Exception):
    """
    Exceção para erro no classificador
    """

    pass


class SentimentClassification(Enum):
    """
    Enum para classificação de sentimentos
    """

    POSITIVE = "Positivo"
    NEUTRAL = "Neutro"
    NEGATIVE = "Negativo"


class ReviewClassifier(ABC):
    """
    Classe abstrata para classificação de avaliações
    """

    @abstractmethod
    def _classify(self, review: str) -> SentimentClassification:
        """
        Classifica uma avaliação
        :param review: Avaliação
        :return: Classificação
        """
        pass

    def classify(self, review: str) -> SentimentClassification:
        """
        Classifica uma avaliação
        :param review: Avaliação
        :return: Classificação
        """
        try:
            return self._classify(review)
        except Exception as e:
            raise ClassifierError(f"Error classifying review: {e}")


class BertReviewClassifier(ReviewClassifier):
    """
    Classificador de avaliações usando BERT
    """

    def __init__(self):
        self.sentiment_analyzer = pipeline(
            "sentiment-analysis",
            model="nlptown/bert-base-multilingual-uncased-sentiment",
            device=0,
        )

    def _classify(self, review: str) -> SentimentClassification:
        """
        Classifica uma avaliação
        :param review: Avaliação
        :return: Classificação
        """
        result = self.sentiment_analyzer(review)
        label = result[0]["label"]

        if label == "1 star":
            return SentimentClassification.NEGATIVE

        if label == "2 stars":
            return SentimentClassification.NEGATIVE

        if label == "3 stars":
            return SentimentClassification.NEUTRAL

        if label == "4 stars":
            return SentimentClassification.POSITIVE

        if label == "5 stars":
            return SentimentClassification.POSITIVE


class ReviewClassifierFactory:
    """
    Fábrica de classificadores de avaliações
    """

    _CLASSIFIERS = {
        "bert": BertReviewClassifier,
    }

    @property
    def classifiers(self) -> list[str]:
        """
        Retorna os classificadores disponíveis
        :return: Classificadores disponíveis
        """
        return list(ReviewClassifierFactory._CLASSIFIERS.keys())

    @staticmethod
    def create_review_classifier(classifier: str) -> ReviewClassifier:
        """
        Cria um classificador de avaliações

        :param classifier: Nome do classificador
        :return: Classificador de avaliações
        """
        classifier_class = ReviewClassifierFactory._CLASSIFIERS.get(classifier)

        if not classifier_class:
            raise InvalidClassifierError(f"{classifier} is not a valid classifier")

        return classifier_class()
