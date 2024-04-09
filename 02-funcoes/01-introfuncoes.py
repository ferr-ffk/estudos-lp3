# Funções em python

"""
def [nome] ([...parametros]):
    ...
"""

def exemplo(parametro):
    print("função de exemplo")

# chamada

exemplo(8)


# Função sem parâmetros e sem retorno

def funcao1():
    print("ebaa")

funcao1()

# Função sem parâmetros e com retorno

def funcao2():
    return range(0,10)

valor = funcao2()

print(f"{valor = } \tda funcao {funcao2}")

# Função com parâmetros e com retorno

def funcao3(a, b):
    return a + b

valor = funcao3(8, 9)

print(f"{valor = } \t\tda funcao {funcao3}")

# Função com parâmetros e sem retorno

def obter_mensagem():
    return 'Socorro!!'

print(obter_mensagem)

notas_alunos: list[list[float]] = [
    [1.5, 2.5, 3.5], 
    [3.4, 7.8, 2.3],
    [5.6, 10.0, 3.4],
    [5.6, 3.4, 2.4],
    [8.7, 4.6, 6.4],
]

def calcular_media(valores: list[int | float]):
    return sum(valores) / len(valores)

def media_lista_alunos(lista_alunos: list[list[float]]) -> list[float]:
    lista_medias: list[float] = []

    for lista in lista_alunos:
        lista_medias.append(calcular_media(lista))

    return lista_medias

# é equivalente de:
def media_lista_alunos(lista_alunos: list[list[float]]) -> list[float]:
    return [(sum(notas) / len(notas)) for notas in lista_alunos]

print("\n")

print(f"{media_lista_alunos(notas_alunos) = }")

# Argumentos nomeados

def saudacao(nome, frase):
    return f"{frase}, {nome}"

#       vvvvvvv     vvvvv       argumentos posicionais
saudacao("Joao", "FAAALAAAA ")

saudacao(frase="tudo bem", nome="Davi")

# Valores padrão

def set_visivel(visivel=True):
    if visivel:
        print("Tudo está visivel agora")
    else:
        print("Tudo escuro...")


# Sobrecarga e sobrescrita
# Sobrecarga: não existe em python </3
# Sobrescrita: reescrita da função