#Program om en mattequiz med while loop, den avslutter quizen så fort svaret er feil

def main():
    print("Her kommer en mattetest.\nNå kommer det en rekke spørsmål, om du svarer riktig så går vi videre.")
    print("Her er første spørsmål: ")

    nøkkel = True

    while nøkkel:
        spm_1 = int(input("Hva er 1 + 1?\nSkriv her: "))
        svar_1 = 1 + 1

        if spm_1 == svar_1:
            print("Supert! Vi går videre.")
        else:
            print("Beklager, det var feil! Spillet er over.")
            break
    
        spm_2 = int(input("Hva er 5 * 4?\nSkriv her: "))
        svar_2 = 5 * 4
        if spm_2 == svar_2:
            print("Supert! Vi går videre.")
        else:
            print("Beklager, det var feil! Spillet er over.")
            break

        spm_3 = int(input("Hva er 10 / 2?\nSkriv her:"))
        svar_3 = 10 / 2
        if spm_3 == svar_3:
            print("Gratulerer, du vant!")
        else:
            print("Beklager, det var feil! Spillet er over.")
            break
        break



main()
