class Celle:
    # Konstruktør
    def __init__(self) -> None:
        self._status = "doed"
        self._naboer = [] 
        self._ant_levende_naboer = 0
    
    def sett_doed(self) -> None:
        self._status = "doed"   # setter

    def sett_levende(self) -> None:
        self._status = "levende"    # setter

    def er_levende(self) -> bool:
        return True if self._status == "levende" else False # Returnerer en boolsk verdi True eller False dersom den er levende eller ikke

    def hent_status_tegn(self) -> str:
        return "O" if self.er_levende() else "."    # Returnerer "O" dersom celle er levende, ellers "."

    def legg_til_nabo(self, nabo: object) -> None:  # Legger til referanse til celle objekt i en liste til cellen
        self._naboer.append(nabo)

    def tell_levende_naboer(self) -> None:  # Oppdaterer verdien til self._ant_levende_naboer dersom det er levende celler i _naboer listen
        naboer = 0
        for celle in self._naboer:
            if celle.er_levende():
                naboer += 1
        self._ant_levende_naboer = naboer

    def oppdater_status(self) -> None:  # Oppdaterer status basert på antall levende naboer
        if self.er_levende():
            if self._ant_levende_naboer < 2:
                self.sett_doed()
            elif self._ant_levende_naboer > 3:
                self.sett_doed()

        else:
            if self._ant_levende_naboer == 3:
                self.sett_levende()