"""
Programmet er om å finne antall ord i en setning og antall bokstaver i et ord
"""
def antall_bokstaver(ord):
    antall = 0
    for bokstav in ord:
        antall += 1
    return antall

def antall_ord_setning(setning):
    setning_liste = setning.split()
    frekvens = {}
    for ord in setning_liste: # Lagrer i en ordbok med ord som nøkkel og teller som frekvens
        if ord in frekvens:
            frekvens[ord] += 1
        else:
            frekvens[ord] = 1

    for ord in frekvens:
        print(f"Ordet {ord} forekommer {frekvens[ord]} gang, og har {antall_bokstaver(ord)} bokstaver")


def main():
    setning = input("Skriv en setning\n> ")
    setning_liste = setning.split()
    print(f"Det er {len(setning_liste)} ord i setningen din.")
    antall_ord_setning(setning)

main()