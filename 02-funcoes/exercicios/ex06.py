# Conversor de Notas Escolares: Baseado em uma pontuação fornecida pelo usuário (0 a 100), converta para o sistema de notas A, B, C, D, ou F, seguindo os padrões de conversão comuns.

def converter_nota(n: int) -> str:
    t = {
        range(0,60): "F",
        range(0,70): "D",
        range(0,80): "C",
        range(0,90): "B",
        range(0,101): "A"
    }
    
    for key in t.keys():
        if n in key:
            return t[key]
        
    return "N/A"
        
nota = int(input("Digite a nota para ser convertida: "))

print(f"A nota {nota} equivale a {converter_nota(nota)}")