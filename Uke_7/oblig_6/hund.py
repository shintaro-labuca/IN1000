class Hund:
    def __init__(self, alder, vekt, metthet = 10):
        self._alder = alder
        self._vekt = vekt
        self._metthet = metthet

    def hent_alder(self):
        return self._alder
    
    def hent_vekt(self):
        return self._vekt
    
    def spring(self):
        self._metthet -= 1
        if self._metthet < 5:
            self._vekt -= 1
    
    def spis(self, heltall):
            self._metthet += heltall
            if self._metthet > 7:
                self._vekt += 1
    