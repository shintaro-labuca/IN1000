from rutenett import Rutenett

class Verden:
    def __init__(self, rader, kolonner):
        self._rader = rader
        self._kolonner = kolonner
        self._rutenett = Rutenett(self._rader, self._kolonner)
        self._generasjonsnummer = 0
        self._rutenett.fyll_med_tilfeldige_celler()
        self._rutenett.koble_celler()

    def tegn(self):
        print(f"Generasjonsnummer: {self._generasjonsnummer}\n")
        self._rutenett.tegn_rutenett()
        print(f"\nAntall levende celler: {self._rutenett.antall_levende()}")


    def oppdatering(self):
        for rad in range(self._rader):
            for kol in range(self._kolonner):

                celle = self._rutenett.hent_celle(rad, kol)
                if celle is None: return
                celle.tell_levende_naboer()
        
        for rad in range(self._rader):
            for kol in range(self._kolonner):
                celle = self._rutenett.hent_celle(rad, kol)
                if celle is None: return      
                celle.oppdater_status()

        self._generasjonsnummer += 1
