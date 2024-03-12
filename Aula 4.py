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
1) Igual: =
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

#Diferente
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



# Calculo de Celsius para Fahrenheit:
# temp_celsius = 0
# temp_fahrenheit = 32
# celsius = int (input("Digite uma temperatura em Celsius"))
# tranformacao = (temp_celsius * 1.8 + 32)
# print(tranformacao)

# Notas Bimestrtias
nota1 = float(input(" Digite a nota1"))
nota2 = float(input("Digite a nota2"))
nota3 = float(input("Digite a nota3"))
nota4 = float(input("Digite a nota4"))
media = (nota1+nota2+nota3+nota4)/4
print(media)

# Calculo de IMC
massa = float (input("Digite sua massa"))
altura = float(input("Digite sua altura"))
imc = (massa/altura^2)
print()


