class Onske:
    def __init__(self, beskrivelse: str, antall: int, minimumspris:int):
        self._beskrivelse = beskrivelse
        self._antall = antall
        self._minimumspris = minimumspris
    
    def passer(self, maksimumspris: int) -> bool:
        return self._minimumspris < maksimumspris and not self._antall == 0
    
    def valgt(self):
        self._antall -= 1
        return self._beskrivelse
    
    def __str__(self):
        return f"{self._beskrivelse} minPris: {self._minimumspris}, antall gjenstår: {self._antall}"


class Onskeliste:
    def __init__(self) -> None:
        self._onsker = []
    
    def nytt_onske(self, beskrivelse, antall, minimumspris):
        onske = Onske(beskrivelse, antall, minimumspris)
        self._onsker.append(onske)
    
    def hent_onsker(self, maksimumspris):
        liste = []
        for onske in self._onsker:
            if onske.passer(maksimumspris):
                liste.append(str(onske))
            else:
                liste.append("Ikke valgbart onske")
        return liste
    
    def onske_oppfylles(self, valg_onske: int):
        return self._onsker[valg_onske].valgt()

###

class Gave:
    def __init__(self, beskrivelse: str, giver: str) -> None:
        self._beskrivelse = beskrivelse
        self._giver = giver

    def __str__(self):
        return f"Beskrivelse: {self._beskrivelse}, Giver: {self._giver}"
    

class Juleferiekalender:
    def __init__(self, dager) -> None:
        self._dager = dager
        self._kalender = {}
     
        dagnummer = 25

        for i in range(dager):
            if dagnummer > 31:
                dagnummer = 1

            self._kalender[dagnummer] = None
            dagnummer += 1
     

    def ny_gave(self, beskrivelse, giver, dagnummer):
        self._kalender[dagnummer] = Gave(beskrivelse, giver)

    def hent_dagens_gave(self, dagnummer):
        maaned = "Desember" if dagnummer > 24 else "Januar"

        if dagnummer in self._kalender:
            return f"Gaven: {self._kalender[dagnummer]} åpnes {dagnummer}.{maaned}"
        else:
            return "Ingen gave for denne dagen"
    
    def hent_ant_dager(self):
        return self._dager

class Julegavefikser:
    def __init__(self) -> None:
        pass
