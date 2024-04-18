from classes.gclass import Gclass
import datetime

class Hotel(Gclass):
    obj = dict()
    lst =list()
    pos = 0
    sortkey = ''
    autonumber = 0
    nkey = 1
    
    att = ['_codigo','_nome','_localizacao','_nquartos','_contacto','_nfuncionarios']
    header = 'Hotel'
    des = ['Codigo','Nome','Localização','Número de quartos','Contacto','Número de funcionários']
    
    def __init__(self, codigo, nome, localizacao, nquartos, contacto, nfuncionarios):
        super().__init__()  
        self._codigo = codigo
        self._nome = nome
        self._nquartos = nquartos
        self._localizacao = localizacao
        self._contacto = contacto
        self._nfuncionarios = nfuncionarios
        Hotel.lst.append(self)
        Hotel.obj[codigo] = self
        
    @property 
    def codigo(self):
        return self._codigo
    @property 
    def nome(self):
        return self._nome
    @property 
    def nquartos(self):
        return self._nquartos
    @property 
    def localizacao(self):
        return self._localizacao
    @property 
    def contacto(self):
        return self._contacto 
    @property 
    def nfuncionarios(self):
        return self._nfuncionarios
    
H1 = Hotel('H1','Sana','Porto',300,'969333111',60)
print (H1.localizacao)
print (H1.contacto)


