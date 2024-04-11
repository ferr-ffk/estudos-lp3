# Verificador de Palíndromos: Solicite ao usuário que digite uma palavra ou frase e verifique se é um palíndromo (ou seja, pode ser lida de frente para trás e de trás para 
# frente da mesma forma).


def verificar_palindromo(palavra: str) -> bool:
    return palavra[::-1] == palavra


palavra = input("Digite uma palavra para se verificar se é um palíndromo: ").strip()

resultado = "É um palíndromo" if verificar_palindromo(palavra) else "Não é um palíndromo"

print(resultado)