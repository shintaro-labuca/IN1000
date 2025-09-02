"""

Dette programmet leser inn en inntekt og gjennom if/else setninger bestemmer en skatt
basert på personens inntekt

"""

inntekt = float(input("Hva tjener du? Du skattes basert på inntekt\n> "))


if inntekt < 10000:
    skatt = inntekt * 0.1

elif inntekt >= 10000:
    skatt_trinn1 = 10000 * 0.1
    skatt_trinn2 = (inntekt - 10000) * 0.3
    skatt = skatt_trinn1 + skatt_trinn2

print(f"Du skatter: {skatt}")
    