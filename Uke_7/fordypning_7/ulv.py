from sau import Sau

class Ulv:
    def __init__(self, navn: str, posisjon: int) -> None:
        self._navn = navn
        self._posisjon = posisjon
        self._vekt = 20

    def spis_sau(self, sau: Sau) -> None:
        sau.blir_spist()
        self._vekt += 5

    def hent_vekt(self) -> int:
        return self._vekt
    
    def hent_navn(self) -> str:
        return self._navn 
    
    def hent_posisjon(self) -> int:
        return self._posisjon