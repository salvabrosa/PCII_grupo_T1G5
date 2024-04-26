from classes.gclass import Gclass
import datetime

class Pessoa(Gclass):
    obj = dict()
    lst =list()
    pos = 0
    sortkey = ''
    auto_number = 0
    nkey = 1
    
    att = ['_codigo','_nome','_idade','_morada','_email','_telemovel','_pais','_username','_password']
    header = 'Pessoa'
    des = ['Codigo','Nome','Idade','Morada','Email','Telemovel','Pais','Username','Password']
    
    
    def __init__(self, codigo, nome, idade, morada, email, telemovel, pais,username,password, usergroup='user'):
        super().__init__()  
        self._codigo = codigo
        self._nome = nome
        self._idade = idade
        self._morada = morada
        self._email = email
        self._telemovel = telemovel
        self._pais = pais

        self._username=username
        self._password=password
        self._usergroup = usergroup
        
        Pessoa.obj[codigo] = self
        Pessoa.lst.append(codigo)
    
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
    @property 
    def username(self):
        return self._username
    @property 
    def password(self):
        return self._password
    @property 
    def usergroup(self):
        return self._usergroup
    
    
    @codigo.setter 
    def codigo(self, codigo):
        self._codigo = codigo 
    @nome.setter 
    def nome(self, nome):
        self._nome = nome 
    @idade.setter 
    def idade(self, idade):
        self._idade = idade 
    @morada.setter 
    def morada(self, morada):
        self._morada = morada 
    @email.setter 
    def email(self, email):
        self._email = email 
    @telemovel.setter 
    def telemovel(self, telemovel):
        self._telemovel = telemovel 
    @pais.setter 
    def pais(self, pais):
        self._pais = pais
    @username.setter 
    def username(self, username):
        pass
    @password.setter 
    def password(self, password):
        self._password = password
    @usergroup.setter 
    def usergroup(self,usergroup):
        pass