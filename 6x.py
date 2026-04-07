usario = int(input("digite seu usuario "))
senha = 0
f = 0
login = 0
if (usario != 1234) and (usario != 4050) and (usario != 2530):
    for i in range(1,5):
        print("usuario incorreto")
        usario = int(input("digite seu usuario novamente :  "))
        if (usario == 1234) or (usario == 4050) or (usario == 2530):
             break
if (usario != 1234) and (usario != 4050) and (usario != 2530):
     print("Tentativas Esgotadas!!!!")
     print(" Solicite o seu cadastramento antes de realizar o login!\n")
     login = int(input("Crie seu usuario\n"))
     usario =  login
     novasenha = int(input("digite sua nova senha "))    
if (usario == 1234) or (usario == 4050) or (usario == 2530):
        print("o seu usario :",usario)
        senha =  int(input("digite sua senha : "))
if (usario == login):
        print("o seu usuario :",usario)
        senha =  int(input("digite sua senha : "))   
if (usario == 1234) and (senha != 9999) or ((usario == 2530 )and (senha != 3333)) or ((usario == 4050) and (senha != 2222)) or ((usario == login) and (senha != novasenha)) :
             for i in range(1,3):
                print("senha incorreta")
                senha = int(input("digite sua senha  novamente : "))
                if (usario == 1234) and (senha == 9999):
                    print("Acesso Permitido para usuario 1234")
                    f = 10
                    break
                if (usario == 4050) and (senha == 2222) :
                    print("Acesso Permitido para usuario 4050")
                    f = 10
                    break
                if (usario == 2530) and (senha == 3333) :
                    f = 10
                    print("Acesso Permitido para usuario 2530")
                    break
                if (usario == login) and (senha == novasenha) :
                    f = 10
                    print("Acesso Permitido para usuario ",login)
                    break
if (usario == 1234) and (senha == 9999) and (f != 10):
    print("Acesso Permitido para usuario 1234")
if (usario == 2530) and (senha == 3333) and (f != 10): 
    print("Acesso Permitido para usuario 2530")
if (usario == 4050) and (senha == 2222) and (f != 10):
    print("Acesso Permitido para usuario 4050")
if (usario == login) and (senha == novasenha) and (f != 10):
    print("Acesso Permitido para usuario ",login)
if(senha != 9999) and (senha != 2222) and (senha != 3333) and (senha != novasenha):
     print("Não foi possível realizar o login! ") 
 

            