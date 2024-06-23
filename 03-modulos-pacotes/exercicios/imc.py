# Utilizando as diretrizes de Índice de Massa Corporal (IMC) da Organização Mundial de Saúde (OMS), crie uma calculadora que solicita ao usuário seu peso (Kg) e sua altura (m) e 
# apresenta em qual classificação o indivíduo se encaixa.

# IMC = peso / altura * altura

# Classificação
# ----------------------------------
# IMC           Classificação
# -----------------------------------
# < 18,5             Baixo peso
# 18,5 a 24,9     Peso normal
# 25,0 a 29,9     Excesso de peso
# 30,0 a 34,9     Obesidade de Classe 1
# 35,0 a 39,9     Obesidade de Classe 2
# >= 40,00         Obesidade de Classe 3

# Além disso, o programa deve apresentar quanto o indivíduo precisa perder ou ganhar de peso para chegar no peso normal (imc = 24,9).

_TABELA_IMC: dict[float, str] = {
    18.5: 'Baixo peso',
    25.0: 'Excesso de peso',
    30.0: 'Obesidade de Classe 1',
    35.0: 'Obesidade de Classe 2',
    40.0: 'Obesidade de Classe 3',
}

IMC_IDEAL: float = 24.9


def calcular_imc(peso: int | float, altura: int | float) -> float:
    """Calcula o IMC com base no peso e na altura

    Args:
        peso (int | float): O peso em kg
        altura (int | float): A altura em metros

    Returns:
        float: O IMC
    """
    return peso / (altura ** 2)


def classificar_imc(imc: float) -> str:
    for valor in _TABELA_IMC:
        if imc < valor:
            return _TABELA_IMC[valor]
        
    # Referencia a ultima chave na lista e sempre retorna a maior opção
    return _TABELA_IMC[list(_TABELA_IMC)[-1]]


def obter_diferencia_peso_ate_imc_normal(peso: float, altura: float) -> float:
    """Calcula o peso necessário para obter o IMC ideal

    Args:
        peso (float): O peso em kg
        altura (float): A altura em metros

    Returns:
        float: O ganho ou a perda de peso necessário, valores positivos indicam a necessidade de ganho e valores negativos significam a necessidade de perda de peso
    """
    
    # Para ter um IMC normal, é necessário calcular o IMC com a altura do usuário
    peso_necessario: float = IMC_IDEAL * (altura ** 2)
    
    # Retorna então a diferença do peso ideal com o peso atual
    return peso_necessario - peso


def main() -> None:
    print(f'IMC: {calcular_imc(50, 1.70) = }')
    print(f'Diferença de peso até imc ideal{obter_diferencia_peso_ate_imc_normal(90, 1.60) = }')


if __name__ == "__main__":
    main()