n1 = int (input("me informe o primeiro numero "))
n2 = n1
while (n2 == n1):
    n2 = int (input("me informe o segundo numero "))
    if (n1 == n2):
        print("digite um numero diferente ")
n3 = int(input("digite o terceiro numero "))
while (n2 == n3) or (n1 == n3):
    print("digite um numero diferente")
    n3 = int(input("digite o terceiro numero "))
if (n1 >= n2) and (n1 >= n3):
    maior = n1
    if (n2 >= n3):
        maior2 = n2
    else:
        maior2 = n3
elif (n2 >= n1) and (n2 >= n3):
    maior = n2
    if (n1 >= n3):
        maior2 = n1
    else:
        maior2 = n3
else:
    maior = n3
    if (n1 >= n2):
        maior2 = n1
    else:
        maior2 = n2

print(f"o primeiro maior = {maior} e segundo maior e = {maior2}")
print(f"a soma do dois = {maior+maior2}")
        
    
    



