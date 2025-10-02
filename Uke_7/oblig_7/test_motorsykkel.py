from motorsykkel import Motorsykkel

def main():
    motorsykkel_1 = Motorsykkel("Suzuki", 6969)
    motorsykkel_2 = Motorsykkel("Harley Davidson", 67)
    motorsykkel_3 = Motorsykkel("Yamaha", 12345)

    motorsykkel_1.skriv_ut()
    motorsykkel_2.skriv_ut()
    motorsykkel_3.skriv_ut()

    motorsykkel_3.kjor(10)
    assert motorsykkel_3.hent_kilometerstand() == 10
    print(motorsykkel_3.hent_kilometerstand())  # 10

main()