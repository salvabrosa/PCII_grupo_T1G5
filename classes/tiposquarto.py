from classes.gclass import Gclass

class TiposQuarto(Gclass):
    obj = dict()
    lst = list()
    pos = 0
    sortkey = ''
    auto_number = 0
    nkey = 1
    
    att = ['_codigo','_name']
    header = 'Tipos'
    des = ['Codigo','Tipo']
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