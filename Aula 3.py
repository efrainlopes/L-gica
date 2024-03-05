# Tipos de dados
# 4 Tipos de dados:
# - Inteiros: Números Inteiros: (1, -1, 1000)
# - Virgula: numero com ponto flutuante: (2.4, 3.141516)
# - textuais: strings (a, aula, hoje é dia 3)
# - booleanos: Verdadeiro ou Falso
# Exemplos de números inteiros: "int" (interger): 1,2,-4,-5...
# Exemplos de numeros com vírgula: "float": 7.4, 3.2, -1.8
# Exemplos de dados textuais (entre aspas): "str":"a", "Escola", "Aprendendo Paython"
# Exemplos de dados booleanos: "bool": True, False

# VARIÁVEIS
# Colocar um nome que seja intuitivo. Que represente a realidade.
# Exemplos:
# numero1 = 5
# numero2 = 2
# soma = numero1 + numero2
# nome_completo = "Efrain Gonçalves Lopes"
# nome ="João"

# OPERAÇÕES MATEMÁTICAS
# Soma: +: 2+2
# Subtração: -: 6-4
# Multiplicação: *: 6*2
# Divisão: / : 7/4


numero1 = 58
# print(numero1)
numero2 = 87
soma = numero1 + numero2
# print(soma)
divisao = numero1/numero2
# print(divisao)
# multiplicaçao = numero1*numero2
# print(multiplicaçao)
# subtraçao = numero1-numero2
# print(subtraçao)

# ORDEM DE PRECEDÊNCIA NAS OPRAÇÕES MATEMATICAS
# 1)Potencição
# 2) multiplicação ou divisão: o que aparecer 1°
# 3) subtração (adição): o que vier aparecer 1°
# calculo = ((2+45)*23)/3-29
# print(calculo)
# numero1 = int(input("Digite um número: "))
# numero2 = int(input("Digite outro número: "))
# soma = numero1+numero2
# print("A soma é:", soma)
# subtraçao = numero1-numero2
# print("A subtração é:", subtraçao)
# divisao = numero1/numero2
# print("A divisão é:", divisao)
# multiplicação = numero1*numero2
# print("A multiplicação é:", multiplicação)


# Crie um programa  que solicite ao usuário o seu nome,
# dia de nascimento, mês de nascimento e ano de nascimento.
# Imprimam a resposta da seguinte forma:
# "Ola, fulano. Você nasceu no dia xx de xx de xxxx."

nome = int(input("Digite seu nome: "))
dia = int(input("Digite o dia de nascimento: "))
mes = int(input("Digite mes de nascimento: "))
ano = int(input("Digite ano de nascimento: "))
print("Olá, fulano:", nome)
print("Você nasceu no:", dia)
print("de:", mes)
print("de:", ano)



