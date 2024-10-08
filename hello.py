from transformers import pipeline

sentiment_analyzer = pipeline("sentiment-analysis", model="nlptown/bert-base-multilingual-uncased-sentiment", device=0)
review = """
O serviço foi muito demorado e o atendente
parecia completamente despreparado. Precisei
repetir meu problema várias vezes, e mesmo
assim senti que ele não estava entendendo o
que eu estava dizendo. Perdi muito tempo, e o
pior de tudo é que o problema não foi resolvido
ao final. Vou reconsiderar continuar usando esse
serviço.
"""
result = sentiment_analyzer(review)

print(result)
