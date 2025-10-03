from hund import Hund

def main():
    bikkje = Hund(5, 10)

    bikkje.spring()     # Metthet = 9
    assert bikkje.hent_vekt() == 10

    bikkje.spring()     # Metthet = 8
    assert bikkje.hent_vekt() == 10

    bikkje.spis(2)      # Metthet = 10
    assert bikkje.hent_vekt() == 11

    bikkje.spis(1)      # Metthet = 11
    assert bikkje.hent_vekt() == 12

main()