# Ex01. Crie um programa que recebe como entrada o comprimento, altura e a largura de um aquário e calcule as seguintes informações.

# O volume do aquário em litros;
# A potência do termostato necessária para manter a temperatura adequada dentro do aquário;
# A quantidade em litros de filtragem por hora necessária para manter a qualidade da água.

# Volume é dado por (comprimento * altura * largura) / 1000
# A potência do termostato depende do tamanho do aquário e da temperatura ambiente. Para o cálculo utilizar a fórmula: potencia = volume * 0,05 * (temperatura desejada - temperatura ambiente)
# A quantidade de filtragem por hora deve ser no mínimo 2 a 3 vezes o volume do aquário.

def calcular_volume(a: int | float, b: int | float, c: int | float) -> int | float:
    """Calcula o volume de um aquário em formato de paralelepípedo

    Args:
        a (int | float): O comprimento do aquário em metros
        b (int | float): A largura do aquário em metros
        c (int | float): A altura do aquário em metros

    Returns:
        float: O volume, em L
    """
    return (a * b * c) / 1000


def calcular_potencia_termostato(a: int | float, b: int | float, c: int | float, temperatura_desejada: float, temperatura_ambiente = 25) -> int | float:
    """Calcula a potencia do termostado de um aquário de medidas a, b e c

    Args:
        a (int | float): O comprimento do aquário em metros
        b (int | float): A largura do aquário em metros
        c (int | float): A altura do aquário em metros
        temperatura_desejada (float): A temperatura desejada do aquário
        temperatura_ambiente (int, optional): A temperatura do ambiente. Defaults to 25.

    Returns:
        int | float: A potencia necessária do termostato, em watt por hora
    """
    return calcular_volume(a, b, c) * 0.05 * (temperatura_desejada - temperatura_ambiente)


def calcular_quantidade_filtragem(a: int | float, b: int | float, c: int | float) -> int | float:
    """Calcula a quantidade de água filtrada por hora de um determinado aquário

    Args:
        a (int | float): O comprimento do aquário em metros
        b (int | float): A largura do aquário em metros
        c (int | float): A altura do aquário em metros

    Returns:
        int | float: A quantidade de água necessária para ser filtrada por hora
    """
    
    return calcular_volume(a, b, c) * 2.66