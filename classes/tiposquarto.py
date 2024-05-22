from classes.gclass import Gclass

class TiposQuarto(Gclass):
    obj = dict()
    lst = list()
    pos = 0
    sortkey = ''
    auto_number = 1
    nkey = 1
    
    att = ['_codigo','_nome','_preco_noite','_foto']
    header = 'Tipos'
    des = ['Codigo','Tipo','Preço por Noite','Foto']
    def __init__(self, codigo, nome, preco_noite, foto):
        super().__init__()
        if codigo == 'None':    
            codes = TiposQuarto.getatlist('_codigo')
            if codes == []:
                codigo = str(1)
            else:
                codigo = str(max(map(int,TiposQuarto.getatlist('_cod_fatura'))) + 1)
        self._codigo = codigo
        self._nome = nome
        self._preco_noite = preco_noite
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
    def preco_noite(self):
        return self._preco_noite
    @property
    def foto(self):
        return self._foto
    
    @nome.setter
    def nome(self, nome):
        self._nome = nome
    @preco_noite.setter
    def preco_noite(self, preco_noite):
        self._preco_noite = preco_noite
    @foto.setter
    def foto(self, foto):
        self._foto = foto