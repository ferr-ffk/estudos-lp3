# Função de Contagem de Palavras: Escreva uma função que receba uma string (frase) como argumento e retorne um dicionário onde as chaves são as palavras únicas no texto e os
# valores são o número de vezes que cada palavra aparece no texto. Depois, teste a função com diferentes textos fornecidos pelo usuário.

def registrar_palavras(frase: str) -> dict[str, int]:
    palavras = frase.split()
    
    r: dict[str, int] = {}
    
    for palavra in palavras:
        r.update({palavra: palavras.count(palavra)})
        
    return r
    
    
frase = input("Digite uma frase para contar quantas vezes cada palavra foi utilidada: ")

contagem = registrar_palavras(frase)

for palavra, contagem in contagem.items():
    print(f"A palavra {palavra} foi utilizada {contagem} vez(es)")