def felles(tall_lister: list[list[int]]):
    ordbok = {}
    resultat = []

    for tall_liste in tall_lister:  # Ordbok av nøstet liste
        for tall in tall_liste:
            if tall in ordbok:
                ordbok[tall] += 1
            else:
                ordbok[tall] = 1
    

    for tall, forekomst in ordbok.items():
        if forekomst > 1:
            resultat.append(tall)
    return resultat

print(felles([[1,5,1], [3,4], [2,3]]))