'''
Programmet jobber med utskrift og innlesing med ulike variabler
'''

#2.
print("Hei Student!") #Skriver ut Hei Student"

#3. Ber bruker om å skrive inn navnet, \n betyr at "Skriv her" kommer på en ny linje på terminalen
navn = input("Hva heter du?\nSkriv her: ") 

print(f"Hei {navn}\n")      #Skriver ut variabelen navn med strengen ved bruk av f streng

#4.
navn_2 = input("Hva heter vennen din?\nSkriv her: ")    #Lik konsept som linje 2
sammen = f"{navn} {navn_2}"         #Setter sammen variablene ved bruk av f streng
print(sammen)

#5.
sammen = f"{navn} og {navn_2}"      #Endrer variabelen sammen slik at det inkluderer "og"
print(sammen)