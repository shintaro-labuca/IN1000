import random
print("Velkommen til Monty Hall Problem, velg mellom 3 dører, der en av de er en bil")
svar = int(input("Velg et dør mellom 0, 1 og 2\n> "))

endret_svar= int(input(
    "En av de andre dørene åpnes og der er det ingenting, vil du velge på nytt mellom de to resterende dører?\n> "
    ))



bil = random.randint(0, 2)  # Tilfeldig helltal fra og med 0 til og med 2

