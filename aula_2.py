#formatação de strings
#o f serve para formatar uma string podendo colocar variaveis e formatalas dentro dessa string
#:.2f é usado para formatar a quantidade de casas decimais que o float irá ter
nome ="roney pires"
altura=1.8
peso=93
imc=peso/altura**2
linha_1=f'{nome} tem {altura:.2f} de altura '
linha_2=f'pesa {peso} quilos e seu imc é'
linha_3=f'{imc:.2f}'
print(linha_1)
print(linha_2)
print(linha_3)