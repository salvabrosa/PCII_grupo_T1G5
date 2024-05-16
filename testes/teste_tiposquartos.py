from datafile import filename

from classes.tiposquarto import TiposQuarto


TiposQuarto.read(filename + 'hotel.db')

cname = "TiposQuarto"
cl = eval(cname)

obj = cl.from_string("None;Nenhum") 

print("objeto sem estar gravado ",obj)

cl.insert(getattr(obj,cl.att[0]))

obj = cl.from_string("1;Quarto de solteiro") 
cl.insert(getattr(obj,cl.att[0]))


print("\nLista dos onjetos gravados " ,cl.lst)


# alterar
obj = cl.first()
print ("\nPrimeiro objeto gravado ",obj)
obj.name = "WORD11"
TiposQuarto.update(getattr(obj, cl.att[0]))

cl.read(filename + 'hotel.db')

print("\nobjectos gravados")    
for code in cl.lst:
    print(cl.obj[code])