# Identificadores
# palavras reservadas (def, if, for, etc)
# caracteres, numeros e _

# Declaração de variáveis
# identificar = literal
# De forma dinânimica
nome = "Fernando"
Nome = "Outro nome"

nome = 123

# De forma estática
altura: float = 168

altura = "asdasd"

# Constantes não existem,
# porém há a convenção de definir constantes em maiúsculo
PI: float = 3.15159

def somar (a: float, b: float):
    """
    Retorna a soma de dois números
    
    :param a: número 1
    :param b: número 2
    :return: a soma de a e b
    """
    return a + b

def fibonnaci(n: int):
    """Retorna a lista de todos os números de fibonacci até n, exclusivo

    Args:
        n (int): O número até que deve retornar

    Returns:
        list[int]: A lista dos números de fibonnaci
    """

    if n <= 0:
        return [0]

    if n == 1:
        return [1]
    
    if n == 2:
        return [0, 1]

    sequence = fibonnaci(n - 1)
    next_number = sequence[-1] + sequence[-2]
    sequence.append(next_number)

    return sequence

numeros: list[int] = fibonnaci(100)


# Interpolação de strings
for indice, numero in enumerate(numeros):
    # f-string
    print(f'{indice}° {numero}')


habilidades = ['c', 'java', 'gdscript', 'python', 'javascript', 'c']

conjunto = set(habilidades)

print(habilidades)
print(conjunto)

