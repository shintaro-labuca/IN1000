
a = input("Tast inn et heltall! ")
b = int(a)
if b < 10:
    print(b + "Hei!")



#1. Programmet ovenfor vil ikke kunne kjøre ved b < 10 fordi da vil man få en error
#   der det står at man ikke kan concatenate literals med typen int + str
#   (Etter kjøring så ble det TypeError unsupported operands)

#2. Når man skriver et heltall 10 og over så kjøre programmet uten å vise til noe siden ingenting
#   er definert ved b >= 10. I tillegg til at det bare blir error