from sau import Sau
import random


dyr = Sau("Lillelam", random.randint(0, 10))
assert dyr.lever()

dyr.blir_spist()
assert dyr.lever() == False

