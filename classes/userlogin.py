import bcrypt

from classes.gclass import Gclass

class Userlogin(Gclass):
    obj = dict()
    lst = list()
    pos = 0
    sortkey = ''
    auto_number = 0
    nkey = 1
    
    att = ['_user','_password','_nome','_idade','_morada','_email','_telemovel','_pais','_usergroup']
    header = 'Users'
    des = ['User','Password','Nome','Idade','Morada','Email','Telemovel','Pais','Grupo de Utilizador']
    username = ''
    
    def __init__(self, user, password, nome, idade, morada, email, telemovel, pais, usergroup):
        super().__init__()
        
        
        
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

    @property
    def user(self):
        return self._user
    @property
    def usergroup(self):
        return self._usergroup     
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
    
    @password.setter
    def password(self, password):
       self._password = password
    @usergroup.setter
    def usergroup(self, usergroup):
        self._usergroup = usergroup
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
       
    