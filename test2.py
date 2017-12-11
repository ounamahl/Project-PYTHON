j=0
i=j+1
h = 0
kuud = []


for i in range(3):
    h=h+1
    print (h, ".kuu")
    a = int(input("Mis on sinu kuupalk?"))
    kuud.append(a)

maks = 0
maksuta = 0
k = 0
j = 0


for k in kuud:
    maks = (kuud[]*0.964) #siin on haige mähis
    maksuta = (maks - 180) * 0.2
    neto = str(maks - maksuta)
    print ("netopalk on: " + neto)
