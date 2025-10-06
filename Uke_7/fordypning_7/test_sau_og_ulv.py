from ulv import Ulv
from sau import Sau
import random

dyr = Sau("sau_1", random.randint(0, 10))
rovdyr = Ulv("ulv_1", random.randint(0, 10))
assert dyr.lever() # True
assert rovdyr.hent_vekt() == 20


rovdyr.spis_sau(dyr)
assert dyr.lever() == False
assert rovdyr.hent_vekt() == 25