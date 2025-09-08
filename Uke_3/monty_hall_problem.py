import random

def spill():
    print("Velkommen til Monty Hall Problem, velg mellom 3 dører, og vinn en bil!")
    svar = int(input("Velg et dør mellom 0, 1 og 2\n> "))


    bil = random.randint(0,2)  # Tilfeldig helltal fra og med 0 til og med 2
    dører = [0, 1, 2]

    #print(f"Bilen er bak dør: {bil} #debug")    #Debug

    vert = None     #Oppretter en tom variabel utenfor skopen til for loopen
    for dør in dører:   #Iterer gjennom hver element i dører liste
        if dør != svar and dør != bil:  #Sjekker for å se om dør elementet 0 / 1 / 2 er lik noen de andre, hvis ikke, oppdaterer vert til den nye døra    
            vert = dør

    endret_svar = input(f"Verten åpner dør {vert} og her er det en geit! Vil du bytte dør? (ja/nei)\n> ").lower()

    if endret_svar == "ja":
        if svar == bil:     #Hvis svar opprinnelig var samme dør som bil, så har bruker byttet dør og ikke vunnet
            print("Desverre du vant ikke en bil.")

        elif svar != bil:   #Hvis var ikke var bil, endrer den svaret til å være bil
            for endre in dører:
                if endre != svar and endre != vert:     #Lik konsept som kodeblokken 12-15
                    svar = endre
            print("Gratulerer, du vant en bil!")

    if endret_svar == "nei":
        if svar == bil:
            print("Gratulerer, du vant en bil!")
        else:
            print("Dessverre du vant ikke en bil.")

spill()


### 3a.


antall_seiere = 0

def spill_hardkodet_nei():
    svar = 0
    bil = random.randint(0,2)  # Tilfeldig helltall fra og med 0 til og med 2
    if svar == bil:
        return 1
    else:
        return 0

for i in range(100000):
    antall_seiere += spill_hardkodet_nei()

print(f"Vinnertall ved å beholde dør hver gang: {antall_seiere}")


### 3d.

def spill_hardkodet_ja():
    svar = 0

    bil = random.randint(0,2)  # Tilfeldig helltal fra og med 0 til og med 2
    dører = [0, 1, 2]

    vert = None     #Oppretter en tom variabel utenfor skopen til for loopen
    for dør in dører:   #Iterer gjennom hver element i dører liste
        if dør != svar and dør != bil:  #Sjekker for å se om dør elementet 0 / 1 / 2 er lik noen de andre, hvis ikke, oppdaterer vert til den nye døra    
            vert = dør

    endret_svar = True #Altså bruker sier ja til å bytte dør

    if endret_svar:
        if svar == bil:     #Hvis svar opprinnelig var samme dør som bil, så har bruker byttet dør og ikke vunnet
            return 0

        elif svar != bil:   #Hvis svar ikke var bil, endrer den svaret til å være bil
            for endre in dører:
                if endre != svar and endre != vert:     #Lik konsept som kodeblokken 12-15
                    svar = endre
            return 1
    

antall_seiere = 0
for i in range(100000):
    antall_seiere += spill_hardkodet_ja()

print(f"Vinnertall ved å endre dør hver gang: {antall_seiere}")
