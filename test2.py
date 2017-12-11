j=0
i=j+1
h = 0
kuud = []


for i in range(12):
    h=h+1
    print (h, ".kuu")
    a = int(input("Mis on sinu kuupalk?"))
    kuud.append(a)

maks = 0
maksuta = 0
k = 0
j = 0

for k in kuud:
    j=j+1
    maks = (k*0.964)
    maksuta = (maks - 180) * 0.2
    neto = str(maks - maksuta)
    print (j, ". kuu netopalk on: " + neto)
