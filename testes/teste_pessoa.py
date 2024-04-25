from datafile import filename

from classes.pessoa import Pessoa


Pessoa.read(filename + 'hotel.db')  

cname = "Pessoa"
cl = eval(cname)

obj = cl.from_string("P100;João Madeira;38;Rua das Flores 18;joaomadeira@hotelmail.com;966 772 224;Portugal")

print("objeto sem estar gravado ",obj)

cl.insert(getattr(obj,cl.att[0]))

obj = cl.from_string("P123;João Caires;39;Rua das Flores 18;joaocaires@hotelmail.com;966 732 224;Portugal")
cl.insert(getattr(obj,cl.att[0]))


print("\nLista dos onjetos gravados " ,cl.lst)


# alterar
obj = cl.first()
print ("\nPrimeiro objeto gravado ",obj)
obj.name = "WORD11"
Pessoa.update(getattr(obj, cl.att[0]))

cl.read(filename + 'hotel.db')

print("\nobjectos gravados")    
for code in cl.lst:
    print(cl.obj[code])