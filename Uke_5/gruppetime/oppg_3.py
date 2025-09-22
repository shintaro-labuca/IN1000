#


def heie(tabellplass_ordbok):
    # Verdi i ordboka for nøkkelen "Brann" er lik 3 eller mindre, returner Brann
    # else returner nøkkelen som i ordboka er koblet til verdien 1

    if tabellplass_ordbok["Brann"] <= 3:
        return "Brann"

    else:
        for lag, plass in tabellplass_ordbok.items():
            if plass == 1:
                return lag
    

tabellplass_1 = {"Brann": 2,"Rosenborg": 4, "Odd": 1, "Molde": 3}
tabellplass_2 = {"Rosenborg": 2, "Odd": 1, "Molde": 3, "Brann": 4}

print(heie(tabellplass_1))
print(heie(tabellplass_2))