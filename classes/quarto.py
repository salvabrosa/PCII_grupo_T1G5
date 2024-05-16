from classes.gclass import Gclass
from classes.hotel import Hotel
import datetime

class Quarto(Gclass):
    obj = dict()
    lst =list()
    pos = 0
    sortkey = ''
    auto_number = 0
    nkey = 1
    
    att = ['_codigo','_cod_hotel','_preco_noite','_estado_reserva']
    header = 'Quarto'
    des = ['Codigo do quarto','Codigo do hotel','Preço por noite','Estado da reserva']
    
    def __init__(self, codigo, cod_hotel, preco_noite, estado_reserva):
        super().__init__()
        
        if cod_hotel in Hotel.lst:
            self._codigo = codigo
            self._cod_hotel = cod_hotel
            self._preco_noite = preco_noite
            self._estado_reserva=estado_reserva
        
            Quarto.obj[codigo] = self
            Quarto.lst.append(codigo)
        else:
            print('Hotel ', cod_hotel, ' not found')
            
    @property 
    def codigo(self):
        return self._codigo
    @property 
    def cod_hotel(self):
        return self._cod_hotel
    @property 
    def preco_noite(self):
        return self._preco_noite
    @property 
    def estado_reserva(self):
        return self._estado_reserva
    
    @codigo.setter
    def codigo(self, codigo):
        self._codigo = codigo
    @cod_hotel.setter
    def cod_hotel(self, cod_hotel):
        if cod_hotel in Hotel.lst:
            self._cod_hotel = cod_hotel
        else:
            print('Hotel ', cod_hotel, ' not found')
    @preco_noite.setter 
    def preco_noite(self, preco_noite):
        self._preco_noite = preco_noite
    @estado_reserva.setter 
    def estado_reserva(self, estado_reserva):
        self._estado_reserva = estado_reserva
        
class TiposQuarto(Gclass):
    obj = dict()
    lst = list()
    pos = 0
    sortkey = ''
    auto_number = 0
    nkey = 1
    
    att = ['_codigo','_name']
    header = 'Tipos'
    des = ['Codigo','']
    def __init__(self, codigo,name):
        super().__init__()

        self._codigo = codigo
        self._name = name

        TiposQuarto.obj[codigo] = self
        TiposQuarto.lst.append(codigo)


    @property
    def codigo(self):
        return self._codigo
    @property
    def name(self):
        return self._name    
    @name.setter
    def name(self, name):
        self._name = name