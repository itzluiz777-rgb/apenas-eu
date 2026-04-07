palavra = str(input("me fala um frase "))
qt = 0

for i in range(0,len(palavra)):
    if ( palavra[i] == "1"):
        qt += 1
print("a quantidade de 1's e :",qt)