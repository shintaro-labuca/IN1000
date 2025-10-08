class Navn:
    def __init__(self, fornavn, mellomnavn, etternavn) -> None:
        self._fornavn = fornavn
        self._mellomnavn = mellomnavn
        self._etternavn = etternavn

    def sorterbar(self):
        return f"{self._etternavn}, {self._fornavn} {self._mellomnavn}"
    
    def naturlig(self):
        return f"{self._fornavn} {self._mellomnavn} {self._etternavn}"
    

person = Navn("Shintaro", "Emmanuel", "Labuca")

print(person.sorterbar())
print(person.naturlig())