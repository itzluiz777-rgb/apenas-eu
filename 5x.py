usario = int(input("digite seu usuario "))
senha = 0
if (usario != 1234):
    for i in range(1,5):
        print("usuario incorreto")
        usario = int(input("digite seu usuario novamente :  "))
        if (usario == 1234):
             break
if (usario != 1234):
     print("Tentativas Esgotadas!!!!")
elif (usario == 1234):
        senha =  int(input("digite sua senha : "))
        if (senha != 9999):
             for i in range(1,3):
                print("senha incorreta")
                senha = int(input("digite sua senha  novamente : "))
                if (senha == 9999):
                     break
if (senha!= 9999) and (senha != 0):
     print("Tentativas Esgotadas!!!!")
elif (senha == 9999):
     print("Acesso Permitido ")
            

