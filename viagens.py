viagens = {
    "Paris": {
        "preco": 5000,
        "vagas": 5
    },
    "Nova York": {
        "preco": 4000,
        "vagas": 3
    },
    "Tokyo": {
        "preco": 6000,
        "vagas": 2
    }
}


# Parte 1: Escolha do Destino
# Peça ao usuário:
# Nome do destino
destino = input("Digite seu destino:")

# Quantidade de pessoas
pessoas = int(input("Digite a quantidade de pessoas:"))

# Mostre o destino escolhido e a quantidade de pessoas
print("Destino:" , destino)
print('Quantidade de pessoas:', pessoas)

# Parte 2: Cálculo do Valor
# Calcule:
# Valor total da viagem (preço * pessoas)

preco = viagens[destino] ["preco"]
valor_total = (pessoas * preco)

print('Valor total integral:' , valor_total)

# Parte 3: Regras da Agência (SEM if, SEM loop)

# Aplique:
# Se pessoas > 3 → desconto de 10%
desconto1 = valor_total * 0.10 * (pessoas > 3)
print("Valor com desconto (3 pessoas):", valor_total - desconto1)

# Se valor total > 10000 → desconto extra de 5%
desconto2 = valor_total * 0.05 * (valor_total > 10000)
print("Valor com desconto (3 pessoas) + 5% extra (total a cima de 10000):", valor_total - desconto2)

# Se não houver vagas suficientes → taxa de 500 (overbooking)
vagas = viagens[destino] ["vagas"]
taxa = 500 * (pessoas > vagas)

print('Valor final:', valor_total - desconto1 - desconto2 + taxa )

# Se destino não existir → valor vira 0


