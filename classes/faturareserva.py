from datafile import filename

from classes.gclass import Gclass
from classes.hotel import Hotel
from classes.quarto import Quarto
from classes.reservaquarto import ReservaQuarto
from classes.fatura import Fatura
from classes.userlogin import Userlogin

Hotel.read(filename + 'hotel.db')
Quarto.read(filename + 'hotel.db')
ReservaQuarto.read(filename + 'hotel.db')
Fatura.read(filename + 'hotel.db')
Userlogin.read(filename + 'hotel.db')

import datetime

class FaturaReserva(Gclass):
    obj = dict()
    lst =list()
    pos = 0
    sortkey = ''
    auto_number = 0
    nkey = 2
    
    att = ['_cod_fatura','_cod_reserva','_preco','_nreservas']
    header = 'FaturaReserva'
    des = ['Codigo da Fatura','Codigo da Reserva','Preço','Nº de reservas']
    
    def __init__(self, cod_fatura, cod_reserva, preco, nreservas):
        super().__init__() 
        if cod_fatura in Fatura.lst:
            if cod_reserva in ReservaQuarto.lst:
                self._cod_fatura = cod_fatura
                self._cod_reserva = cod_reserva
                self._preco = float(preco)
                self._nreservas = float(nreservas)
        
                code = str(cod_fatura) + str(cod_reserva)
                FaturaReserva.obj[code] = self
                FaturaReserva.lst.append(code)
            else:
                print('Reserva ', cod_reserva, ' not found')
        else:
            print('Fatura ', cod_fatura, ' not found')      
            
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
    
    @preco.setter
    def quantity(self, preco):
        self._preco = float(preco)
    @nreservas.setter
    def nreservas(self, nreservas):
        self._nreservas = float(nreservas)    