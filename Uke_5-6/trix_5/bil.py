

def les_bil(filnavn):

    resultatet = {}


    for linje in open(filnavn):
        linje = linje.strip()
        kolonner = linje.split(":")
        nøkkel = kolonner[0]
        verdi = kolonner[1]
        resultatet[nøkkel] = verdi
    return resultatet

print(les_bil("bil.txt"))