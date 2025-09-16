"""
Reiseplan
"""

def main():

    print("Her skal du lagre reiser.")
    reise_1 = ["Frankrike", "Mat", "20.08"]
    reise_2 = ["Brazil", "Shorts", "21.08"]
    reise_3 = ["Danmark", "Jakke", "22.08"]

    reise_liste = [reise_1, reise_2, reise_3]

    for reise in reise_liste:
        print(reise)
    
    hent_reise = int(input(f"Hvilken reise vil du hente info om?\n\
    Skriv tallet som du vil se mer om\n\
    1: \n\
    2: \n\
    3: \n\
    > "))
    hent_kategori = (input("Hvilken kategori vil du se på av reisen? Skriv kategorien\n\
    1: Reisemål\n\
    2: Klær\n\
    3: Avreisedato:\n\
    > "))


    if -1 < hent_reise - 1 < 3:
        if hent_kategori == "Reisemål":
            hent_kategori = 1
            print(f"Du valgte reise {hent_reise} og kategori {hent_kategori}: {reise_liste[hent_reise - 1][hent_kategori - 1]}")
        elif hent_kategori == "Klær":
            hent_kategori = 2
            print(f"Du valgte reise {hent_reise} og kategori {hent_kategori}: {reise_liste[hent_reise - 1][hent_kategori - 1]}")
        elif hent_kategori == "Avreisedato":
            hent_kategori = 3
            print(f"Du valgte reise {hent_reise} og kategori {hent_kategori}: {reise_liste[hent_reise - 1][hent_kategori - 1]}")
        else:
                print("Du har valgt tall utenfor menyen.")
    else:
                print("Du har valgt tall utenfor menyen.")

        
    
main()