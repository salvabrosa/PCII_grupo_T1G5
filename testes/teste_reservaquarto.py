from datafile import filename

from classes.hotel import Hotel
from classes.quarto import Quarto
from classes.reservaquarto import ReservaQuarto
from classes.tiposquarto import TiposQuarto

Hotel.read(filename + 'hotel.db')
TiposQuarto.read(filename + 'hotel.db')
Quarto.read(filename + 'hotel.db')
ReservaQuarto.read(filename + 'hotel.db')

cname = "ReservaQuarto"
cl = eval(cname)

obj = cl.from_string('10000;2-01-2024;2-01-2024;Ativa;A100;12345')

print("objeto sem estar gravado ",obj)

cl.insert(getattr(obj,cl.att[0]))

obj = cl.from_string('20000;2-01-2024;2-01-2024;Ativa;A100;12345')
cl.insert(getattr(obj,cl.att[0]))


print("\nLista dos onjetos gravados " ,cl.lst)


# alterar
obj = cl.first()
print ("\nPrimeiro objeto gravado ",obj)
obj.name = "WORD11"
ReservaQuarto.update(getattr(obj, cl.att[0]))

cl.read(filename + 'hotel.db')

print("\nobjectos gravados")    
for code in cl.lst:
    print(cl.obj[code])
