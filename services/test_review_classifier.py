from .review_classifier import BertReviewClassifier


def test_bert_review_classifier():
    classifier = BertReviewClassifier()

    review = "This is a great product!"
    classification = classifier.classify(review)
    assert classification == "positive"

    review = "This is a terrible product!"
    classification = classifier.classify(review)
    assert classification == "negative"

    review = "This is a normal product."
    classification = classifier.classify(review)
    assert classification == "neutral"