def main():
    print("Velkommen til Fangens dilemma. Velg over å svike, eller samarbeide med den andre spilleren.")

    valg_1 = int(input(
    "Spiller 1 - Velg tall mellom å svike eller samarbeide:\n\
    1: Samarbeide\n\
    2: Svike\n\
    > "))

    valg_2 = int(input(
    "Spiller - Velg tall mellom å svike eller samarbeide:\n\
    1: Samarbeide\n\
    2: Svike\n\
    > "))

    def beregn_score(valg_spiller1, valg_spiller2):
        spiller_1 = 0
        spiller_2 = 0
        if (valg_spiller1 == 1) and (valg_spiller2 == 1):
            spiller_1 += 3
            spiller_2 += 3

        elif (valg_spiller1 == 2) and (valg_spiller2 == 2):
            spiller_1 += 1
            spiller_2 += 1
        
        elif (valg_spiller1 == 1) and (valg_spiller2 == 2):
            spiller_1 += 0
            spiller_2 += 5
        
        elif (valg_spiller1 == 2) and (valg_spiller2 == 1):
            spiller_1 += 5
            spiller_2 += 0
        
        score = [spiller_1, spiller_2]
        return score

    print(beregn_score(valg_1, valg_2))

    motspiller = []
    motspiller.append(valg_2)
    
    def spill_snilt(liste):
        pass
    
    print(motspiller)

main()



        
    
