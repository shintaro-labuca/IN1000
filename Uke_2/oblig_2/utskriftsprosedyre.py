"""

Dette er et program som leser inn informasjon om brukeren til en prosedyre
og kaller det tre ganger

"""

def main():

    #Definerer funksjon
    def hilsen():
        navn = input("Skriv inn navn:\n> ")
        bosted = input("Hvor kommer du fra?\n> ")




        print(f"Hei {navn}! Du er fra {bosted}.")
        
    #Kaller funksjonen tre ganger
    hilsen()
    hilsen()
    hilsen()

main()



