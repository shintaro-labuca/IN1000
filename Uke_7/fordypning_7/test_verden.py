from verden import Verden
import random

verden = Verden()

verden.opprett_dyr("sau", "pattedyr1", random.randint(1,10))
verden.opprett_dyr("sau", "pattedyr2", random.randint(1,10))
verden.opprett_dyr("sau", "pattedyr3", random.randint(1,10))
verden.opprett_dyr("sau", "pattedyr4", random.randint(1,10))
verden.opprett_dyr("sau", "pattedyr5", random.randint(1,10))
verden.opprett_dyr("sau", "pattedyr6", random.randint(1,10))

verden.opprett_dyr("ulv", "rovdyr1", random.randint(1,10))
verden.opprett_dyr("ulv", "rovdyr2", random.randint(1,10))
verden.opprett_dyr("ulv", "rovdyr3", random.randint(1,10))

print(verden.antall_sauer())
print(verden.antall_ulver())

verden.beskriv()

for i in range(10):
    verden.oppdater()

print(f"Feiteste ulv er {verden.finn_feiteste_ulv()}")