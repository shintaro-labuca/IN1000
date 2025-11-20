# from random import randint
# class Plagg:
#     def __init__(self, farger: list[str]):
#         self._farger = farger # liste av strenger
#         self._antrekk = 0
    
#     def har_farge(self, farge: str):
#         return True if farge in self._farger else False
        
#     def hent_ant_antrekk(self):
#         return self._antrekk
    
#     def oppdater_ant_antrekk(self, endring: int):
#         return self._antrekk += endring
    
    
# class Kategori:
#     def __init__(self, kategorinavn: str):
#         self._kategorinavn = kategorinavn
#         self._plagger = [] # liste med Plagg
    
#     def nytt_plagg(self, farger: list[str]):
#         plagg = Plagg(farger)
#         self._plagger.append(plagg)
        
#     def finn_plagg_med_farge(self, farge: str):
#         liste = []
        
#         for plagg in self._plagger:
#             if plagg.har_farge(farge):
#                 liste.append(plagg)
  
#         return liste # Tolker som tom liste hvis ingen gyldige plagg
    
#     def trekk_tilfeldig_plagg(self, farge: str):
#         gyldige_plagg = self.finn_plagg_med_farge(farge) # liste med plagg
        
#         if not gyldige_plagg:
#             return None
            
#        return gyldig_plagg[randint(0, len(gyldige_plagg) - 1)]
       
# class Antrekk:
#     def __init__(self, anledning: str, plagg_liste: list[Plagg]):
#         self._anledninger = [] # list[str]
#         self._anledninger.append(anledning) # 
#         self._plagg_liste = plagg_liste
        
#         for plagg in self._plagg_liste:
#             plagg.oppdater_ant_antrekk(1)
    
#     def hent_plaggene(self):
#         return self._plagg_liste
    
#     def legg_til_anledning(self, anledning: str):
#         self._anledninger.append(anledning)
    
#     def passer_til(self, anledning: str):
#         return True if anledning in self._anledninger else False
    
#     def har_farge(self, farge: str):
#         for plagg in self._plagg_liste:
#             if plagg.har_farge(farge):
#                 return True
#         return False
    
    
# class Garderobe:
#     def __init__(self):
#         self._kategori_ordbok = {} # kategorinavn : Kategori
#         self._antrekk_liste = [] # list[Antrekk]
    
#     def nytt_plagg(self, kategorinavn: str, farger : list[str]):
#         kategori = Kategori(kategorinavn)
#         kategori.nytt_plagg(farger)
#         self._kategori_ordbok[kategorinavn] = kategori
    
#     def finn_antrekk_til_anledning(self, anledning):
#         liste = []
        
#         for antrekk in self._antrekk_liste:
#             if antrekk.passer_til(anledning):
#                 liste.append(antrekk)
  
#         return liste
    
#     def velg_første_antrekk(self, anledning: str, farge: str):
#         for antrekk in self._antrekk_liste:
#             if antrekk.passer_til(anledning):
#                 for plagg in antrekk.hent_plaggene():
#                     if plagg.har_farge(farge):
#                         return antrekk
                    
#     def finn_plagg_til_antrekk(self, lst_kategorinavn: list(str), farge: str):
#         liste_gyldige_plagg = []
#         for kategorinavn in lst_kategorinavn:
            
#             if kategorinavn not in self._kategori_ordbok:
#                 return None
                
#             plagg = self._kategori_ordbok[kategorinavn].trekk_tilfeldig_plagg(farge)
            
#             if plagg == None:
#                 return None
            
#             liste_gyldige_plagg.append(plagg)
        
#         if not liste_gyldige_plagg:
#             return None
        
#         return liste_gyldige_plagg
        
#     def lag_nytt_antrekk(self, list_kategorinnavn: list[str], farge: str, anledning: str):
        
#         gyldige_plagg = finn_plagg_til_antrekk(list_kategorinavn, farge)
#         if gyldige_plagg == None:
#             return False
        
#         antrekk = Antrekk(anledning, gyldige_plagg)
#         self._antrekk_liste.append(antrekk)
#         return True

# # Oppg 5a/b
# def er_blokkert(nummer: int, oppdrag: dict):
#     for verdier in oppdrag.values():
#         fullfort = verdier[0]
#         blokkerer_liste = verdier[1]
#         if fullfort and nummer in blokkerer_liste:
#             return True
#     return False

# def kan_spilles(nummer, oppdrag):
#     if nummer not in oppdrag:
#             return False
    
#     if er_blokkert(nummer, oppdrag):
#         return False
    
#     for krav in oppdrag[nummer][2]:
#         if not oppdrag[krav][0]:
#             return False
    
#     return True
    
            
    
        
        
        
            
        
    
        
    
    
        
        
        
        
    
        
        