måneder = ["januar", "februar", "mars", "april", "mai", "juni", "juli", 
           "august", "september", "oktober", "november", "desember"]

print(
    "Skriv et heltall 1 - 12 og dette skriver ut hvilken måned tallet tilsvarer."
    )

velg = int(input("> "))

if 0 < velg < 13:
    print(f"Dette tilsvarer: {måneder[velg - 1]}")
else:
    print("Ugyldig svar.")
