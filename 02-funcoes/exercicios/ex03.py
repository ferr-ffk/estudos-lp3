# Contador de Vogais e Consoantes: Peça ao usuário para digitar uma frase e retorne o número de vogais e consoantes na frase.

alfabeto = "a b c d e f g h i j k l m n o p q r s t u v w x y z".split()

vogais = "a e i o u".split()

consoantes = [n for n in alfabeto if n not in vogais]

def contar_vogais(s: str) -> int:
    cont: int = 0

    for char in s:
        if char in vogais:
            cont += 1

    return cont


def contar_consoantes(s: str) -> int:
    cont: int = 0

    for char in s:
        if char in consoantes:
            cont += 1

    return cont

str = input("Escreva uma frase:")

print(f"A frase possui {contar_vogais(str)} vogais e {contar_consoantes(str)} consoantes")
