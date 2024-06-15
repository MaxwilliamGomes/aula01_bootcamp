# Cálculo de Bônus com Entrada do Usuário

## Escreva um programa em Python que solicita ao usuário para digitar seu nome, o valor do seu salário mensal e o valor do bônus que recebeu.
## O programa deve, então, imprimir uma mensagem saudando o usuário pelo nome e informando o valor do salário em comparação com o bônus recebido.

## Instruções:


# 1) Solicita ao usuário que digite seu nome
nome = input("Digite seu nome : ")
# 2) Solicita ao usuário que digite o valor do seu salário
# Converte a entrada para um número de ponto flutuante
salario = float(input("Digite seu salário: "))
# 3) Solicita ao usuário que digite o valor do bônus recebido
# Converte a entrada para um número de ponto flutuante
bonus_recebido = float(input("Digite o bônus recebido: "))
# 4) Calcule o valor do bônus final
constante_bonus = 1000
Kpi = constante_bonus + salario * bonus_recebido
# 5) Imprime a mensagem personalizada incluindo o nome do usuário, salário e bônus
print(f'Olá {nome}, o seu bônus foi de {Kpi}')
# Bônus: Quantos bugs e riscos você consegue identificar nesse programa?

