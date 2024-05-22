from classes.gclass import Gclass
import datetime

class ReservaQuarto(Gclass):
    obj = dict()
    lst =list()
    pos = 0
    sortkey = ''
    auto_number = 1
    nkey = 1
    
    att = ['_codigo','_codigo_cliente','_checkin','_checkout','_nadultos','_ncrianças','_pequenoalmoco','_estado_reserva','_cod_quarto']
    header = 'ReservaQuarto'
    des = ['Codigo','Codigo do cliente','Check-in','Check-out','Nº de adultos','Nº de crianças','Pequeno Almoço','Estado da reserva','Codigo do quarto']
    
    def __init__(self, codigo, codigo_cliente, checkin, checkout, nadultos, ncriancas, pequenoalmoco, estado_reserva, cod_quarto):
        super().__init__() 
        
        if codigo == 'None':    
            codes = ReservaQuarto.getatlist('_codigo')
            if codes == []:
                codigo = 'RQ' + str(1)
            else:
                codigo = 'RQ' + str(int(ReservaQuarto.getatlist('_codigo')[-1].replace('RQ','')) + 1)
                
        self._codigo = codigo
        self._codigo_cliente = codigo_cliente
        self._checkin = datetime.date.fromisoformat(checkin)
        self._checkout = datetime.date.fromisoformat(checkout)
        self._nadultos = nadultos
        self._ncriancas = ncriancas
        self._pequenoalmoco = pequenoalmoco
        self._estado_reserva = estado_reserva
        self._cod_quarto = cod_quarto
        
        ReservaQuarto.obj[codigo] = self
        ReservaQuarto.lst.append(codigo)

    @property 
    def codigo(self):
        return self._codigo
    @property 
    def codigo_cliente(self):
        return self._codigo_cliente
    @property 
    def checkin(self):
        return self._checkin
    @property 
    def checkout(self):
        return self._checkout
    @property 
    def nadultos(self):
        return self._nadultos
    @property 
    def ncriancas(self):
        return self._ncriancas
    @property 
    def pequenoalmoco(self):
        return self._pequenoalmoco   
    @property 
    def estado_reserva(self):
        return self._estado_reserva
    @property 
    def cod_quarto(self):
        return self._cod_quarto
    
    @checkin.setter
    def checkin(self, checkin):
        self._checkin = checkin
    @checkout.setter
    def checkout(self, checkout):
        self._checkout = checkout
    @nadultos.setter
    def nadultos(self, nadultos):
        self._nadultos = nadultos
    @ncriancas.setter
    def ncriancas(self, ncriancas):
        self._ncriancas = ncriancas
    @pequenoalmoco.setter
    def pequenoalmoco(self, pequenoalmoco):
        self._pequenoalmoco = pequenoalmoco
    @estado_reserva.setter
    def estado_reserva(self, estado_reserva):
        self._estado_reserva = estado_reserva
    @cod_quarto.setter
    def cod_quarto(self, cod_quarto):
        self._cod_quarto = cod_quarto