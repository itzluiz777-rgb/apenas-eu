palavra = str(input("me fala um frase "))
qv = 0
qc = 0
for i in range(0,len(palavra)):
    if ( palavra[i] == "a") or ( palavra[i] == "e") or ( palavra[i] == "i") or ( palavra[i] == "o") or ( palavra[i] == "u"):
        qv += 1
    else:
        qc += 1
print("a quantidade de vogais :",qv)
print("a quantidade de cosoantes :",qc)  