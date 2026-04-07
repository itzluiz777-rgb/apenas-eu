n = int(input("me fala  um número "))
nl = str(n)
inverso = ""
for i in range(len(nl) - 1, -1, -1):
    inverso += nl[i]
print(inverso)