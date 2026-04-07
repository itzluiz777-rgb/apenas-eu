h1 = int(input("me fala idade do primeiro homen"))
h2 = h1 
while h1 == h2 :
    h2 = int(input("digite a idade de homen que seja diferente "))

m1 = int(input("qual a idade do primeira mulher"))
m2 = m1
while m1 == m2 :
    m2 = int(input("digite a idade de mulher que seja diferente "))
if h1 > h2 :
    hm =  h1
else:
    hm = h2
if m1 > m2 :
    mm =  m1
else:
    mm = m2
if h1 < h2:
    hmenor = h1
else:
    hmenor = h2
if m1<m2:
    mmenor = m1
else:
    mmenor = m2
print(f"homen mais velhor idade {hm} mulher mais nova idade {mmenor} soma = {hm+mmenor}")
print(f"homen mais novo idade {hmenor} mulher mais nova idade {mm} produto = {hmenor*mm}")



