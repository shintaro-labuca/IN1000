def format_text(tekst, filnavn, maks_ord):
    fil = open(filnavn, "w")    # Åpner filen
    teller = 0
    ordliste = tekst.split()    # Lager en liste med alle strengene med " " som split
    for ord in ordliste:    # For hvert element ord i listen
        fil.write(ord)  # Skriver inn ordet til filen som parameter
        fil.write(" ")  # Passer på for mellomrom i tekstfilen

        teller += 1
        if teller == maks_ord:
            fil.write("\n")     # Linjeskift
            teller = 0

    fil.close()

format_text("I denne oppgave skal du lage et program som tar inn en tekst og skriver den ut til en fil. I utdatafilen er det maksimalt antall ord som er tillatt per linje.",
            "test.out", 5)