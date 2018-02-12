#Let it begin
import webbrowser
print("Veebilehed: 1 - Tamme stuudium; 2 - YouTube; 3 - Facebook; 4 - auto24")
mislehte = input("Mis veebilehele minna soovid? ")

üks = "tamme.ope.ee"
kaks = "www.youtube.com"
kolm = "www.facebook.com"
neli = "www.auto24.ee"

if mislehte == '1':
    webbrowser.open_new(üks)
if mislehte == '2':
    webbrowser.open_new(kaks)
if mislehte == '3':
    webbrowser.open_new(kolm)
if mislehte == '4':
    webbrowser.open_new(neli)





