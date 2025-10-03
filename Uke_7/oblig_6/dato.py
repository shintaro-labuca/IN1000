class Dato:
    def __init__(self, ny_dag: int, ny_måned: int, nytt_år: int):
        self._dag = ny_dag
        self._måned = ny_måned
        self._år = nytt_år
    
    def hent_år(self):
        return self._år
    
    def hent_dato(self):
        return f"{self._dag}.{self._måned}.{self._år}"
    
    def samme_dag(self, dag_nr) -> bool:
        return self._dag == dag_nr # Returnerer True ved likhet, ellers False
    
    def dager_i_måneden(self, måned): # Hjelpefunksjon for å finne riktig antall dager i en måned
        if måned in [4, 6, 9, 11]: # Måneder med 30 dager
            return 30
        elif måned == 2:
            return 28
        else:
            return 31
    
    def ny_dag(self): # Oppdaterer datoen til neste dag, men tar ikke hensyn til skuddår
        self._dag += 1
        if self._dag > self.dager_i_måneden(self._måned):
            self._dag = 1
            self._måned += 1
                
        if self._måned > 12:
            self._måned = 1
            self._år += 1
    
    def kommer_før(self, annen_dato):
        annen_dato = annen_dato.split(".")
        if self._år < int(annen_dato[2]): # Sammenligner år
            return True
        elif self._år == int(annen_dato[2]) and self._måned < int(annen_dato[1]): # Sammenligner måned
            return True
        elif self._år == int(annen_dato[2]) and self._måned == int(annen_dato[1]) and self._dag < int(annen_dato[0]):  # Sammenligner dag
            return True
        else: # Opprinnelig dato kommer ikke før annen_dato
            return False