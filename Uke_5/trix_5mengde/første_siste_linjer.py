def opprett_filen(filnavn): #Funksjon som oppretter fil med filnavn

    fil = open(filnavn, "w") # Åpner filen, "w" for å skrive til
    fil.write("Hei\n")
    fil.write("DKDK\n")
    fil.write("FEFJ\n")
    fil.write("FIEJF:\n")
    fil.write("EOFJEOF\n")
    fil.write("FEFIE\n")
    fil.write("FJEIENA\n")
    fil.write("FIEJFOIJ\n")
    fil.write("IFGIN\n")
    fil.write("GEKPO\n")

    fil.close()

opprett_filen("test.in")

def skriv_ut_første_linjer(filnavn, antall_linjer):
    fil = open(filnavn)     # Åpner filen
    teller = 0
    for linje in fil:   # For hver linje i fil
        linje = linje.strip()   # Stripper whitespaces 
        print(linje)
        teller += 1
        if teller == antall_linjer:     # Sørger for at de kun første linjene skrives ut
            break
    fil.close()

def skriv_ut_siste_linjer(filnavn, antall_linjer):
    fil = open(filnavn) 
    linjer = []     # Lager en liste med alle linjer i filen
    for linje in fil:
        linjer.append(linje.strip())
    
    start = len(linjer) - antall_linjer     # Finner ut de siste indeksene fra listen
    for linje in linjer[start:]:    # [start:] sørger for at for løkken starter fra indeksen og utover
        print(linje.strip())
    fil.close()
        

skriv_ut_første_linjer("test.in", 2)
skriv_ut_siste_linjer("test.in", 3)

