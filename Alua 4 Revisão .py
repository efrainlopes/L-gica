#print (12)
#print (12, 45)
#print(12, 45, sep="", end="")
"""
print(12, 45, sep="-", end="")
print (1, 2)
print (3, 4)
print (5, 6)
print ("CALCULADORA")
print ("*" * 30)
print ('Olá, Mundo')
print('Paython, é uma "linguagem" de programação')
print("Paython, é uma 'linguagem' de programação")
"""
"""
Posso fazer qualquer comentário 
"""
"""
CONDICIONAIS 
1) if (se)
2) else (então
3) elif (else + if) (senão)
"""
#  Exemplo
# Informacao_usuario = str (input('voce deseja "entrar" ou "Sair" do programa?' ))
# if Informacao_usuario == "Entrar":
#     print ("Sistema acessado com com sucesso!")
# else:
#     print("Voce não acesssou a sistema")
"""
entrada_usuario = str(input('Digite "E" para entar' 'ou "S" para sair:'))
if entrada_usuario == "E":
    print("Bem vindo ao sistema")
elif entrada_usuario == "S":
    print("Você saiu do sistema")
else:
    print('Você não digitou nem "E" e nem "S" .' )
"""

"""
Operadores relacionais (de comparação)
1) Igual: ==
2) Maior: >
3) Menor: <
4) Maior ou igual: >=
5) Menor ou igual: <=
6) Diferente: != 
"""
# Igual
# igual = "1" == "1"
# print(igual)

# maior = 2 > 1
# maior = 1 > 2
# print(maior)

# Menor
# menor = 4 < 8
# print(menor)

# Maior ou igual
# maior_ou_igual = 6 >=6
# print(maior_ou_igual)

# Diferente
# diferente = 1!= "1"
# print(diferente)

"""
Operadores lógicos
e (and)
X (True) and Y (False) = False
X (False) and Y (True) = False
X (False) and Y (False) = False
X (True) and Y (True) = True

ou (or)
X (True) or Y (False) = True
X (False) or Y (True) = True
X (True) or Y (True) = True
X (False) or Y (False) = False

Negação (not)
X (True) not X  = False
X (False) not X = True 
"""

# and
# x = True
# Y = True
# resultado = x and y
# print(resultado)


# or
# x = False
# Y = False
# resultado = x and y
# print(resultado)



# Tranformação de Celsius para Fahrenheit:
# temp_celsius = 0
# temp_fahrenheit = 32
# celsius = int (input("Digite uma temperatura em °C"))
# tranformacao = (temp_celsius * 1.8 + 32)
# print(tranformacao)
"""
# Notas Bimestrtias
nota1 = float(input(" Digite a nota1:"))
nota2 = float(input("Digite a nota2:"))
nota3 = float(input("Digite a nota3:"))
nota4 = float(input("Digite a nota4:"))
media = (nota1+nota2+nota3+nota4)/4
print("A sua média final é:")
if media >= 6:
    print("Parabens, você foi aprovado")
else:
    print("Não foi dessa vez, você foi reprovado")
print(media)
"""
"""
# Programa de Calculo de IMC
# Potenciação: **
peso = float (input("Digite seu peso:"))
altura = float(input("Digite sua altura:"))
imc = (peso/(altura**2))
print(imc)
if (imc < 18.5):
    print("Baixo peso")
elif (18.5 <= imc < 25):
     print("Peso nornal")
elif 25 <= imc < 30:
    print("Sobrepeso")
elif 30 <= imc < 35:
    print("Você está com obesidade grau I")
elif 35 <= imc < 40:
    print("Você está com obesidade grau II")
else:
    print("Você esta com obesidade mórbida")
"""
"""
# Faça um programa que peça 2 numeros e diga qual é maior.
numero1 = float(input("Digite um número qualquer:"))
numero2 = float(input("Digite um número qualquer, pode ser o mesmo:"))
if numero1 > numero2:
    print("O numero", numero1, "É maior que o numero", numero2)
elif numero1 < numero2:
    print("O numero", numero1, "É menor que o numero", numero2)
else:
    print("Os números são iguais")
"""
"""
# Peça para o usuário um número e informe se le é positivo ou negativo

numero = float(input("Digite um número:"))
if numero > 0:
    print(("O número é positivo"))
elif numero == 0:
    print("O número é nulo")
else: 
    print("O número é negativo")
"""
"""
Desenvolva um programa que calcule o reajuste salarial, conforme o salário do funcionarário
1) Salário de até R$2000: aumento de 20%
2) Salário entre R$ 2000 e R$3500: aumento de 10%
3) Salário entre R$ 3500 e R$5000: aumento de 10%
4) Salário maior R$ 5000 : aumento de 5%
O resultado precisa aparecer como resultado:
- Salário atual
- Percentual de aumento
- Valor em R$ do aumento
- Novo salário (incluindo o aumento)
"""