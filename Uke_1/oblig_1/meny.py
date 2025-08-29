'''

Programmet handler om å skrive ut en meny der brukeren bes om å velge en ut hovedrett og tilbehør fra listen
Deretter får brukeren en kommentar basert på deres valg.

'''

#1. Definerer menyen
meny = ["biff", "torsk", "salat"]
tilbehør = ["gulrøtter", "bearnaise"]

#Printer ut menyen ved hjelp av for loop
print("Her er restaurantmenyen våres ")
print("Hovedretter:")
for hovedretter in meny:
    print(hovedretter)

print("Her er tilbehøret som tilhører hovedrettene: ")
for tilbehører in tilbehør:
    print(tilbehører)

#2. Bruker velger en hovedrett og tilbehør
hovedrett = input("Velg en hovedrett: ").lower()
tilbehør = input("Velg en tilbehør: ").lower()

#3. Løser oppgaven ved hjelp av if/else setning 
if (hovedrett == "biff" or "torsk") and tilbehør == "bearnaise":
    print("Du spiser ikke nok grønnsaker!")

elif hovedrett == "salat" and tilbehør == "gulrøtter":
    print("Du har valgt et vegetarmåltid.")

else:

    print(f"Du har valgt {hovedrett} med {tilbehør}.")