

def skriv_dna(filnavn):
    fil = open(filnavn, "a")
    
    fil.write("o---o\n")
    fil.write(" o-o \n")
    fil.write("  o  \n")
    fil.write(" o-o \n")
    fil.write("o---o\n")

    fil.close()


skriv_dna("dna.txt")
skriv_dna("dna.txt")
skriv_dna("dna.txt")