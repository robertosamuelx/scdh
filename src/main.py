# coleta de dados do arduino

from machine import IA

ph = 6.0
ia = IA(ph)
ia.classificador()
ia.definidor()
print(ia.status)

# envio pro mysql