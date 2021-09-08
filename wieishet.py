import sys

geel = input("Is de kaas geel? ")

if geel == "ja":
    gaten = input("Zitten er gaten in? ")
    if gaten == "ja":
        duur = input("Is de kaas belachelijk duur? ")
        if duur == "ja":
            print("Emmenthaler")
            sys.exit()
        else:
            print("leerdammer")
            sys.exit()
    hard = input("Is de kaas hard als steen? ")
    if hard == "ja":
       print("Pamigiano Reggiano")
    else:
        print("Goudse kaas")
blauw = input("Heeft de kaas blauwe schimmels? ")
if blauw == "ja":
    korst = input("heeft de kaas een korst? ")
    if korst == "ja":
        print("Bleu de Rochbaron")
        sys.exit()
    else:
        print("Foume d'Ambert")
        sys.exit()
korst2 = input("Heeft de kaas een korst? ")
if korst2 == "ja":
    print("Camembert")
else:
    print("Mozzarella")