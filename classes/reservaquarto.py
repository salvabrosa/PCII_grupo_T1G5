from classes.gclass import Gclass
import datetime

class ReservaQuarto(Gclass):
    obj = dict()
    lst =list()
    pos = 0
    sortkey = ''
    auto_number = 0
    nkey = 1
    
    att = ['_cod_reserva','_diaComeco','_diaFim','_estado_reserva','_cod_quarto','_cod_cliente']
    header = 'ReservaQuarto'
    des = ['Codigo da Reserva','Dia de começo','Dia de fim','Estado da reserva','Codigo de quarto','Codigo cliente']
    
    def __init__(self, cod_reserva, diaComeco, diaFim, estado_reserva, cod_quarto, cod_cliente):
        super().__init__()  
        self._cod_reserva = cod_reserva
        self._diaComeco = diaComeco
        self._diaFim = diaFim
        self._estado_reserva=estado_reserva
        self._cod_quarto = cod_quarto
        self._cod_cliente = cod_cliente
        
        ReservaQuarto.obj[cod_reserva] = self
        ReservaQuarto.lst.append(cod_reserva)
        
    @property 
    def cod_reserva(self):
        return self._cod_reserva
    @property 
    def diaComeco(self):
        return self._diaComeco
    @property 
    def diaFim(self):
        return self._diaFim
    @property 
    def estado_reserva(self):
        return self._estado_reserva
    @property 
    def cod_quarto(self):
        return self._cod_quarto
    @property 
    def cod_cliente(self):
        return self._cod_cliente
    @property
    def numeroNoites(self):
        diferença=self._diaFim-self._diaComeco
        return diferença
    
    @cod_reserva.setter
    def cod_reserva(self, cod_reserva):
        self._cod_reserva = cod_reserva
    @diaComeco.setter
    def diaComeco(self, diaComeco):
        self._diaComeco = diaComeco
    @diaFim.setter
    def diaFim(self, diaFim):
        self._diaFim = diaFim
    @estado_reserva.setter
    def estado_reserva(self, estado_reserva):
        self._estado_reserva = estado_reserva
    @cod_quarto.setter
    def cod_quarto(self, cod_quarto):
        self._cod_quarto = cod_quarto
    @cod_cliente.setter
    def cod_cliente(self, cod_cliente):
        self._cod_cliente = cod_cliente
    
    
    
    
    
    