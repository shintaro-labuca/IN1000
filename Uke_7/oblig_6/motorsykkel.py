class Motorsykkel:
    def __init__(self, merke, regnummer, km = 0):
        self._merke = merke
        self._regnummer = regnummer
        self._km = km

    def kjor(self, km):
        self._km += km

    def hent_kilometerstand(self):
        return self._km
    
    def skriv_ut(self):
        print(self._merke, self._regnummer, self._km)
