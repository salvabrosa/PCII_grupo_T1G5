from classes.gclass import Gclass

class TiposQuarto(Gclass):
    obj = dict()
    lst = list()
    pos = 0
    sortkey = ''
    auto_number = 0
    nkey = 1
    
    att = ['_codigo','_nome','_foto']
    header = 'Tipos'
    des = ['Codigo','Tipo','Foto']
    def __init__(self, codigo, nome, foto):
        super().__init__()

        self._codigo = codigo
        self._nome = nome
        self._foto = foto

        TiposQuarto.obj[codigo] = self
        TiposQuarto.lst.append(codigo)

    @property
    def codigo(self):
        return self._codigo
    @property
    def nome(self):
        return self._nome    
    @property
    def foto(self):
        return self._foto
    @nome.setter
    def nome(self, nome):
        self._nome = nome
    @foto.setter
    def foto(self, foto):
        self._foto = foto