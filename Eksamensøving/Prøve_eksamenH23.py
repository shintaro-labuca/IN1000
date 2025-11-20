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
        
    
