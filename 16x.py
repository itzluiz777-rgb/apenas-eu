palavra = str(input("me fala um frase "))
primeiro = ""
segundo = ""
ultimo = ""
penultimo = ""
for i in range(0,len(palavra)):
    if (i == 0) :
        primeiro = palavra[i]
    if (i == 1) :
        segundo = palavra[i]
    if (len(palavra)-2 == i):
        penultimo = palavra[i]
    if (len(palavra)-1 == i):
        ultimo = palavra[i]

print (f"primeiro,segundo,penultimo,ultimo  = {primeiro},{segundo},{penultimo},{ultimo}")