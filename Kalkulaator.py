
def liitmine(x, y):
   return x + y


def lahutamine(x, y):
   return x - y


def korrutamine(x, y):
   return x * y


def jagamine(x, y):
   return x / y



 
valik = input("Valige tehe sisestades järjekorra number(1-liitmine, 2-lahutamine, 3-korrutamine, 4-jagamine):")

number1 = int(input("Sisestage esimene number: "))
number2 = int(input("Sisestage teine number: "))

if valik == '1':
   print(number1,"+",number2,"=", liitmine(number1,number2))

elif valik == '2':
   print(number1,"-",number2,"=", lahutamine(number1,number2))

elif valik == '3':
   print(number1,"*",number2,"=", korrutamine(number1,number2))

elif valik == '4':
   print(number1,"/",number2,"=", jagamine(number1,number2))
else:
   print("Pole sellist valikut")