from classes.gclass import Gclass

class TiposQuarto(Gclass):
    obj = dict()
    lst = list()
    pos = 0
    sortkey = ''
    auto_number = 0
    nkey = 1
    
    att = ['_codigo','_nome']
    header = 'Tipos'
    des = ['Codigo','Tipo']
    def __init__(self, codigo, nome):
        super().__init__()

        self._codigo = codigo
        self._nome = nome

        TiposQuarto.obj[codigo] = self
        TiposQuarto.lst.append(codigo)

    @property
    def codigo(self):
        return self._codigo
    @property
    def nome(self):
        return self._nome    
    @nome.setter
    def nome(self, nome):
        self._nome = nome