def adder(tall1, tall2):    # 1.
    return tall1 + tall2

print(f"Tallene 6 + 7 = {adder(6, 7)}")

print(f"Tallene 9 + 10 = {adder(9, 10)}")


# 2.
streng_bokstav = input("Skriv en streng, deretter en bokstav skilt med ,\n> ")

liste = streng_bokstav.split(",")   # Lager en liste med strengen, og deretter bokstaven

def tell_forekomst(min_tekst, min_bokstav):
    min_tekst = liste[0]    # Strengen liste[0] blir lagret som min_tekst
    min_bokstav = liste[1]  # Bokstaven liste[1] blir lagret som min_bokstav

    antall = 0
    for bokstav in min_tekst:
        if bokstav == min_bokstav:  # For hver bokstav i liste[0] så teller man antall + 1
            antall += 1
    return antall

print(f"Bokstaven {liste[1]} forekommer {tell_forekomst(liste[0], liste[1])} ganger.")