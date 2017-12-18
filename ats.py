#Programm, mis küsib kasutajalt alkohoolse joogi hinda Eestis
#(vastavalt, siis erinevate aktsiisidega lahjem alko, kangem alko)
#ja väljastab kasutajale selle joogi umbkaudse aktsiisihinna Läti riigis ja vahe/võidu.
#Viina aktsiis liitri kohta Eestis 9.56
#Viina aktsiis liitri kohta Lätis 5.80
#Õlle aktsiis liitri kohta Eestis 0.74
#Õlle aktsiis liitri kohta Lätis 0.22
jook = str(input("(Sisesta jook väikeste tähtedega) Mis jooki ostate?"))
kogus = int(input("Mitu liitrit ostate?"))
if jook == ("viin"):
    eesti = (kogus*9.56)
    läti = (kogus*5.8)
    vahe = (eesti - läti)
    print ("Eestis maksaksite aktsiisi", eesti , "eurot.")
    print ("Lätis maksaksite aktsiisi", läti , "eurot.")
    print ("Lätist ostes võidaksite", vahe , "eurot.")

elif jook == ("õlu"):
    eesti1 = (kogus*0.74)
    läti1 = (kogus*0.22)
    vahe1 = (eesti1 - läti1)
    print ("Eestis maksaksite aktsiisi", eesti1 , "eurot.")
    print ("Lätis maksaksite aktsiisi", läti1 , "eurot.")
    print ("Lätist ostes võidaksite", vahe1 , "eurot.")
    
    
    