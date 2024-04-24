from classes.gclass import Gclass
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
        self._codigo = codigo
        self._cod_hotel = cod_hotel
        self._preco_noite = preco_noite
        self._estado_reserva=estado_reserva
        
        Quarto.obj[codigo] = self
        Quarto.lst.append(codigo)
        
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
    
# Q100 = Quarto('A100','H1',50,Ativo)
# print(Q100)