def antecessor_sucessor(numero: int) -> tuple:
    antecessor = numero - 1
    sucessor = numero + 1

    return (antecessor, sucessor)

def main() -> None:
    numero = int(input())

    print(f'Antecessor, sucessor de {numero}: {antecessor_sucessor(numero)}')

if __name__ == "__main__":
    main()