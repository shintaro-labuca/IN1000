#Oppgave 3
str_1 = "Hei"
str_2 = "Hade"
str_3 = "Velkommen"

print(str_1, str_2, str_3 )
print("Skriv en av disse ordene som ble skrevet ut ^")

brukerinput = input("Skriv her: ")

if (brukerinput == str_1) or (brukerinput == str_2) or (brukerinput == str_3):
    print(brukerinput)
else:
    print("Du skrev ikke noen av ordene.")

#Oppgave 4
print("\n")
print("Her kommer to nye ord:")
ord = ["Bra", "Dårlig"]
print(ord[0], ord[1])

brukerinput_2 = input("Skriv igjen en av disse ordene som ble skrevet ut\n> ")
if brukerinput_2 in ord:
    print(brukerinput_2)
else:
    print("Du skrev ikke noen av ordene.")
