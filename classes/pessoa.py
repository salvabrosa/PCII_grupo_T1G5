from classes.gclass import Gclass
import datetime

class Pessoa(Gclass):
    obj = dict()
    lst =list()
    # Inicializar a classe com os atributos adicionais
    def __init__(self, codigo, nome, idade, morada, email, telemovel, pais):
        super().__init__()  # Chama o construtor da classe pai
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
    
    # Atualizar a representação do objeto como string
    def __str__(self):
        return f'{self.nome};{self.idade};{self.morada};{self.email};{self.telemovel};{self.pais}'

    # Atualizar o método from_string para aceitar os novos atributos
    @classmethod
    def from_string(cls, str_data):
        nome, idade, morada, email, telemovel, pais = str_data.split(";")
        return cls(nome, idade, morada, email, telemovel, pais)
