from classes.gclass import Gclass
import datetime

class Pessoa(Gclass):
    obj = dict()
    lst =list()
    pos = 0
    sortkey = ''
    autonumber = 0
    nkey = 1
    
    att = ['_codigo','_nome','_idade','_morada','_email','_telemovel','_pais']
    header = 'Pessoa'
    des = ['Codigo','Nome','Idade','Morada','Email','Telemovel','Pais']
    
    
    def __init__(self, codigo, nome, idade, morada, email, telemovel, pais):
        super().__init__()  
        self._codigo = codigo
        self._nome = nome
        self._idade = idade
        self._morada = morada
        self._email = email
        self._telemovel = telemovel
        self._pais = pais
        Pessoa.lst.append(self)
        Pessoa.obj[codigo] = self
    
    @property 
    def codigo(self):
        return self._codigo
    @property 
    def nome(self):
        return self._nome
    @property 
    def idade(self):
        return self._idade
    @property 
    def morada(self):
        return self._morada
    @property 
    def email(self):
        return self._email
    @property 
    def telemovel(self):
        return self._telemovel
    @property 
    def pais(self):
        return self._pais
    
  
    def __str__(self):
        return f'{self.nome};{self.idade};{self.morada};{self.email};{self.telemovel};{self.pais}'

P1 = Pessoa('12345','João Caires',39, 'Porto','joaocaires@hotel.pt','933222111','Portugal')
print(P1)
print(P1.telemovel)
   
