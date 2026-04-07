s= int(input("me informe  o salario "))
i = 1
smaior = s
smenor = s
soma = s
qt = 1
while i>0 :
    s= int(input("me informe  o salario "))
    soma +=s
    if  (s>smaior) :
         smaior = s
    if  (s<smenor) :
        smenor = s 
    qt += 1
    para = str(input("deseja parar : sim ou nao"))
    if (para == "sim"):
        break
print("salario maior = ",smaior,"$")
print("salario menor = ",smenor,"$")
print("media salarial =  ",soma/qt,"$")
    
