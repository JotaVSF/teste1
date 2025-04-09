email = 'J04o'
senha = 12345
for tentativas in range(3):
    digitar_email = input('Email: ')
    digitar_senha = int(input('Senha: '))
    if digitar_email == email and digitar_senha == senha:
        print('''
                    Acesso liberado!😅
              
              ''')
        break
    elif digitar_email == email and digitar_senha != senha:
        print('''
                    Senha incorreta!😥
                    
                    ''')
        tentativas-=1
    else:
        print('''
                Credenciais invalidas.😥
                    
                    ''')
    if tentativas == 2:
        print('Voce excedeu o limite de tentativas permitidas!😭\n ')
        break