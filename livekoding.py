def adskilt(tall_lister: list[list[int]]):
    for første_index in range(len(tall_lister)):
        for andre_index in range(len(tall_lister)):
            
            if tall_lister[første_index] == tall_lister[andre_index]:
                continue

            liste1 = tall_lister[første_index]
            liste2 = tall_lister[andre_index]

            if min(liste1) > max(liste2):
                return True
            elif min(liste2) > max(liste1):
                return True
    return False
    
print(adskilt([[1, 10], [6,8], [2,3,7]]))
print(adskilt([[1, 10], [6,8], [2,3]]))