from random import choice

class Util:
    letras = "abcdefghijklmnopqrstuvxwyz"
    tamanho = len(letras)

    @staticmethod
    def gerar_palavra(n):
        palavra = "".join(choice(Util.letras) for _ in range(n))
        return palavra
