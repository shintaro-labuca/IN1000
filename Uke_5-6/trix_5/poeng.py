def les_poeng(filnavn):
    poeng = {}

    for linje in open(filnavn):
        linje = linje.strip()
        kolonner = linje.split(":")
        h_kolonne = kolonner[1].split(",")
        nøkkel = kolonner[0]
        sum = 0
        for tall in h_kolonne:
            sum += int(tall)
        poeng[nøkkel] = sum
    
    return poeng

print(les_poeng("poeng.txt"))