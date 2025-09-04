"""
Dette er et program som jobber med å aksessere data og skriv inn data på lister
"""

def main():
    #1. Appender ny tall i liste
    liste = [1,2,3]
    liste.append(4)
    print(liste[0], liste[2])

    #2. Beregner sum og produkt av listen
    summen = sum(liste) #sum funksjon

    produkt = 1
    for tall in liste: #for loop for å beregne produkt av alle tallene i lista
        produkt * tall

    sum_produkt_liste = [summen, produkt]

    ny_liste = []
    ny_liste.append(liste)
    ny_liste.append(sum_produkt_liste)
    print(ny_liste)     # Ny liste som inneholder opprinnelig og ny liste

    #3.
    navn_liste = []
    for i in range(3):      #Looper tre ganger for å oppgi tre navn
        navn = input("Skriv et navn.\n> ")
        navn_liste.append(navn)

    #4.
    if "Shintaro" in navn_liste:
        print("Du husket meg!")
    else:
        print("Glemte du meg?")




main()