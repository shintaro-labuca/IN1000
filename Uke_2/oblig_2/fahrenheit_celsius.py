"""


"""

def main():
    bruker_fahrenheit = int(input("Skriv en temperatur gitt i Fahrenheit:\n> "))
    bruker_fahrenheit_til_celsius = (bruker_fahrenheit - 32) * 5/9
    print(f"Temperaturen du skrev i Fahrenheit gitt i Celsius er {bruker_fahrenheit_til_celsius}")

    temperatur = int(input("Skriv et tall:\n> "))
    C_eller_F = input("Er dette i Fahrenheit eller Celsius?\nSkriv F for Fahrenheit og C for Celsius\n> ")
    celsius_til_fahrenheit = (temperatur / 5) * 9 + 32

    if C_eller_F == "F":
        fahrenheit_til_celsius = (temperatur - 32) * 5/9
        print(f"Temperaturen i Fahrenheit konvertert til Celsius er {fahrenheit_til_celsius}")
    elif C_eller_F == "C":
        celsius_til_fahrenheit = (temperatur / 5) * 9 + 32
        print(f"Temperaturen i Celsius konvertert til Fahrenheit er {celsius_til_fahrenheit}")
    else:
        print("Skjønte ikke.")

main()