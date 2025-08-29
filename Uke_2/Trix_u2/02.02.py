#02.02: int, str og float
"""
a)
Det skrives ut "<class int>"

b)
Det skrives ut class str

c)
Det skrives ut class float

d)
print(float("4" + ".8") / 2)
Det skrives ut Error, cannot concatenate str og int #feil
Det gjør om str til float også deler på 2

e)
skriver ut 35 i terminalen

f)
print("3"*3)
Blir til error, syntax #feil
printer ut "3" tre ganger ved siden av hverandre: 333

g)
print(type(3*"A"))
blir class string

h)
print(type(int("3")))
blir class integer

i)
print(3 + "3")
Det blir error cannot concatenate str og int

j)
print(float(3))
Det blir 3.0

k)
print("1.50" == "1.5")
Det blir False

l)
print(float("1.50") == float("1.5"))
Det skrives ut True

"""
print(type(3))
print(float("4" + ".8") / 2)
print("3"*3)
print(type(3*"A"))
print(type(int("3")))
print(float(3))
print("1.50" == "1.5")
print(float("1.50") == float("1.5"))

tall = 4 + (3 * 2)
tall = tall - 1
print(tall)