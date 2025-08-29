#02.03: Input og datatyper
#a)
str = input("Skriv en streng:\n> ")
inte = int(input("Skriv en integer:\n> "))
float = float(input("Skriv en float\n> "))

#b) Skriver ut hver verdi og deres datatype
print(f"Verdi: {str} Type: {type(str)}")
print(f"Verdi {inte} Type: {type(inte)}")
print(f"Verdi: {float} Type: {type(float)}")

#d)

tilfelle_1 = inte * str
print(type(tilfelle_1))     #Det blir til str

tilfelle_2 = inte * float    #Det blir til float
print(type(tilfelle_2))
print(tilfelle_2)

#tilfelle_3 = str * float    #Det blir til TypeError, man kan ikke gange str med float
#print(type(tilfelle_3))

#e)
print(int(3.8))     #Den rundes ned til nærmeste heltall