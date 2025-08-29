#Dette programmet ber bruker skrive inn tall og deretter skriver ut informasjon om det største tallet

print("Her skal du skrive tre heltall og programmet skal skrive ut den største verdien")
tall_1 = int(input("Første tall: "))
tall_2 = int(input("Andre tall: "))
tall_3 = int(input("Tredje tall: "))

størst = 0

if (tall_1 >= tall_2) and tall_1 >= tall_3:
    størst = tall_1
    print(f"Største tall er {størst}")
elif tall_2 >= tall_1 and tall_2 >= tall_3:
    størst = tall_2
    print(f"Største tall er {størst}")
else:
    størst = tall_3
    print(f"Største tall er {størst}")

teller = 0

if tall_1 == størst:
    teller += 1
if tall_2 == størst:
    teller += 1
if tall_3 == størst:
    teller += 1

if teller == 1: 
    print(f"{teller} verdier er lik den største verdien")
else:
    print(f"Tallet som repeterer mest er {størst} som kommer {teller} ganger.")


