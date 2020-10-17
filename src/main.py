from entity import Entity
from machine import IA

# coleta de dados do arduino

ph = 6.0
ia = IA(ph)
ia.classificador()
ia.definidor()
print(ia.status)

entity = Entity()
entity.ph = ph
entity.status = ia.status
entity.save()