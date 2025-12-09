"""
1a.
3

1b.
6

1d.
AL

1f.
abcd

1g.
ba

2a.
2

2g.
tall = parameter, c = lokal variabel, e = global variabel, self._a = instansvariabel

2h.
int(input("Alder:")) = uttrykk som evaluerer til int
print(navn) = uttrykk eval til str
for i in range(4): = uttrykk til int
"713 + 56" = uttrykk til str

"""

# Oppg 3a
def karantene(vaksinert: bool, farge: str):
    if vaksinert:
        return 0
    
    return 10 if farge in ["roed", "oransje"] else 3

# Oppg 3b
def tell_grad(fag, bsc, msc):
    grad_liste = [bsc, msc]
    teller = 0
    for grad in grad_liste:
        if fag == grad:
            teller += 1
    return teller

# Oppg 3c
def fjern_vokaler(setning: str, vokal_liste: list[str]):
    ny_setning = ""
    for bokstav in setning:
        if bokstav not in vokal_liste:
            ny_setning += bokstav
    
    return ny_setning

# Oppg 3d
def summer_rabatt(vareliste: list[str], forpris: dict, nypris: dict): # varenavn : forpris, varenavn : nypris
    
    rabatt_total = 0
    for varenavn in vareliste:
       rabatt = forpris[varenavn] - nypris[varenavn]
       rabatt_total += rabatt
       
    return rabatt_total
    







class Onske:
    def __init__(self, beskrivelse: str, antall: int, minimumspris: int):
        self._beskrivelse = beskrivelse
        self._antall = antall
        self._minimumspris = minimumspris
    
    def passer(self, maksimumspris: int):
        if self._antall == 0 or self._minimumspris > maksimumspris:
            return False
        return True
    
    def valgt(self):
        self._antall -= 1
        return self._beskrivelse
    
    def __str__(self):
        return f"Beskrivelse: {self._beskrivelse}, minimumspris: {self._minimumspris}"
    
class Onskeliste:
    def __init__(self):
        self._onskeliste = [] # list[Onske]
    
    def nytt_onske(self, beskrivelse: str, antall: int, minimumspris: int):
        onske = Onske(beskrivelse, antall, minimumspris)
        self._onskeliste.append(onske)
    
    def hent_onsker(self, maksimumspris: int):
        str_onske_liste = []
        for onske in self._onskeliste:
            if onske.passer(maksimumspris):
                str_onske_liste.append(str(onske))
            else:
                str_onske_liste.append("Ikke valgbart onske")
        return str_onske_liste
    
    def onske_oppfylles(self, onske_valg: int):
        return self._onskeliste[onske_valg].valgt()
    

class Gave:
    def __init__(self, beskrivelse: str, giver: str):
        self._beskrivelse = beskrivelse
        self._giver = giver
    
    def hent_info(self):
        return f"Beskrivelse: {self._beskrivelse}, Giver: {self._giver}"
    
class Juleferiekalender:
    def __init__(self, antall_dager: int):
        self._kalender_ordbok = {} # dagnummer : None
        self._antall_dager = antall_dager
        
        dagnummer = 25
        for dager in range(self._antall_dager):
            self._kalender_ordbok[dagnummer] = None
            if dagnummer == 31:
                dagnummer = 1
            else:
                dagnummer += 1
        
    def ny_gave(self, beskrivelse: str, giver: str, dagnummer: int):
        gave = Gave(beskrivelse, giver)
        self._kalender_ordbok[dagnummer] = gave
    
    def hent_dagens_gave(self, dagnummer: int):
        if self._kalender_ordbok[dagnummer] is not None:
            if 24 < dagnummer <= 31:
                måned = "desember"
            else:
                måned = "januar"
            return f"Åpnes: {dagnummer}.{måned}. Info: {self._kalender_ordbok[dagnummer].hent_info()}"
        else:
            return "Ingen gaver på denne dagen."
        
    def hent_ant_dager(self):
        return self._antall_dager
    
class Julegaverfikser:
    def __init__(self, antall_dager: int):
        self._juleferiekalender = Juleferiekalender(antall_dager)
        self._onskeliste = Onskeliste()
        self._neste_dag = 25
    
    def les_onsker_fra_fil(self, filnavn: str):
        fil = open(filnavn + ".txt")
        for linje in fil:
            linje = linje.strip()
            onsker_liste = linje.split(";")
            beskrivelse = onsker_liste[0]
            antall = int(onsker_liste[1])
            minimumspris = int(onsker_liste[2])
            self._onskeliste.nytt_onske(beskrivelse, antall, minimumspris)
        fil.close()
        
    def velg_gave(self, maksimumspris: int):
        passende_onske_liste = self._onskeliste.hent_onsker(maksimumspris)
        print("Passende onsker:")
        nummerert = 0
        for onske in passende_onske_liste:
            print(f"{nummerert}: {onske}")
            nummerert += 1
        bruker_input = int(input("Velg et ønske ved å oppgi nummer: "))
        beskrivelse = self._onskeliste.onske_oppfylles(bruker_input)
        print("Registrert i ønskelisten.")
        
        dagnummer = int(input("Angi dagnummer som onsket skal legges i juleferiekalenderen."))
        giver = input("Hvem er giver: ")
        self._juleferiekalender.ny_gave(beskrivelse, giver, dagnummer)
    
    def ny_dag(self):
        return self._juleferiekalender.hent_dagens_gave(self._neste_dag)

    
# Oppg 5
def sjekk_reise(reise: list[list[str]]):
    
    for reiserute in range(len(reise) - 1):
        slutt = reise[reiserute][1]
        neste_start = reise[reiserute + 1][0]
        
        if slutt != neste_start:
            return False
    return True