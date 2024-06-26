from classes.gclass import Gclass
import datetime

class Hotel(Gclass):
    obj = dict()
    lst =list()
    pos = 0
    sortkey = ''
    auto_number = 1
    nkey = 1
    
    att = ['_codigo','_nome','_localizacao','_nandares','_nquartos','_contacto','_nfuncionarios','_video']
    header = 'Hotel'
    des = ['Codigo','Nome','Localização','Nº de andares','Nº de quartos','Contacto','Nº de funcionários','Video']
    
    def __init__(self, codigo, nome, localizacao, nandares, nquartos, contacto, nfuncionarios, video):
        super().__init__()  
        if codigo == 'None':    
            codes = Hotel.getatlist('_codigo')
            if codes == []:
                codigo = str('H')+str(1)
            else:
                codigo = str('H')+str(int(Hotel.getatlist('_codigo')[-1].replace("H",''))+1)
        self._codigo = codigo
        self._nome = nome
        self._nquartos = nquartos
        self._localizacao = localizacao
        self._nandares = nandares
        self._nfuncionarios = nfuncionarios
        self._contacto = contacto        
        self._video = video
        
        self._lista_quartos = []
        
        Hotel.obj[codigo] = self
        Hotel.lst.append(codigo)
        
        
    @property 
    def codigo(self):
        return self._codigo
    @property 
    def nome(self):
        return self._nome
    @property 
    def nquartos(self):
        return self._nquartos
    @property 
    def localizacao(self):
        return self._localizacao
    @property 
    def contacto(self):
        return self._contacto 
    @property 
    def nfuncionarios(self):
        return self._nfuncionarios
    @property 
    def video(self):
        return self._video
    # PARA O LINK DO MAPS 
    @property 
    def maps_lugar(self):
        return self._localizacao.replace(' ','+')
    #PARA QUARTO AUTONUMBER
    @property 
    def lista_quartos(self):
        return self._lista_quartos
    #PARA ANDAR DO QUARTO
    @property 
    def nandares(self):
        return self._nandares
    # PARA LISTA DE ANDARES NO FORM QUARTOS
    @property 
    def lista_andares(self):
        lista_andares = []
        for i in range(1,int(self.nandares)+1):
            lista_andares.append(i)
        return lista_andares
    
    @codigo.setter 
    def codigo(self, codigo):
        self._codigo = codigo
    @nome.setter 
    def nome(self, nome):
        self._nome = nome
    @localizacao.setter 
    def localizacao(self, localizacao):
        self._localizacao = localizacao    
    @nquartos.setter 
    def nquartos(self, nquartos):
        self._nquartos = nquartos
    @contacto.setter 
    def contacto(self, contacto):
        self._contacto = contacto
    @nfuncionarios.setter 
    def nfuncionarios(self, nfuncionarios):
        self._nfuncionarios = nfuncionarios
    @video.setter 
    def video(self, video):
        self._video = video

