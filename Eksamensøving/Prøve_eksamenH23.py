# Oppg 1a
# 3

# Oppg 1b
# 15

# Oppg 1c
# 2

# Oppg 1d
# 5

# Oppg 1e
# 5

# Oppg 1f
# 4

# Oppg 1g
# 3, 6, 12, 100




# Oppg 2a - d
# a = 4, b = 4, c = 6, d = 6

# Oppg 2e
# Bilde 3




# Oppg 3a
def badmington(per_vil, palle_vil, espen_vil):
    liste_vil = [per_vil, palle_vil, espen_vil]
    teller = 0
    for vil in liste_vil:
        if vil:
            teller += 1
    
    if teller == 2:
        return True
    return False

# Oppg 3b
def heie(tabellplass_ordbok): # fotball-lag : plassering
    for lag, plassering in tabellplass_ordbok.items():
        if lag == "Brann" and plassering <= 3:
            return "Brann"
    
    for lag, plassering in tabellplass_ordbok.items():
        if plassering == 1:
            return lag
        
# Oppg 3c  
def bordsetting(introverte: list[str], ekstroverte: list[str]):
    blandet_liste = []
    for i in range(len(introverte)):
        blandet_liste.append(introverte[i])
        blandet_liste.append(ekstroverte[i])
    return blandet_liste

# Oppg 3d
def lag_interessegrupper(personers_interesse: dict): # navn : interesse
    interessegrupper = {} # interesse : list[navn]
    
    for navn, interesse in personers_interesse:
        if interesse in interessegrupper:
            interessegrupper[interesse].append(navn)
        if interesse not in interessegrupper:
            interessegrupper[interesse] = [navn]
    return interessegrupper

# Oppg 3e
def gyldig_input(tekst):
    streng = input(tekst)
    while len(streng) == 0:
        print("\nUgyldig verdi!")
        streng = input("Skriv en streng")
        
    return streng


# Oppg 4
class Gruppe:
    def __init__(self, krav_til_fasiliteter: list):
        self._krav_til_fasiliteter = krav_til_fasiliteter
        self._personer = []
    
    def legg_til_personer(self, personnavn: list):
        for person in personnavn:
            self._personer.append(person)
    
    def hent_personer(self):
        return self._personer
    
    def hent_krav(self):
        return self._krav_til_fasiliteter
        
class Rom:
    def __init__(self, romnummer: int, antall_senger: int, fasiliteter: list[str]):
        self._romnummer = romnummer
        self._antall_senger = antall_senger
        self._fasiliteter = fasiliteter
        self._rom_er_opptatt = False
        self._gjester = []
    
    def reserver(self, personnavn: list):
        self._gjester = personnavn
        self._rom_er_opptatt = True
        
    
    def hent_ant_senger(self):
        return self._antall_senger
    
    def passer(self, krav_til_fasiliteter: list[str]):
        if krav_til_fasiliteter in self._fasiliteter:
            return True
        return False
        
    def __str__(self):
        return f"Romnummer: {self._romnummer}, Antall senger: {self._antall_senger}, Fasiliteter: {self._fasiliteter}"
    
class Hotell:
    def __init__(self, hotellnavn: str):
        self._hotellnavn = hotellnavn
        self._rom = {} # romnummer : Rom
        
        fil = open(hotellnavn + ".txt", "r")
        for linje in fil:
            linje.strip()
            data = linje.split("")
            romnummer = int(data[0])
            antall_senger = int(data[1])
            fasiliteter = data[2:]
            rom = Rom(romnummer, antall_senger, fasiliteter)
            self._rom[romnummer] = rom
        
    def reserver_rom(self, romnummer, personnavn: list[str]):
        self._rom[romnummer].reserver(personnavn)
    
    def finn_passende_rom(self, krav_til_fasiliteter: list):
        gyldig_rom = []
        for romnummer, rom in self._rom:
            if rom.passer(krav_til_fasiliteter):
                gyldig_rom.append(rom)
        return gyldig_rom
    
class Reservasjonssystem:
    def __init__(self, liste_hotellnavn: list[str]):
        self._hoteller = {} # hotellnavn : Hotell
        
        for hotellnavn in liste_hotellnavn:
            hotell = Hotell(hotellnavn)
            self._hoteller[hotellnavn] = hotell
        
    
    def reserver_rom_i_hotell(self, hotellnavn: str, romnummer: int, personnavn: list):
        
        self._hoteller[hotellnavn].reserver_rom(romnummer, personnavn)
    
    def _finn_alle_passende_rom(self, krav_til_fasiliteter: list[str]):
        alle_passende_rom = {} # hotellnavn : list[Rom]
        
        for hotellnavn, hotell in self._hoteller.items():
            gyldig_rom = hotell.finn_passende_rom(krav_til_fasiliteter)
            alle_passende_rom[hotellnavn] = gyldig_rom
        
        return alle_passende_rom
    
    def gruppe_reservasjon(self, gruppe: Gruppe):
        
        krav_til_fasiliteter = gruppe.hent_krav()
        passende_rom_for_gruppen = self._finn_alle_passende_rom(krav_til_fasiliteter)
        antall_personer = len(gruppe.hent_personer())
        
        if not passende_rom_for_gruppen:
            return "Ingen passende rom"
        
        hotell = ""
            
        for hotellnavn, rom_liste in passende_rom_for_gruppen.items():
            hotell = hotellnavn
            for rom in rom_liste:
                if rom.passer(krav_til_fasiliteter):
                    rom.reserver(gruppe.hent_personer())
                    

# Oppg 5a
def stigespill(terningkast: list[int], stiger: dict): # fra_rute : til_rute
    posisjon = 0
    for kast in terningkast:
        posisjon += kast
        if posisjon in stiger:
            posisjon = stiger[posisjon]
    return posisjon

# Oppg 5b                    
def hvilke_tre_kast(slutt_rute, stiger):  # fra_rute : til_rute
    liste_over_kast = []
    for kast1 in range(1,7):
        for kast2 in range(1,7):
            for kast3 in range(1,7):
                if stigespill([kast1, kast2, kast3], stiger) == slutt_rute:
                    liste_over_kast.append([kast1, kast2, kast3])
            
    return liste_over_kast
    
        
                    
                        
                    
    
    
            
        
        
        
        
        
        
    
        