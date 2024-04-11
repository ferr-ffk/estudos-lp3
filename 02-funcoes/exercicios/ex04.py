# Simulador de Eleições: Crie um programa que simule uma votação com três candidatos. O programa deve pedir ao usuário para votar várias vezes e, 
# no final, mostrar o número de votos de cada candidato e quem foi o vencedor. 


def exibir_candidatos(cs: list):
    for candidato in cs:
        nome = candidato["nome"]
        votos = candidato["votos"]

        print(f"Candidato '{nome}' possui {votos}")
        
        
def exibir_podio(cs: list):
    posicao = 1
    for candidato in cs:
        print(f"{posicao}° colocado(a): {candidato["nome"]}, com {candidato["votos"]} votos")
        
        posicao += 1
        
    vencedor = cs.pop(0)
        
    print(f"\nVencedor: {vencedor["nome"]}!!")


def votar(candidatos, n: str):
    for candidato in candidatos:
        for key in candidato.keys():
            if candidato[key] == n:
                candidato["votos"] += 1


def registrar_candidato(candidatos, nome: str):
    candidatos.append({"nome": nome, "votos": 0})
    

def ordenar_por_voto(candidato):
    return candidato["votos"]


def main():
    candidatos: list[dict] = []
    
    registrar_candidato(candidatos, "Joao Gomes")
    registrar_candidato(candidatos, "Davi Gomes")
    registrar_candidato(candidatos, "Rodrigo Gomes")

    n = int(input("Digite quantas vezes deseja votar:"))

    for _ in range(n):
        exibir_candidatos(candidatos)
        nome = input("Digite o nome do candidato que deseja votar:")

        votar(candidatos, nome)

    candidatos.sort(key=ordenar_por_voto, reverse=True)
    
    print("Resultados:")
    
    exibir_podio(candidatos)

main()
