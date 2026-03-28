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
destino = input("Digite seu destino: ")

preco = viagens["preco"]
vagas = viagens["vagas"]

# Quantidade de pessoas
pessoas = int(input("Digite o número de pessoas: "))

# Parte 2: Cálculo do Valor
valor_total = preco * pessoas

# Parte 3: Regras da Agência (SEM if, SEM loop)

# desconto de 10% se pessoas > 3
desconto1 = valor_total * 0.10 * (pessoas > 3)

# desconto extra de 5% se valor_total > 10000
desconto2 = valor_total * 0.05 * (valor_total > 10000)

# taxa de 500 se não houver vagas suficientes
taxa = 500 * (pessoas > vagas)

# Se o destino não existir, já define tudo como 0
dados = viagens.get(destino, {"preco": 0, "vagas": 0})

# valor final
valor_final = valor_total - desconto1 - desconto2 + taxa

print("Valor final da viagem:", valor_final)
