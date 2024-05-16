from datafile import filename

from classes.hotel import Hotel
from classes.quarto import Quarto
from classes.tiposquarto import TiposQuarto

TiposQuarto.read(filename + 'hotel.db')
Hotel.read(filename + 'hotel.db')
Quarto.read(filename + 'hotel.db')

cname = "Quarto"
cl = eval(cname)

obj = cl.from_string("5;H1;1;30;False") 

print("objeto sem estar gravado ",obj)

cl.insert(getattr(obj,cl.att[0]))

obj = cl.from_string("6;H1;1;30;False")
cl.insert(getattr(obj,cl.att[0]))


print("\nLista dos onjetos gravados " ,cl.lst)


# alterar
obj = cl.first()
print ("\nPrimeiro objeto gravado ",obj)
obj.name = "WORD11"
Quarto.update(getattr(obj, cl.att[0]))

cl.read(filename + 'hotel.db')

print("\nobjectos gravados")    
for code in cl.lst:
    print(cl.obj[code])