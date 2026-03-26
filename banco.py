cdg prof
# 4  tipos
# str      int             float    bool
# textos numeros inteiros reais lógicos
# 'texto',  10 ,  5.2 ,  True , False
# 'Bom dia', 2026,1.80, 1 , 0
# 'Seu nome:',1, 60.200,
# 'R$'
# ESTRUTURAS DE DADOS ****
# espaços na memória ram da maquina
# variar
# variaveis são dados únicos
# interpertador
# meio termo linguagem
# força indentação = organização
# OUTPUT - SAIDA - print()
# nomear de forma semantica  -  boa pratica
# regras para criar variáveis:
# _ ou letra
# não pode começar por números
# não pode carcateres especiais
# pode utilizar números(só não pode começar)
# palavra composta snake_case
# linguagem alto nivel
# interpretada
# dinamica - variáveis
print('CADASTRO DE USUÁRIOS:')
nome = 'Lucas Lima'
idade  =  25
email_usuario = 'lucas@gmail.com'
peso = 80.50
altura =  1.90
endereco = 'Rua 10, Jd X'
graduacao = 'ADS'
casado = False
# SAÍDA
print(nome)
print(idade)
print(email_usuario)
print(endereco)
print(graduacao)
print(peso)
print(altura)
print(casado)
# ENTRADA
nome_2 = input('digite seu nome: ')
print(nome_2)





print('IMC')
peso =  float(input('Digite seu peso: '))
altura  =  float(input('Digite sua altura: '))
imc  =  peso/altura**2
print('IMC', imc)


print('SINAIS DE CALCULO ARITMÉTICO')



print(10+200) # soma
print(10-200) # subtração
print(10*200) # multiplicalçi
print(10/200) # divisão
print('modulo', 10%200) #módulo
print(10**2) # potencia
print(10//200.0) # divisão c/ 2 barras
# variáveis -  estruturas de dados
# funções  - print() input() float() int()
# sinais aritmétivos



# sinais lógicos
print(10 == 200) # comparar
print(10 > 200) # verifa se 1º numero é maior
print(10<200) # verifa se 1º numero é menor
print(10>=200) # maior ou iguael
print(10<=200) # menor ou igual
print(10 != 2) # diferente





# linguagem de alto nivel
# interpretada
# dinamica - variáveis


# OUTPUT = SAIDA - print ()
# nomear as estrututras de dados de forma semantica - boa pratica
# str = texto
# int =
# float =


# regras para criar variáveis :
# _ ou Letra
# pode utilizar, mas, não pode começar por números
# não pode caracteres especiais
# palavra composta = snake_case


# SAIDA DE DADOS


# print('CADASTRO DE USUÁRIOS:')
# nome = 'Lucas Lima'
# idade = 25
# email_usuario = 'lucas@gmail.com'
# peso = 80.50
# altura = 1.90
# endereco = 'Rua 10, Jd Paraíso'
# graduacao = 'Gestão TI'
# casado = False


# print( type (nome))
# print(type (idade))
# print(email_usuario)
# print(peso)
# print(altura)
# print(endereco)
# print(graduacao)
# print(casado)


# ENTRADA DE DADOS


# nome2 = input('digite seu nome:')
# print(nome2)


# numero1 = float(input('digite um número:'))
# numero2 = float(input('digite um número:'))


# soma = numero1 + numero2
# print = (soma)


# print('IMC')


# peso = float(input('digite seu peso:'))
# altura = float(input('digite sua altura:'))
# imc = peso/altura**2
# print ('IMC', imc)


# sinais de calculos aritiméticos


# print('calculos aritimeticos')


# print(10+200) # soma
# print(10-200) # subtração
# print(10*200) # multiplicação
# print(10/200) # divisão
# print('modulo', 10%200) # modulo
# print(10**200) # potencia
# print(10//200) # divisão com duas barras


# funções = print; input; float; int;


# sinais lógicos


# print(10 == 200) # comparar
# print(10 > 200) # verificar se é maior ou menor
# print(10 < 200) # verificar se é maior ou menor
# print(10 >= 200) # maior ou igual
# print(10 <= 200) # menor ou igual
# print(10 != 200) # diferente






	






# Peça so usuário dois números:


n1 = int(input('Digite um número:'))
n2 = int(input('Digite um número:'))


#  Mostre a soma, subtração, multiplicação e divisão :


print(n1 + n2)
print(n1 - n2)
print(n1 * n2)
print(n1 / n2)


# Verifique se os números são iguais:


print(n1 == n2)


# Se o primeiro número é maior que o segundo


print(n1 > n2)


# Se pelo menos um dos números é maior que 10


print(n1 > 10)
print(n2 > 10)






atividade  2 ( desconto ) 


# Peça o valor de um produto e:


valor_produto = float(input('Digite um número:'))


# Calcule um desconto de 10%.


desconto = valor_produto * 0.10
valor_final = valor_produto - desconto


# Mostre o valor final.


print ( valor_final )


# Verifique se o valor final é maior que 100.


print ( valor_final > 100  )


# Verifique se o produto ficou barato (menor que 50).


print ( valor_final < 50  )



concatenado 


# Peça o valor de um produto e:


valor_produto = float(input('Digite um número:'))


# Calcule um desconto de 10%.


desconto = valor_produto * 0.10
valor_final = valor_produto - desconto


# Mostre o valor final.


print ( 'Valor do produto: R$', valor_final )


# Verifique se o valor final é maior que 100.


print ('Verifique se o valor final é maior que 100:', valor_final > 100  )


# Verifique se o produto ficou barato (menor que 50).


print ( 'Verifique se o produto ficou barato:', valor_final < 50  )

#lista 


# adicionar ou remover um dado a lista


lista_vazia.append(100)
lista_vazia.remove(100)

# estrutura composta




listas = [10,20,30,40]
lista_texto = ['a', 'b', 'c']
listas_mista = [True, False, True]
lista_vazia = []



TRANSAÇÃO BANCO (EXEMPLO) 

saldo = [1500.0]
extrato = []
extrato.append(sum(saldo))
saque =  float(input('Digite o saque: '))
transacao =  sum(saldo) - saque
extrato.append(saque)
saldo = [transacao]
print('Saldo R$', saldo)
deposito =  float(input('Digite o Deposito R$: '))
extrato.append(deposito)
transacao =  sum(saldo) + deposito
saldo = [transacao]
print('Saldo R$', saldo)
print(extrato)
