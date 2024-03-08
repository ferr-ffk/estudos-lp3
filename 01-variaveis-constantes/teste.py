def tudo_maiusculo(elementos: list[str]) -> list[str]:
    return [elemento.upper() for elemento in elementos]

def main():
    lista = ["abc", "def", "ghi", "jlkmn", "op", "qr", "stuv"]

    print(tudo_maiusculo(lista))

    print([1, 2, 3, 4, 5, 6, 7, 8, 9, 10][0:5:2])

    lista_longa: list[str] = [p for p in lista if len(p) > 2]

    print(lista_longa)

if __name__ == "__main__":
    main()