def antall_bokstaver(ord):
    antall = 0
    for bokstav in ord:
        antall += 1

    return antall

def antall_ord_setning(setning):
    setning_liste = setning.split()
    frekvens = {}

    for ord in setning_liste:
        if ord in frekvens:
            frekvens[ord] += 1
        else:
            frekvens[ord] = 1
        if frekvens[ord] == 1:
            print(f"Ordet {ord} forekommer {frekvens[ord]} ganger, og har {antall_bokstaver(ord)} bokstaver")
        else:
            pass

def main():
    setning = input("Skriv en setning\n> ")
    setning_liste = setning.split()
    print(f"Det er {len(setning_liste)} ord i setningen din.")
    antall_ord_setning(setning)

main()