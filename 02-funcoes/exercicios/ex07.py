# Jogo da Forca: Implemente uma versão simples do jogo da forca. O programa começa com uma palavra oculta (o usuário não vê) e o usuário tenta adivinhar a palavra, letra por letra.
# O usuário tem um número limitado de tentativas para adivinhar toda a palavra.

from random import randint

palavras_jogo = ["cachorro", "gato", "passarinho", "tartaruga", "camaleão"]

def escolher_palavra_aleatoria(palavras: list[str]):
    return palavras.pop(randint(0, len(palavras) - 1))

def jogar_rodada(palavra: str, letras_advinhadas: list[str], num_vidas: int) -> bool:
    # separa as letras em uma lista
    letras: list[str] = [char for char in palavra]

    # exibe a palavra e filtra com as letras ja advinhadas, exibindo um _ se a letra não advinhado    
    letras_palavra: list[str] = ["_" if char not in letras_advinhadas else char for char in letras]
    
    palavra_advinhada: bool = "".join(letras_palavra) == palavra
    
    if palavra_advinhada:
        return True
    
    palavra_escondida = " ".join(letras_palavra)
    
    possibilidades_bonequinho: dict[int, str] = {
        6: 
        """
        |
        |
        """,
        5: 
        """
        |   O
        |
        """,
        4: 
        """
        |   O
        |   |
        |
        """,
        3: 
        """
        |   O
        |   |-
        |
        """,
        2: 
        """
        |   O
        |  -|-
        |
        """,
        1: 
        """
        |   O
        |  -|-
        |  / 
        """,
        0: 
        """
        |   O
        |  -|-
        |  / \\
        """,
    }
    
    bonequinho: str = possibilidades_bonequinho[num_vidas]
    
    exibir_forca(palavra_escondida, bonequinho, letras_advinhadas)
    
    return False

def exibir_forca(palavra_escondida: str, bonequinho: str, letras_advinhadas: list[str]):
    print(
    f"""
    \t|---|
    \t|{bonequinho}|
    \t| {palavra_escondida}
    Letras advinhadas: ({letras_advinhadas})
    """
    )


def jogar() -> None:
    num_vidas: int = 6
    letras_advinhadas: list[str] = []
    palavra_escolhida: str = escolher_palavra_aleatoria(palavras_jogo)
    
    while num_vidas >= 0:
        ganhou = jogar_rodada(palavra_escolhida, letras_advinhadas, num_vidas)
        
        if ganhou:
            break
        
        letra = input("Digite uma letra... ").lower()
        
        if letra in letras_advinhadas:
            print("Você já advinhou essa letra! Escolha outra...")
            continue
        
        # advinhou uma letra que a palavra não tem, logo perde uma vida
        if letra not in palavra_escolhida:
            num_vidas -= 1
            
        letras_advinhadas.append(letra)
        
    
    if num_vidas >= 0:
        print(f"Parabéns! Você advinhou a palavra \"{palavra_escolhida}\"!")
    else:
        print(f"Você errou... a palavra escolhida era {palavra_escolhida}!")

        
def main() -> None:
    jogar()

if __name__ == "__main__":
    main()