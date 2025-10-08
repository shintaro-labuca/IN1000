from sau import Sau
from ulv import Ulv
import random

class Verden:
    def __init__(self) -> None:
        self._sauer = []
        self._ulver = []

    def opprett_dyr(self, type: str, navn: str, posisjon: int):
        if type == "sau":
            sau = Sau(navn, posisjon)
            self._sauer.append(sau)
        elif type == "ulv":
            ulv = Ulv(navn, posisjon)
            self._ulver.append(ulv)
    
    def beskriv(self):
        print("Antall sauer med navn og posisjon:")
        for sau in self._sauer:
            print(f"Sauen heter {sau.hent_navn()} og befinner seg i posisjon: {sau.hent_posisjon()}")

        print("Antall ulver med navn og posisjon")
        for ulv in self._ulver:
            print(f"Ulven heter {ulv.hent_navn()} og befinner seg i posisjon: {ulv.hent_posisjon()}")

        
    def antall_sauer(self):
        antall = 0
        for sau in self._sauer:     # Levende sauer
            if sau.lever():
                antall += 1
        return antall
        
    def antall_ulver(self):
        return len(self._ulver)
        
    def oppdater(self):
        for ulv in self._ulver:
            retning = random.choice([-1, 1])    # Venstre eller høyre
            if retning == 1:
                ulv.beveg_høyre()
            else:
                ulv.beveg_venstre()

            for sau in self._sauer:
                if sau.lever() and sau.hent_posisjon() == ulv.hent_posisjon():  # Sjekker kollisjon og spiser deretter 
                    ulv.spis_sau(sau)
                    print(f"Ulven {ulv.hent_navn()} spiser sauen {sau.hent_navn()} på posisjon {sau.hent_posisjon()}")


    def finn_feiteste_ulv(self):
        ulv_vekt = self._ulver[-1].hent_vekt()  # Første ulv
        for ulv in self._ulver:
            if ulv.hent_vekt() > ulv_vekt:
                ulv_vekt = ulv.hent_vekt()
        return ulv_vekt



        