from film import Film

def test_film():
    # __init__
    # Opprett to film-objekter med tittel og produksjonsår du velger selv
    print("Oppretter to filmer")
    # <fyll ut og fjern # på print-setningen>
    film_1 = Film("Hidden Figures", 2016)
    film_2 = Film("The Imitation Game", 2014)
    print()

    # hent_tittel
    # Skriv ut tittel på de to filmene
    print("Skriver ut titler på to filmer:")
    # <fyll ut og fjern # på print-setningen>
    print(film_1.hent_tittel())
    print(film_2.hent_tittel())
    print()

    # ny_skuespiller
    # Legg til to skuespillere og deres roller for en av filmene, skriv ut alt om filmen
    print("Legger til to skuespillere:")
    # <fyll ut og fjern # på print-setningen>
    film_2.ny_skuespiller("Benedict Cumberbatch", "Alan Turing")
    film_2.ny_skuespiller("Keira Knightley", "Joan Clarke")
    print()

    # Prøv å legge inn en av skuespillerne igjen, med en ny rolle, og sjekk at rollen ikke blir endret
    print("Tester ulovlig innlegging av skuespiller")
    # <fyll ut og fjern # på print-setningen>
    film_2.ny_skuespiller("Benedict Cumberbatch", "Hugh Alexander")
    print()

    # skriv_ut_film
    # Skriv ut all informasjon om begge filmer du har lagt inn
    print("Skriver ut all info om to filmer:")
    # <fyll ut og fjern # på print-setningen>
    film_1.skriv_ut_film()
    film_2.skriv_ut_film()
    print()

    # hent_alle_skuespiller_navn
    # Skriv ut skuespillernes navn for den filmen som har to
    print("Henter og skriver ut alle skuespillernavn for en film:")
    # <fyll ut og fjern # på print-setningen>
    # print(film_2.hent_skuespiller_navn())
    for skuespiller in film_2.hent_skuespiller_navn():
        print(skuespiller)
    print()

    # sjekk_periode
    # Sjekk om en film du har lagt inn er i en periode du velger
    # (velg periode som skal gi True og sjekk at dette blir resultatet)
    print ("Sjekker at en film er i oppgitt periode")
    # <fyll ut og fjern # på print-setningen>
    print(film_1.sjekk_periode(1996, 2020))
    print()

    # Sjekk om en film er i en periode som skal gi False
    # (velg samme årstall til begge argumenter og sjekk resultat er False)
    print ("Sjekker at en film ikke kan være produsert før og etter samme år")
    # <fyll ut og fjern # på print-setningen>
    print(film_1.sjekk_periode(2020, 2020))
    print()

    # sjekk_tittel
    # Sjekk om en film har en tittel som starter på en streng som du selv velger
    print ("Sjekker om starten på en films tittel kjennes igjen")
    # <fyll ut og fjern # på print-setningen>
    print(film_2.sjekk_tittel("The I"))
    print()

    
    # __str__
    # Skriv ut film-objekt med print
    print("Skriver ut en film med print (test av __str__)")
    # <fyll ut og fjern # på print-setningen>
    print(film_2)
    print()

    
    # test __eq__ (frivillig)
    print ("tester __eq__ med to ulike filmer:")
    # <fyll ut og fjern # på print-setningen>
    print(film_1.__eq__(film_2))
    
    print("\nTester __eq__ med to like filmer:")
    film_1_test = Film("Hidden Figures", 2016)  #Test variabel
    print(film_1.__eq__(film_1_test))

    # <fyll ut og fjern # på print-setningen>


test_film()