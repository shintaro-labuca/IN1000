from film import Film

class Filmklubb:
    def __init__(self) -> None:
        self._filmer = []

    def les_filmer_fra_fil(self, filnavn):
        fil = open(filnavn, "r")
        for linje in fil:
            linje = linje.strip()
            kolonne = linje.split(";")
            film = Film(kolonne[0], int(kolonne[1]))
            self._filmer.append(film)

    def skriv_ut_alle_filmer(self):
        for film in self._filmer:
            print(f"{film.hent_tittel()} ({film.hent_år()}).")
    
    def registrer_film(self):
        print("Registrer ny film her -")
        film_tittel = input("Tittel: ")
        år = int(input("År: "))
        registrert_film = Film(film_tittel, år)

        for film in self._filmer:
            if film.__eq__(registrert_film):
                print("Denne filmen er allerede registrert.")
                return
            
        self._filmer.append(registrert_film)
        print(f"{registrert_film.hent_tittel()} ({registrert_film.hent_år()}) ble lagt til.")
            


    def finn_film_tittel(self, tittel: str):
        for film in self._filmer:
            if film.sjekk_tittel(tittel):
                return film
        return None

        # return self._filmer[tittel] if tittel in self._filmer else None
    
    def legg_til_skuespillere(self, film: Film):
        print("Legg til skuespiller her - ")
        navn = input("Navnet til skuespilleren: ")
        rolle = input("Rollen til skuespilleren: ")
        film.ny_skuespiller(navn, rolle)
    
    def finn_filmer_periode(self, år_1: int, år_2: int):
        gyldig_filmer = []
        for film in self._filmer:
            if film.sjekk_periode(år_1, år_2):
                gyldig_filmer.append(film)
        return gyldig_filmer


