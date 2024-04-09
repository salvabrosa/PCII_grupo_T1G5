from classes.gclass import Gclass
import datetime

class Pessoa(Gclass):
    obj = dict()
    lst =list()
    pos = 0
    sortkey = ''
    autonumber = 0
    nkey = 1
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

    
   
