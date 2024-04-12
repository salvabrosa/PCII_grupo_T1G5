from classes.gclass import Gclass
import datetime

class Hotel(Gclass):
    obj = dict()
    lst =list()
    pos = 0
    sortkey = ''
    autonumber = 0
    nkey = 1
    def __init__(self, codigo, localizacao, nquartos, contacto, nfuncionarios):
        super().__init__()  
        self._codigo = codigo
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
    
