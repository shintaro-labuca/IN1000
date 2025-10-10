class Film:
    def __init__(self, tittel: str, år: int) -> None:
        self._tittel = tittel
        self._år = år
        self._skuespillere = {}
    
    def hent_tittel(self) -> str:   # Getter
        return self._tittel
    
    def hent_år(self) -> int:   # Getter
        return self._år
    
    def ny_skuespiller(self, navn: str, rolle: str):    # Lagrer skuespiller i ordbok hvis den ikke finnes
        if navn in self._skuespillere:
            print(f"Feil: {navn} er allerede i lista med skuespillere")
        else:
            self._skuespillere[navn] = rolle

    def hent_skuespiller_navn(self) -> list[str]:    # returnerer en liste over skuespillerne i filmen
        skuespille_liste = []
        for skuespiller in self._skuespillere:
            skuespille_liste.append(skuespiller)
        return skuespille_liste
    
    def skriv_ut_film(self):    # Printer ut all info om filmen
        print(f"{self._tittel} ({self._år}). Medvirkende:")
        for skuespiller, rolle in self._skuespillere.items():
            print(f"{skuespiller} som {rolle}")
    
    def sjekk_periode(self, år_1: int, år_2: int):
        return år_1 < self._år < år_2               
    
    def sjekk_tittel(self, tittel_start: str):
        if (tittel_start in self._tittel) or (tittel_start == ""):
            return True
        elif len(tittel_start) > len(self._tittel):
            return False
        else:
            return False
    
    def __str__(self) -> str:
        tekst = f"Film: {self._tittel} ({self._år})\n"
        if self._skuespillere:          # Returner True hvis det finnes noe i ordboken
            tekst += "Medvirkende:\n"   # Skriver ut dersom det er registrerte skuespillere til film-objektet
            for skuespiller, rolle in self._skuespillere.items():
                tekst += f"{skuespiller} som {rolle}\n"
        return tekst

    def __eq__(self, annen_film) -> bool:
        return self.hent_tittel() == annen_film.hent_tittel() and self.hent_år() == annen_film.hent_år() # Bruker getters og sjekker verdiene mot hverandre
        