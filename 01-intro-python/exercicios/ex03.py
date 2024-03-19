def valor_com_desconto_aplicado(valor: float) -> float:
    desconto: float = 0

    if valor in range(10, 100):
        desconto = 0.05
    elif valor in range(100, 500):
        desconto = 0.1
    else:
        desconto = 0.15

    tupla: tuple = (valor - (valor * desconto), desconto)

    return tupla

def main() -> None:
    valor = int(input())

    print(f'Valor após a compra e o desconto: {valor_com_desconto_aplicado(valor)}')

if __name__ == "__main__":
    main()