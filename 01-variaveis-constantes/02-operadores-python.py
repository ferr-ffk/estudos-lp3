# Operadores aritméticos

nota1 = 7.8
nota2 = 3.5
nota3 = 9.6

media = (nota1 + nota2 + nota3) / 3

print(media)

numero_elevado_5 = nota1 ** 5

print(numero_elevado_5)

# Operadores lógicos
# and, not, or

autenticado = True
senhaConfirmada = True
admin = False

usuarioLogado = autenticado and senhaConfirmada

if usuarioLogado:
    print("O usuário está logado")

usuarioAdmin = usuarioLogado and admin

if usuarioAdmin:
    print("O usuário é o admin")

lista = [1, 2, 3, 4, 5]

listaVazia = []

print(bool(lista))      # True
print(bool(listaVazia)) # False

print(bool(""))    # False
print(bool("oie")) # True

print('\x1b[2J')

print("oier")

# Operadores de identitade
# == compara os valores da variavel ou identidade
# is compara se ambos apontam para a mesma referência

a = [1, 2, 3]
b = [1, 2, 3]

print(a == b)
print(a is b)

# operador de lista
# apenas em sequências como str, list, dict, tuple

opcoes = ("sim", "nao", "talvez")

while True:

    opcao = input("Digite Sim, Nao ou Talvez").lower().strip()

    if opcao not in opcoes:
        print("Digite uma opção válida!")
        continue

    break
    
print("Continuouu")




