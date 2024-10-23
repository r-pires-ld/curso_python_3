#input sempre retorna uma string
#nome = input("Qual seu nome?")
#print(f"seu nome é {nome}")

#sempre fazer a conversão da variavel para receber o valor

''''
modo errado de se fazer
numero_1 = int(input("Digite um numero qualquer: "))
numero_2 = int(input("Digite outro numero qualquer: "))
'''

numero_1 = input('Digite um numero: ')
conv_numero_1 = int(numero_1)
numero_2=input('Digite outro numero')
conv_numero_2 = int(numero_2)
print(f'A soma dos numeros é: {conv_numero_1+conv_numero_2}')