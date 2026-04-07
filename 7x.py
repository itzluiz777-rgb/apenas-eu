macas =float(input("quanto kilos de maçãs voce quer "))
morango =float(input("quantos kilos de morango voce quer "))
if (macas>=5):
    valor = 4
else:
     valor = 5
if (morango>=5):
    vm = 7.50
else:
     vm = 10
print (f"{macas}Kg de maçãs esta {macas*valor}R$")
print (f"{morango}Kg de maças esta {morango*vm}R$")
