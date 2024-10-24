entrada= input('voce quer entrar ou sair?')
if entrada == 'entrar':
    print('voce entrou no sistema')
elif entrada == 'sair':
    print('voce saiu no sistema')
elif entrada =='admin':
    senha = input('Digite a senha: ')
    if senha =='senha':
        print('Voce entrou no modo administrador')
    else:
        print('senha incorreta')
else:
    print('voce não digitou entrar ou sair')

print('sistema logout')