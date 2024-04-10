#  Jogo de Adivinhação: Peça ao usuário para adivinhar um número entre 1 e 100 que o programa escolheu aleatoriamente. 
# Informe ao usuário se o palpite está alto ou baixo, até que ele acerte o número.

from random import randrange

def jogar():
    numero_aleatorio = randrange(1, 100)

    errando = True

    while errando:
        aposta = int(input("Digite um número de 1 a 100..."))

        errando = numero_aleatorio != aposta

        print("Aposta errada!")

        proximidade = "maior" if aposta > numero_aleatorio else "menor"

        print(f"O número advinhado é {proximidade}...")

    print(f"Parabéns!! Você acertou o número {numero_aleatorio}!!")


jogar()
