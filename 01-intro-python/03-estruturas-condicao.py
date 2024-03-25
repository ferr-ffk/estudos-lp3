# Estruturas de condicao

idade = 17

# if

if idade >= 18:
    print("É um adulto jaa ownt")

# if/else

if idade >= 18 <= 60:
    print("já pode ser preso")
else:
    print("não pode ser preso")

# if/elif/else

if idade <= 12:
    print("crianca")
elif idade <= 17:
    print("adolescente")
else:
    print("adulto ou idoso")


if idade >= 18:
    print("O usuário é maior de idade")

for _ in range(0, 100):
    print(f'{_}°')

# Ternario

email = "usuario@gmail.com"
senha = "123456"

def autenticarUsuario(email: str, senha: str) -> bool:
    return email == "usuario@gmail.com" and senha == "123456"

# match case (switch case)

def numero_correspondente_dia(dia: int) -> str:
    dias: dict[int, str] = {1: "domingo", 2: "segunda", 3: "terça", 4: "quarta", 5: "quinta", 6: "sexta", 7: "sabado"}

    return dias[dia] if dia in dias else '0'

print(numero_correspondente_dia(3))

# Operador ternário

idade = 20
status = ''

status = 'Maior' if idade >= 18 else 'Menor'

# equivalente de

if idade >= 18:
    status = 'Maior'
else:
    status = 'Menor'

# match (switch) case

periodo = "dia"
dia = 12

match periodo:
    case "dia":
        print("Sim")
    case "noite":
        print("Nao")
    case _:
        print("invalidooo")

match dia:
    case 1 | 7:
        print("fim de semana")
    case 2 | 3 | 4 | 5 | 6:
        print("semana")
    case _:
        print("boco")
