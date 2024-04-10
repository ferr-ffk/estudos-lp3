# Tabuada de Um Número: Solicite ao usuário um número e exiba a tabuada desse número de 1 a 10.

def tabuada(x: int) -> list[int]:
    l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    return [num * x for num in l]

n = int(input("Digite um número: "))

print(f"{tabuada(n) = }")
