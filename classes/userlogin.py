"""
@author: António Brito / Carlos Bragança
(2024) #objective: class Person
"""""
# Class User - generic version
# import sys
import bcrypt
# Import the generic class
from classes.gclass import Gclass

class Userlogin(Gclass):
    obj = dict()
    lst = list()
    pos = 0
    sortkey = ''
    auto_number = 0
    nkey = 1
    
    att = ['_user','_password','_nome','_idade','_morada','_email','_telemovel','_pais']
    header = 'Users'
    des = ['User','Password','Nome','Idade','Morada','Email','Telemovel','Pais']
    username = ''
    
    # Constructor: Called when an object is instantiated
    def __init__(self, user, password, nome, idade, morada, email, telemovel, pais, usergroup='user'):
        super().__init__()
        
        if user not in Userlogin.lst:
            
            self._user = user
            self._usergroup = usergroup
            self._password = password
        
            self._nome = nome
            self._idade = idade
            self._morada = morada
            self._email = email
            self._telemovel = telemovel
            self._pais = pais
        
            Userlogin.obj[user] = self
            Userlogin.lst.append(user)

    # code property getter method
    @property
    def user(self):
        return self._user
    # name property getter method
    @property
    def usergroup(self):
        return self._usergroup
    @usergroup.setter
    def usergroup(self, usergroup):
        self._usergroup = usergroup
        
    @property
    def password(self):
        return ""
    
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
    
    @password.setter
    def password(self, password):
        self._password = password
    
    @classmethod
    def chk_password(self, user, password):
        Userlogin.username = ''
        if user in Userlogin.obj:
            obj = Userlogin.obj[user]
            valid = bcrypt.checkpw(password.encode(), obj._password.encode())
            if valid:
                Userlogin.username = user
                message = "Valid"
            else:
                message = 'Wrong password'
        else:
            message = 'No existent user'
        return message
    
    @classmethod
    def set_password(self, password):
        passencrypted = bcrypt.hashpw(password.encode(), bcrypt.gensalt())
        return passencrypted.decode()


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