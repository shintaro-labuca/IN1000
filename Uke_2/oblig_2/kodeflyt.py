def print_prosa():                                                          # 1
    print("Melding til alle gaardeiere: ")                                  # 4, 10
    print("Antall dyr paa gaarden: ")                                       # 5, 11

antall_dyr = 4                                                              # 2
print_prosa()                                                               # 3
print(antall_dyr)                                                           # 6
antall_nye_dyr = int(input("Hvor mange nye dyr kommer til gaarden: "))      # "Bruker taster 8" 7
antall_dyr = antall_dyr + antall_nye_dyr                                    # 8
print_prosa()                                                               # 9

print(antall_dyr)                                                           # 12

if antall_dyr > 12:                                                         # 13
    print("Det er mer enn ett dusin dyr paa gaarden!")                      # 
elif antall_dyr == 12:                                                      # 14
    print("Det er ett dusin dyr paa gaarden!")                              # 15
else:                                                                       # 
    print("Det er mindre enn ett dusin dyr paa gaarden!")                   #