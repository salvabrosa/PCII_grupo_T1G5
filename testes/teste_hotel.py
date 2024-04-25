from datafile import filename

from classes.hotel import Hotel


Hotel.read(filename + 'hotel.db')  

cname = "Hotel"
cl = eval(cname)

obj = cl.from_string("H9;Hotel1234;Porto;300;969 333 222;83")

print("objeto sem estar gravado ",obj)

cl.insert(getattr(obj,cl.att[0]))

obj = cl.from_string("H000;Sana;Porto;300;969 333 222;83")
cl.insert(getattr(obj,cl.att[0]))


print("\nLista dos onjetos gravados " ,cl.lst)


# alterar
obj = cl.first()
print ("\nPrimeiro objeto gravado ",obj)
obj.name = "WORD11"
Hotel.update(getattr(obj, cl.att[0]))

cl.read(filename + 'hotel.db')

print("\nobjectos gravados")    
for code in cl.lst:
    print(cl.obj[code])