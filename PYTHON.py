#Ül 1 /  Kirjutada programm, mis küsib inimeselt kasutajasisendi kaudu
#iga kuu palga ühes aastas. Seejärel peab programm iga kuu palgast
#maha arvestama maksud ja maksuvaba tulu ning lisama vastavad netopalgad faili.
#

jaanuar = int(input("Sisesta jaanuari kuu palk ümardatult täisarvuni: "))

veebruar = int(input("Sisesta veebruari kuu palk ümardatult täisarvuni: "))
märts = int(input("Sisesta märtsi kuu palk ümardatult täisarvuni: "))
aprill = int(input("Sisesta aprilli kuu palk ümardatult täisarvuni: "))
mai = int(input("Sisesta mai kuu palk ümardatult täisarvuni: "))
juuni = int(input("Sisesta juuni kuu palk ümardatult täisarvuni: "))
juuli = int(input("Sisesta juuli kuu palk ümardatult täisarvuni: "))
august = int(input("Sisesta augusti kuu palk ümardatult täisarvuni: "))
september = int(input("Sisesta septembri kuu palk ümardatult täisarvuni: "))
oktoober = int(input("Sisesta oktoobri kuu palk ümardatult täisarvuni: "))
november = int(input("Sisesta novembri kuu palk ümardatult täisarvuni: "))
detsember = int(input("Sisesta detsembri kuu palk ümardatult täisarvuni: "))



jaanuarmaksud = (jaanuar*0.964)
jaanuarmaksuvaba = (jaanuarmaksud - 180) * 0.2
jaanuarneto = str(jaanuarmaksud - jaanuarmaksuvaba)
print ("Jaanuari netopalk on: " + jaanuarneto)

veebruarmaksud = (veebruar*0.964)
veebruarmaksuvaba = (veebruarmaksud - 180) * 0.2
veebruarneto = str(veebruarmaksud - veebruarmaksuvaba)
print ("Veebruari netopalk on: " + veebruarneto)

märtsmaksud = (märts*0.964)
märtsmaksuvaba = (märtsmaksud - 180) * 0.2
märtsneto = str(märtsmaksud - märtsmaksuvaba)
print ("Märtsi netopalk on: " + märtsneto)

aprillmaksud = (aprill*0.964)
aprillmaksuvaba = (aprillmaksud - 180) * 0.2
aprillneto = str(aprillmaksud - aprillmaksuvaba)
print ("Aprilli netopalk on: " + aprillneto)

maimaksud = (mai*0.964)
maimaksuvaba = (maimaksud - 180) * 0.2
maineto = str(maimaksud - maimaksuvaba)
print ("Mai netopalk on: " + maineto)

juunimaksud = (juuni*0.964)
juunimaksuvaba = (juunimaksud - 180) * 0.2
juunineto = str(juunimaksud - juunimaksuvaba)
print ("Juuni netopalk on: " + juunineto)

juulimaksud = (juuli*0.964)
juulimaksuvaba = (juulimaksud - 180) * 0.2
juulineto = str(juulimaksud - juulimaksuvaba)
print ("Juuli netopalk on: " + juulineto)

augustmaksud = (august*0.964)
augustmaksuvaba = (augustmaksud - 180) * 0.2
augustneto = str(augustmaksud - augustmaksuvaba)
print ("Augusti netopalk on: " + augustneto)

septembermaksud = (september*0.964)
septembermaksuvaba = (septembermaksud - 180) * 0.2
septemberneto = str(septembermaksud - septembermaksuvaba)
print ("Septembri netopalk on: " + septemberneto)

oktoobermaksud = (oktoober*0.964)
oktoobermaksuvaba = (oktoobermaksud - 180) * 0.2
oktooberneto = str(oktoobermaksud - oktoobermaksuvaba)
print ("Oktoobri netopalk on: " + oktooberneto)

novembermaksud = (november*0.964)
novembermaksuvaba = (novembermaksud - 180) * 0.2
novemberneto = str(novembermaksud - novembermaksuvaba)
print ("Novembri netopalk on: " + novemberneto)

detsembermaksud = (detsember*0.964)
detsembermaksuvaba = (detsembermaksud - 180) * 0.2
detsemberneto = str(detsembermaksud - detsembermaksuvaba)
print ("Detsembri netopalk on: " + detsemberneto)



f = open("palgad.txt", "w")
f.write("Jaanuari netopalk on: " + jaanuarneto + "\n")
f.write("Veebruari netopalk on: " + veebruarneto + "\n")
f.write("Märtsi netopalk on: " + märtsneto + "\n")
f.write("Aprilli netopalk on: " + aprillneto + "\n")
f.write("Mai netopalk on: " + maineto + "\n")
f.write("Juuni netopalk on: " + juunineto + "\n")
f.write("Juuli netopalk on: " + juulineto + "\n")
f.write("Augusti netopalk on: " + augustneto + "\n")
f.write("Septembri netopalk on: " + septemberneto + "\n")
f.write("Oktoobri netopalk on: " + oktooberneto + "\n")
f.write("Novembri netopalk on: " + novemberneto + "\n")
f.write("Detsembri netopalk on: " + detsemberneto + "\n")
f.close()
























    