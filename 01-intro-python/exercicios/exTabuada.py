def tabuada(n: int) -> list[int]:
    return list(map(lambda x: x * n, range(1, 11)))


def tabuada_prova(n: int) -> list[int]:
    l = []

    for numero in range(0,11):
        l.append(numero * n)

    return l


def main() -> None:
    print(tabuada(5))
    print(tabuada_prova(5))

if __name__ == "__main__":
    main()