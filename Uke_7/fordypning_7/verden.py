from sau import Sau
from ulv import Ulv

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
            print(f"Ulven heter {ulv.hent_navn()} og befinner seg i posisjon: {ulv.hent.posisjon()}")

        
    def antall_sauer(self):
        antall = 0
        for sau in self._sauer:
            if sau.lever():
                antall += 1
        return antall
        
    def antall_ulver(self):
        return len(self._ulver)
        

        