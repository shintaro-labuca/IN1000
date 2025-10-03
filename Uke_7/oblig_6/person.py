# Skriv en klasse, Person, med en konstruktør som tar imot navn og alder og oppretter
# og initialiserer instansvariabler med disse. I tillegg skal konstruktøren opprette en
# instansvariabel, hobbyer, som en tom liste . Skriv en metode, legg_til_hobby, som tar
# i mot en tekststreng og legger den til i hobbyer-listen. Skriv også en metode,
# skriv_hobbyer. Denne metoden skal skrive ut alle hobbyene etter hverandre på en
# linje. Gi deretter Person-klassen en metode, skriv_ut, som i tillegg til å skrive ut navn
# og alder kaller på metoden skriv_hobbyer.
# Lag deretter et testprogram for klassen Person, der du lar brukeren skrive inn navn
# og alder, og oppretter et Person-objekt med informasjonen du får. Deretter skal
# brukeren, ved hjelp av en løkke, få legge til så mange hobbyer de vil. Når brukeren
# ikke lenger ønsker å oppgi hobbyer, skal informasjon om brukeren skrives ut.

class Person:
    def __init__(self, navn: str, alder: int) -> None:
        self._navn = navn
        self._alder = alder
        self._hobbyer = []

    def legg_til_hobby(self, hobby: str):
        self._hobbyer.append(hobby)
    
    def skriv_hobbyer(self) -> None:
        print(*self._hobbyer)
    
    def skriv_ut(self):
        print(f"Du heter {self._navn} og er {self._alder} år gammel")
        print("Her er hobbyene dine:")
        self.skriv_hobbyer()