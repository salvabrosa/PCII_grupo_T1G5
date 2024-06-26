
from datafile import filename

from classes.hotel import Hotel
from classes.quarto import Quarto
from classes.reservaquarto import ReservaQuarto
from classes.fatura import Fatura
from classes.userlogin import Userlogin
from classes.faturareserva import FaturaReserva

Hotel.read(filename + 'hotel.db')
Quarto.read(filename + 'hotel.db')
ReservaQuarto.read(filename + 'hotel.db')
FaturaReserva.read(filename + 'hotel.db')
Fatura.read(filename + 'hotel.db')
Userlogin.read(filename + 'hotel.db')

cname = "FaturaReserva"
cl = eval(cname)

obj = cl.from_string('Fat9;rq1;300;2')

print("objeto sem estar gravado ",obj)

cl.insert(getattr(obj,cl.att[0]))

obj = cl.from_string('Fat9;rq1;300;2')
cl.insert(getattr(obj,cl.att[0]))


print("\nLista dos onjetos gravados " ,cl.lst)


# alterar
obj = cl.first()
print ("\nPrimeiro objeto gravado ",obj)
obj.name = "WORD11"
FaturaReserva.update(getattr(obj, cl.att[0]))

cl.read(filename + 'hotel.db')

print("\nobjectos gravados")    
for code in cl.lst:
    print(cl.obj[code])
