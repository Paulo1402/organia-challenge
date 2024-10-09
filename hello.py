from transformers import pipeline

sentiment_analyzer = pipeline(
    "sentiment-analysis",
    model="nlptown/bert-base-multilingual-uncased-sentiment",
    device=0,
)
# review = """
# O serviço foi muito demorado e o atendente
# parecia completamente despreparado. Precisei
# repetir meu problema várias vezes, e mesmo
# assim senti que ele não estava entendendo o
# que eu estava dizendo. Perdi muito tempo, e o
# pior de tudo é que o problema não foi resolvido
# ao final. Vou reconsiderar continuar usando esse
# serviço.
# """

review = """
Estou extremamente satisfeito com o suporte!
Resolveram meu problema de forma ágil e com
clareza nas explicações. Além de resolverem o
erro no sistema que estava impedindo a
execução de uma função crítica para o meu
negócio, eles ainda sugeriram melhorias para
evitar que o problema ocorresse novamente. O
atendimento foi muito acima do esperado!
"""
result = sentiment_analyzer(review)

print(result)
