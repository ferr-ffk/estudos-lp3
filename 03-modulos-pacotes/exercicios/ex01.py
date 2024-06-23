from aquario import *

# Ex01. Crie um programa que recebe como entrada o comprimento, altura e a largura de um aquário e calcule as seguintes informações.

def main() -> None:
    A = int(input("Digite o comprimento do aquário: "))
    B = int(input("Digite a altura do aquário: "))
    C = int(input("Digite a largura do aquário: "))
    
    temperatura_desejada = int(input("Digite a temperatura desejada para um aquário: "))
    
    print(f'Volume do aquário: {calcular_volume(A, B, C)} L')
    print(f'Potência necessária do termostato: {calcular_potencia_termostato(A, B, C, temperatura_desejada)} W/h')
    print(f'Quantidade de água necessária para filtrar: {calcular_quantidade_filtragem(A, B, C)} L/h')

if __name__ == "__main__":
    main()