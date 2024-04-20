import random

def gera_resultados():
    pontosA = random.randint(75,130)
    pontosB = random.randint(75,130)
    while pontosA == pontosB:
        pontosB = random.randint(75,130)
    return [pontosA, pontosB]

def mata_mata(timeA, timeB, arquivo):
    vitA = 0
    vitB = 0
    while vitA < 4 and vitB < 4:
        placar = gera_resultados()
        arquivo.write(f"{timeA} {placar[0]} x {placar[1]} {timeB}\n")
        if placar[0] > placar[1]:
            vitA += 1
        else:
            vitB += 1
    
    if vitA == 4:
        return timeA
    else:
        return timeB

leste = ["knicks", "Nets", "Celtics", "76ixers", "Bucks", "Cavaliers", "Bulls", "Hornets"]

oeste = ["Lakers", "Warriors", "Nuggets", "Suns", "Grizzlers", "Heat", "Clippers", "Raptors"]


arq = open("resultado.txt", 'w')

# vencedor = mata_mata(leste[0], leste[7], arq)
# aux_leste.append(vencedor)

while len(leste) > 1:
        
    aux_oeste = []
    aux_leste = []

    i = 0
    j = len(leste) - 1 
    while i < j:
        vencedor = mata_mata(leste[i], leste[j], arq)
        aux_leste.append(vencedor)
        vencedor = mata_mata(oeste[i], oeste[j], arq)
        aux_oeste.append(vencedor)
        i = i + 1
        j = j - 1

    leste = aux_leste
    oeste = aux_oeste

vencedor = mata_mata(leste[0], oeste[0], arq)
print(f"Vencedor: {vencedor}")

arq.close()