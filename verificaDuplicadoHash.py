"""
Algoritmo que verifica se alguém já está no sistema
Caso seja a primeira vez vai ser liberado entrar
Caso contrário vai ser barrado

O algoritmo usa um dicionário para armazenar os nomes
Em seguida a função verifica se o nome já está no dicionário
Se estiver, a pessoa não pode entrar
"""

votaram = {} # lista de eleitores que já votaram

def verifica_eleitor(nome):
    if votaram.get(nome): # Verifica se o nome já está no dicionário
        # votaram.get retorna True se estiver no dicionário e None se não houver registro
        print("Saia daqui")
    else:
        votaram[nome] = True # Se não estiver no dicionário vai ser adicionado
        print("Pode entrar")

verifica_eleitor("Lucas") # Primeira vez então vai entrar
verifica_eleitor("Maria") # Primeira vez então vai entrar
verifica_eleitor("Lucas") # Já está no dicionário então vai ser barrado

print(votaram)