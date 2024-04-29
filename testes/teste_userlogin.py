from datafile import filename

from classes.userlogin import Userlogin


Userlogin.read(filename + 'hotel.db')  

cname = "Userlogin"
cl = eval(cname)

obj = cl.from_string("joao9;"+ Userlogin.set_password("1234")+ ";João Madeira;38;Rua das Flores 18;joaomadeira@hotelmail.com;966 772 224;Portugal;user")

print("objeto sem estar gravado ",obj)

cl.insert(getattr(obj,cl.att[0]))

obj = cl.from_string("joao10;"+ Userlogin.set_password("1234")+ ";João Madeira;38;Rua das Flores 18;joaomadeira@hotelmail.com;966 772 224;Portugal;user")
cl.insert(getattr(obj,cl.att[0]))


print("\nLista dos onjetos gravados " ,cl.lst)


# alterar
obj = cl.first()
print ("\nPrimeiro objeto gravado ",obj)
obj.name = "WORD11"
Userlogin.update(getattr(obj, cl.att[0]))

cl.read(filename + 'hotel.db')

print("\nobjectos gravados")    
for code in cl.lst:
    print(cl.obj[code])