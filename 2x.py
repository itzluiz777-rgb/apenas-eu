for i in range(1,6):
    print(f"exucuçao numero {i} ")
    n1 = int (input("me informe o primeiro numero "))
    n2 = int (input("me informe o segundo numero "))
    n3 =  int (input("me informe o teceiro numero "))
    if (n1>n2 ) and (n1>n3) :
        maior = n1
    if (n2>n1 ) and (n2>n3) :
        maior = n2
    if (n3>n1) and (n3>n2)  :
        maior = n3 
    print(f"maior da  {i} sequencia : ")
    print(maior)


    
    
