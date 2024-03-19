def media(notas: list[int | float]) -> float:
    soma = 0

    for nota in notas:
        soma += nota

    return soma / len(notas)

def main() -> None:
    _numeroNotas = 3

    notas: list = []

    print("Digite as três notas, uma por vez")

    for _ in range(_numeroNotas):
        notas.append(float(input()))

    print(media(notas))

if __name__ == "__main__":
    main()