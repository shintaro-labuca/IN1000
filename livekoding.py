class Student:
    def __init__(self, navn):
        self._poeng = 0
        self._navn = navn

    def hent_poeng(self):
        return self._poeng
    
    def registrer_poeng(self, antall):
        self._poeng += antall

    def hent_navn(self):
        return self._navn
    
student1 = Student("Shintaro")

print(student1.hent_navn())
student1.registrer_poeng(20)
print(student1.hent_poeng())