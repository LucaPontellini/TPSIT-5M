from auto import Auto
from moto import Moto

a = Auto("Fiat", "Panda", "Benzina", 5)
m = Moto("Yamaha", "MT-07", "Benzina", 689)

print(a.descrizione())
print()
print(m.descrizione())