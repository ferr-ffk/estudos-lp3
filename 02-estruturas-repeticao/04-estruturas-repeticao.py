# estruturas de repeticao

def print_palavra_vertical(palavra: str) -> None:
    for letra in palavra:
        print(letra)

    return None

print_palavra_vertical("DaviGomes")

# range
# range(inicio, termino, passo)
# ou
# range(inicio, termino)
# inclusivo, exclusivo
# ex:
# range(4, 10) 4, 5, 6, 7, 8, 9
# range(0, 20, 2) 0, 2, 4, 5, 6, 7, 8, 9, 10, 12, 14, 16, 18

print(range(0, 101, 2))

# for e while

for numero in range(0, 10):
    print(numero)

contador = 0

while contador < 40:
    print(contador)
    contador += 1

lista = list(range(-10, 10))

# tarefa: exibir os numeros positivos

for numero in lista:
    if 0 > numero:
        continue

    print(numero)

# ou de outra forma

print("\n")

for numero in lista:
    if 0 < numero:
        print(numero)

# COMPREENSAO DE LISTAS...

numeros = [1, 2, 3, 4, 5, 6, 7, 9, 10]

# nova_lista = [operacao de mapeamento for operando in lista_a_mapear]
numerosAoQuadrado = [numero ** 2 for numero in numeros]

numerosPares = [numero for numero in numeros if numero % 2 == 0]

print(f'Numeros originais: \t{numeros}')
print(f'Numeros ao quadrado: \t{numerosAoQuadrado}')
print(f'Numeros pares: \t\t{numerosPares}')

