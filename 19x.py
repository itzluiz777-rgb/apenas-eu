n = int(input("me informe um numero falerei se e primo "))
qt = 0
for i in range (1,n+1):
    if (n % i == 0):
       qt += 1
if (qt<=2) :
    print(f"o numero {n} e primo")
else:
     print(f"o numero {n} e nao primo")
