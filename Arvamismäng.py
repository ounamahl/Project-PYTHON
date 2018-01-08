#Kristofer Parv #Artur Ennok #Jan-Marten Leivo
import random

arvamisi = 0
print("Tere, mis su nimi on ?")
minunimi = input()
keerul = int(input("Mitu korda sa arvata soovid?"))

number = random.randint(1, 20)
print("Nonii, " + minunimi + ", ma mõtlen ühest numbrist, mis jääb 1 ja 20 vahele.")

while arvamisi < keerul:
    print ("Arva, lapseke")
    mõte = input()
    mõte = int(mõte)

    arvamisi = arvamisi + 1

    if mõte < number:
        print ("Pakutud arv on liiga väike")

    if mõte > number:
        print ("Pakutud arv on liiga suur")

    if mõte == number:
        break
if mõte == number:
    arvamisi = str(arvamisi)
    print("Tubli, " + minunimi + "sa arvasid mu numbri " + arvamisi + ". korraga!")

if mõte != number:
    number = str(number)
    print("Ei, sa ei saa hakkama. Number on " + number)
    