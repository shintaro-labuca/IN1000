def fil_na_filter(inputfilnavn, outputfilnavn):
    inputfil = open(inputfilnavn)
    outputfil = open(outputfilnavn, "w")

    for linje in inputfil:
        if "NA" not in linje:
            outputfil.write(linje)


    inputfil.close()
    outputfil.close()
    

fil_na_filter("input_med_na.csv", "output_uten_na.csv")
