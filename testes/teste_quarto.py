from datafile import filename

from classes.quarto import Quarto


Quarto.read(filename + 'hotel.db')

cname = "Quarto"
cl = eval(cname)

obj = cl.from_string("1000;H1;30;False") 

print("objeto sem estar gravado ",obj)

cl.insert(getattr(obj,cl.att[0]))

obj = cl.from_string("1000;H1;30;False")
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