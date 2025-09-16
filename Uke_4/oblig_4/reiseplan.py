"""
Reiseplan
"""

def main():

    print("Her skal du lagre reiser.")
    
    reisemål = ["Frankrike", "Brazil", "Norge"]
    pakke = ["Mat", "Shorts", "Jakke"]
    avreise_dato = ["21.08", "22.08", "23.08"]

    """for i in range(3):
        bruker_reisemål = input("Hvor skal du reise?\n> ")
        bruker_pakke = input("Hvilke klær skal du pakke med?\n> ")
        bruker_avreise_dato = input("Når er avreisedatoen?\n> ")

        reisemål.append(bruker_reisemål)
        pakke.append(bruker_pakke)
        avreise_dato.append(bruker_avreise_dato)"""


    reiser = [reisemål, pakke, avreise_dato]
    for reise in reiser:
        print(reise)

    print(f"Her er listen over reisene:\n{reiser[0][0], reiser[0][1], reiser[0][2]}")
    reise = input("Skriv hvilken reise for å se ytterligere informasjon\n> ")
    for reise in reiser:
        if reise in reiser:
            kategori = input("Hvilken kategori vil du se? 1: Reisemål")
main()