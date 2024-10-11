from .review_classifier import BertReviewClassifier


def test_bert_review_classifier():
    classifier = BertReviewClassifier()

    review = "Ótimo produto!"
    classification = classifier.classify(review)
    assert classification.value == "Positivo"

    review = "Produto péssimo!"
    classification = classifier.classify(review)
    assert classification.value == "Negativo"

    review = "Produto mediano"
    classification = classifier.classify(review)
    assert classification.value == "Neutro"
