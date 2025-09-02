ordliste = [
    "I", "dag", "er", "jeg", "så", "lykkelig", "så", "lykkelig", "så", 
    "lykkelig", "det", "hele", "endte", "dejligt", "jeg", "synger", "og",
      "er", "glad", "Ja", "alting", "endte", "lykkeligt",
        "så", "lykkeligt", "så", "lykkeligt", "i", "dag", "er",
          "jeg", "så", "lykkelig", "som", "dagen", "den", "er", "lang"]

print(len(ordliste))

unike_ord = set(ordliste)
print(unike_ord)
print(len(unike_ord))

antall_lykkelig = ordliste.count("lykkelig")
antall_så = ordliste.count("så")
antall_dag = ordliste.count("dag")
print(f"Antall -\nLykkelig: {antall_lykkelig}\nSå: {antall_så}\nDag: {antall_dag}")

ordbok = {"lykkelig": antall_lykkelig, "så": antall_så, "dag": antall_dag}
print(ordbok)

print(list(ordbok)) #Får en liste med nøkler []
print(set(ordbok))  #Får en mengde med nøkler {}