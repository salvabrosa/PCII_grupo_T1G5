from classes.gclass import Gclass
import datetime

class Fatura(Gclass):
    obj = dict()
    lst =list()
    pos = 0
    sortkey = ''
    autonumber = 0
    nkey = 1
    
    att = ['_cod_fatura','_dataemissao','_cod_cliente']
    header = 'Fatura'
    des = ['Codigo','Data Emissão','cod_cliente']
    
    def __init__(self, cod_fatura, dataemissao, cod_cliente):
        super().__init__()  
        self._cod_fatura = cod_fatura
        self._dataemissao = dataemissao
        self._cod_cliente = cod_cliente
        
        Fatura.lst.append(self)
        Fatura.obj[cod_fatura] = self
        
    @property 
    def cod_fatura(self):
        return self._cod_fatura
    @property 
    def dataemissao(self):
        return self._dataemissao
    @property 
    def cod_cliente(self):
        return self._cod_cliente
    
    def pagar(self):
        pass