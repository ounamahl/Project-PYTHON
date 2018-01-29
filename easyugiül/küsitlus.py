#Jan - Marten Leivo
#11 IT
#küsitluse ül
from easygui import *
image = ("python_and_check_logo.gif")
msg = ("Milline on Eesti riigis vanus esmase juhiloa omandamiseks?")
msg2 =("Mis aastast kehtib praegune Eesti Vabariigi põhiseadus?")
msg3 = ("Kas sa käid koolis?")
msg4 = ("Kas sa käid trennis?")
msg5 = ("Kas sul on auto?")
msg6 = ("Kas sa tahad magada?")
msg7 = ("Kas sa oled 18?")
nupud = ["Jah", "Ei"]
nupud1 = ["16", "17", "18"]
nupud2 = ["1992", "1938", "1990"]
vastus = buttonbox(msg, image=image, choices=nupud1)
vastus1 = buttonbox(msg2, choices=nupud2)
vastus2 = buttonbox(msg3, choices=nupud)
vastus3 = buttonbox(msg4, choices=nupud)
vastus4 = buttonbox(msg5, choices=nupud)
vastus5 = buttonbox(msg6, choices=nupud)
vastus6 = buttonbox(msg7, choices=nupud)
