# Utilizando as diretrizes de Índice de Massa Corporal (IMC) da Organização Mundial de Saúde (OMS), crie uma calculadora que solicita ao usuário seu peso (Kg) e sua altura (m) e 
# apresenta em qual classificação o indivíduo se encaixa.

from imc import calcular_imc, classificar_imc, obter_diferencia_peso_ate_imc_normal, IMC_IDEAL

def main() -> None:
    PESO = float(input("Informe seu peso em kg: "))
    ALTURA = float(input("Informe sua altura em metros: "))
    
    IMC = calcular_imc(PESO, ALTURA)
    
    print(f'O seu IMC é de {IMC:.2f}, com a classificação de \'{classificar_imc(IMC)}\'')
    
    diferenca_peso = obter_diferencia_peso_ate_imc_normal(PESO, ALTURA)
    
    condicao_imc = 'ganhar' if diferenca_peso > 0 else 'perder'
    
    print(f'Para obter o IMC ideal ({IMC_IDEAL}), é necessário {condicao_imc} {abs(diferenca_peso):.2f}')

if __name__ == "__main__":
    main()