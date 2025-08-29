#Program om en mattequiz med if/else setninger

def main():
    print("Her en en enkel mattequiz: ")

    spm_1 = (input("Hva er 2 + 2?\nSkriv her: "))
    svar_1 = 2 + 2
    if int(spm_1) == svar_1:
        print("Helt rett!")
    else:
        print(f"Beklager, svaret var {svar_1}")


    spm_2 = (input("Hva er 9 + 10?\nSkriv her: "))
    svar_2 = 21
    if int(spm_2) == svar_2:
         print("Helt rett!")
    else:
        print(f"Beklager, svaret var {svar_2}")


    spm_3 = (input("Hva er 1349 gange 34234\nSkriv her: "))
    svar_3 = 1349 * 34234
    print(f"Hint: {svar_3}")
    if int(spm_3) == svar_3:
         print("Helt rett!")
    else:
        print(f"Beklager, svaret var {svar_3}")

main()
