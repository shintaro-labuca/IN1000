# 1.
def maks_temp_mnd(filnavn):
    fil = open(filnavn, "r")
    ordbok = {}
    for linje in fil:
        linje = linje.strip()
        kolonne = linje.split(",")
        måned = kolonne[0]
        temperatur = float(kolonne[1])
        ordbok[måned] = temperatur # Hver iterasjon lagrer en måned som nøkkel og temperatur som verdi
    fil.close()
    return ordbok
maks_temp_ordbok = maks_temp_mnd("max_temperatures_per_month.csv")

# 2-3.
def maks_daglig_temp(temp_ordbok, filnavn):
    fil = open(filnavn, "r")
    for linje in fil:
        linje = linje.strip()
        kolonner = linje.split(",")
        måned = kolonner[0]
        temperatur = float(kolonner[2])
        if temp_ordbok[måned] < temperatur: # Hvis temperatur er høyere enn temp i ordboken
            temp_ordbok[måned] = temperatur # så oppdateres det
    fil.close()
    return temp_ordbok
ny_temp = (maks_daglig_temp(maks_temp_ordbok, "max_daily_temperature_2018.csv"))

# 4-5.
def ny_maks_temp(temp, filnavn):
    fil = open(filnavn, "w")
    for måned, temperatur in temp.items(): # For hver nøkkel:verdi par så skrives det inn
        fil.write(måned)
        fil.write(",")
        fil.write(str(temperatur))
        fil.write("\n")
    fil.close()
ny_maks_temp(ny_temp, "ny_maks_temp_per_month.csv")

# 6.
# def varmebølge(filnavn):
#     fil = open(filnavn, "r")
  
#     måned = []
#     dag = []
#     temperatur = []
#     for linje in fil:
#         linje = linje.strip()
#         kolonner = linje.split(",")
#         måned.append(kolonner[0])
#         dag.append(int(kolonner[1]))
#         temperatur.append(float(kolonner[2]))

#     dager = 5
#     limit_temperatur = 25.0



#     fil.close()
# UNFINISHED
