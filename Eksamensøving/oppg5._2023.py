# 5a)
# 3P PRO: oppslag, sjekker alle som kan stenge, resultat
# 2P PRE: Helt korrekt kode
def er_blokkert(nummer, oppdrag):
    # det er irrelevant om oppdraget er utført
    # (det gir poeng uansett hva man har antatt her)
    blokkerer = oppdrag[nummer][1]
    for stenger in blokkerer:
        if oppdrag[stenger][0]:
            return True
    return False

# IKKE FORVENTET I BESVARELSER
# Test av 5a)
# Eksempel fra oppgaven
oppdrag = { 16: [False, []],
            24: [False, []],
            25: [False, []],
            33: [False, [42]],
            40: [False, [42]],
            41: [False, [42]],
            42: [False, [41]]}
assert not er_blokkert(40, oppdrag)
assert not er_blokkert(16, oppdrag)
oppdrag[42][0] = True
assert er_blokkert(40, oppdrag)
assert not er_blokkert(16, oppdrag)
print("Test oppg 5a) ok")

###########################################################################
# 5b)
# 3P PRO: oppslag, kaller er_blokkert, sjekker alle som skal åpne, resultat
# 1P PRE: Helt korrekt kode
def kan_spilles (nummer,oppdrag): 
    for oppdragsnummer in oppdrag:
        if nummer not in oppdrag:
            return False
    if er_blokkert(nummer,oppdrag):
        return False 
    for oppdragsnummer in oppdrag[nummer][2]:
        if not oppdrag[oppdragsnummer][0]:
            return False 
    return True 

# IKKE FORVENTET I BESVARELSER
# Test av 5b)
# Eksempel fra oppgaven
oppdrag = { 16: [False, [], []],
            24: [False, [], [16]],
            25: [False, [], [16]],
            33: [False, [42], [25]],
            40: [False, [42], [24, 33]],
            41: [False, [42], [40]],
            42: [False, [41], [24]]}
assert not kan_spilles(10, oppdrag)         # Oppdraget finnes ikke
assert kan_spilles(16, oppdrag)             # Ingen blokkerer, ingen må åpne
oppdrag[42][0] = True                       # blokkerer 40 og 41
assert not kan_spilles(40, oppdrag)         # Er blokkert
assert not kan_spilles(24, oppdrag)         # Ikke blokkert, men 16 ikke fullført
oppdrag[16][0] = True                       # Fullført oppdrag 16
assert kan_spilles(24, oppdrag)             # Ingen blokkerer, 16 er fullført
print("Test oppg 5b) ok")
