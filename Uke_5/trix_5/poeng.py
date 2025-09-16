def les_poeng(filnavn):
    poeng = {}

    for linje in open(filnavn):
        linje = linje.strip()
        kolonner = linje.split(":")
        h_kolonne = kolonner[1].split(",")
        nøkkel = kolonner[0]
        verdi = h_kolonne
        poeng[nøkkel] = verdi
    
    sum = 0
    for liste in poeng.values():
        for poeng in liste:
            poeng = int(poeng)
            sum += poeng
        poeng[nøkkel] = sum
            
    
    

print(les_poeng("poeng.txt"))