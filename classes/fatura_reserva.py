from classes.gclass import Gclass
import datetime

class Fatura_Reserva(Gclass):
    obj = dict()
    lst =list()
    pos = 0
    sortkey = ''
    autonumber = 0
    nkey = 2
    
    att = ['_cod_fatura','_cod_reserva','_preco','_nreservas']
    header = 'Quarto'
    des = ['Codigo da Fatura','Codigo da Reserva','Preço','Nº de reservas']
    
    def __init__(self, cod_fatura, cod_reserva, preco, nreservas):
        super().__init__()  
        self._cod_fatura = cod_fatura
        self._cod_reserva = cod_reserva
        self._preco = preco
        self._nreservas = nreservas
        
        Fatura_Reserva.lst.append(self)
        Fatura_Reserva.obj[cod_reserva] = self
        
    @property 
    def cod_fatura(self):
        return self._cod_fatura
    @property 
    def cod_reserva(self):
        return self._cod_reserva
    @property 
    def preco(self):
        return self._preco
    @property 
    def nreservas(self):
        return self._nreservas
    
# fatRes=Fatura_Reserva('fat1', 'rq1', '1000', '1')
# print(fatRes)
