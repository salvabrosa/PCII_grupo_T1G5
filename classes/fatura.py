from classes.gclass import Gclass
from classes.userlogin import Userlogin
import datetime

class Fatura(Gclass):
    obj = dict()
    lst = list()
    pos = 0
    sortkey = ''
    auto_number = 1
    nkey = 1
    
    att = ['_cod_fatura','_dataemissao','_cod_cliente']
    header = 'Fatura'
    des = ['Codigo','Data Emissão','cod_cliente']
    
    def __init__(self, cod_fatura, dataemissao, cod_cliente):
        super().__init__()  
        if cod_fatura == 'None':    
            codes = Fatura.getatlist('_cod_fatura')
            if codes == []:
                cod_fatura = 'F' + str(1)
            else:
                cod_fatura = 'F' + str(int(Fatura.getatlist('_cod_fatura')[-1].replace('F','')) + 1)
        # Object attributes
        # Check the customer referential integrity
        if cod_cliente in Userlogin.lst:
            self._cod_fatura = cod_fatura
            self._dataemissao = dataemissao
            self._cod_cliente = cod_cliente
        
            Fatura.obj[cod_fatura] = self
            Fatura.lst.append(cod_fatura)
        else:
            print('Customer ', cod_cliente, ' not found')
            
    @property 
    def cod_fatura(self):
        return self._cod_fatura
    @property 
    def dataemissao(self):
        return self._dataemissao
    @property 
    def cod_cliente(self):
        return self._cod_cliente
    
    @dataemissao.setter 
    def dataemissao(self, dataemissao):
        return self._dataemissao                            

    @cod_cliente.setter
    def cod_cliente(self, cod_cliente):
        if cod_cliente in Userlogin.lst:
            self._cod_cliente = cod_cliente
        else:
            print('Customer ', cod_cliente, ' not found') 