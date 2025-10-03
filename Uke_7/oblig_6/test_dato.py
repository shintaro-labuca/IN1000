from dato import Dato

def main():
    bruker_dato = input("Skriv en dato i dette formatet: xx.xx.xxxx\n> ")
    bruker_dato = bruker_dato.split(".")
    dato_1 = Dato(int(bruker_dato[0]), int(bruker_dato[1]), int(bruker_dato[2]))

    print(f"Dette er datoens år: {dato_1.hent_år()}")
    if dato_1.samme_dag(15):
        print("Lønningsdag!")
    elif dato_1.samme_dag(1):
        print("Ny måned, nye muligheter") 

    print("Datoen")
    print(dato_1.hent_dato())

    print("Ny dato")
    dato_1.ny_dag()
    print(dato_1.hent_dato())

    bruker_annen_dato = input("Skriv inn en ny dato i samme formatet: xx.xx.xxxx\n> ")
    print(f"Kommer den opprinnelige datoen før den nye?\n:{dato_1.kommer_før(bruker_annen_dato)}")


main()