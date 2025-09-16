"""
Bruk av while- og for-løkker for å løse problemer
"""
# 1.
def liste_whilelokke():
    liste =[]
    teller = 0
    while teller <= 10:
        liste.append(teller)
        teller += 1
    print(liste)
liste_whilelokke()

# 2.
def liste_forlokke():
    liste = []
    for tall in range(11):
        liste.append(tall)
    print(liste)
liste_forlokke()

# 3.
"""
I while løkke så kjører man den med en teller slik at den når en maksimum til når den stopper
I en for-løkke så kan man kjøre range antall ganger man vil den skal kjøre
"""

# 4.
"""
a. Det finnes en slags samling i range() funksjonen. 
b. Man får en liste med integers
"""

# 5 - 9.
def øke_med_3():
    liste = []
    for tall in range(0,20,3):
        liste.append(tall)
    print(liste)
    
    for i in range(len(liste)):
        print(i)

    for tall in range(len(liste)):
        liste[tall] = liste[tall] * 10
    print(liste)
øke_med_3()

