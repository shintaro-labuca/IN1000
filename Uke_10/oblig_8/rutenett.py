from random import randint
from celle import Celle

class Rutenett:
    def __init__(self, rader: int, kolonner: int):
        self._ant_rader = rader
        self._ant_kolonner = kolonner
        self._rutenett = self._lag_tomt_rutenett()

    def _lag_tomt_rutenett(self) -> list:   # Lager en to-dimensjonal liste fylt med None-verdier basert på antall rader og kolonner gitt ved opprettelse av en rutenett-objekt
        rutenett = []
        for _ in range(self._ant_rader):
            rad = self._lag_tom_rad()
            rutenett.append(rad)
        return rutenett

    def _lag_tom_rad(self) -> list: # Lager en liste med None-verdier basert på antall kolonner, som blir en rad
        liste = []
        for _ in range(self._ant_kolonner):
            liste.append(None)
        return liste
        

    def fyll_med_tilfeldige_celler(self) -> None:   # Itererer gjennom rutenett-lista og kaller på lag_celle() for hver plass
        for rad in range(self._ant_rader):
            for kolonne in range(self._ant_kolonner):
                self._rutenett[rad][kolonne] = self.lag_celle(rad, kolonne)

    def lag_celle(self, rad, kol) -> Celle:  # Lager en Celle-objekt og bestemmer om den er levende via 1/3 sjanse
        celle = Celle()
        if randint(0,2) == 2:
            celle.sett_levende()
        return celle

    def hent_celle(self, rad, kol): # Returnerer referanse til celle-objekt, ellers None hvis det ikke finnes
        if 0 <= rad < self._ant_rader:
            if 0 <= kol < self._ant_kolonner:
                return self._rutenett[rad][kol] 
        return None
    
    def tegn_rutenett(self) -> None:    #Går gjennom hver plass i rutenettet, skriver ut cellens status, "O" om den er levende, "." hvis ikke
        for rad in range(self._ant_rader):
            for kolonne in range(self._ant_kolonner):
                print(self._rutenett[rad][kolonne].hent_status_tegn(), end="")
            print()

    def _sett_naboer(self, rad, kol) -> None:
        celle = self._rutenett[rad][kol]    #Definerer en gitt celle

        for nabo_rad in range(rad-1, rad+2):    # For radene over, raden med cellen, og raden under
            for nabo_kol in range(kol-1, kol+2):    # For kol ved siden, kol med celle, og kol ved siden

                if nabo_rad == rad and nabo_kol == kol: # Hvis det er samme posisjon som den gitte cellen, hopp over
                    continue
                
                nabo = self.hent_celle(nabo_rad, nabo_kol)
                if nabo == None:    # Hvis det er utenfor det det definerte området, hopp over
                    continue
                
                celle.legg_til_nabo(nabo)   # Legger til gyldige celler i self._naboer listen til den gitte cellen


    def koble_celler(self) -> None: # Kobler cellene med hverandre
        for rad in range(self._ant_rader):
            for kolonne in range(self._ant_kolonner):
                self._sett_naboer(rad, kolonne)

    def hent_alle_celler(self) -> list["Celle"]: # Returnerer en liste med alle referanser til celle-objekter
        celle_liste = []
        for rad in self._rutenett:
            for celle in rad:
                celle_liste.append(celle)
        return celle_liste
    
    def antall_levende(self) -> int:   # Teller antall levende celler
        levende = 0
        liste_celler = self.hent_alle_celler()
        for celle in liste_celler:
            if celle.er_levende():
                levende += 1
        return levende
