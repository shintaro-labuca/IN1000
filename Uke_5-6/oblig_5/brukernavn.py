"""
Program som registrerer nye brukere og produserer e-postadresser for dem.
"""

# 1.
def lag_brukernavn(navn):
    navn_liste = navn.split()
    brukernavn = navn_liste[0].lower()  # Blir "kari" ved "Kari Nordmann"
    for bokstav in navn_liste[1].lower():
        brukernavn = brukernavn + bokstav   # Legger til første bokstav i siste navnet "karin"
        break
    return brukernavn
assert lag_brukernavn("Kari Nordmann") == "karin"

# 2.
def lag_epost(brukernavn, suffix):
    pass

# 3.
def skriv_ut_eposter(ordbok):
    pass

# 4.
def main():
    pass
