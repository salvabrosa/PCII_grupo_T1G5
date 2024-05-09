from classes.gclass import Gclass
from classes.userlogin import Userlogin
from classes.Fatura import Fatura
import datetime

class Fatura_Reserva(Gclass):
    obj = dict()
    lst =list()
    pos = 0
    sortkey = ''
    auto_number = 0
    nkey = 2
    
    att = ['_cod_fatura','_cod_reserva','_preco','_nreservas']
    header = 'Quarto'
    des = ['Codigo da Fatura','Codigo da Reserva','Preço','Nº de reservas']
    
    def __init__(self, cod_fatura, cod_reserva, preco, nreservas):
        super().__init__() 
        if cod_fatura in Fatura.lst:
            if cod_reserva in Reserva.lst:                       # !!!!!!!!!!
                self._cod_fatura = cod_fatura
                self._cod_reserva = cod_reserva
                self._preco = preco
                self._nreservas = nreservas
        
                Fatura_Reserva.obj[cod_fatura] = self
                Fatura_Reserva.lst.append(cod_fatura)
            else:
                print('Product ', Reserva, ' not found')       #QUARTO ?????
        else:
            print('Order ', order_code, ' not found')        #ALTERAR
            
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
    
