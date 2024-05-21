from classes.gclass import Gclass
from classes.hotel import Hotel
from classes.tiposquarto import TiposQuarto
import datetime

class Quarto(Gclass):
    obj = dict()
    lst =list()
    pos = 0
    sortkey = ''
    auto_number = 1
    nkey = 1
    
    att = ['_codigo','_cod_hotel','_andar','_tipoquarto','_preco_noite','_estado_reserva']
    header = 'Quarto'
    des = ['Codigo do quarto','Codigo do hotel','Andar','Tipo do quarto','Preco Noite','Estado da reserva']
    
    def __init__(self, codigo, cod_hotel, andar, tipoquarto, preco_noite,  estado_reserva):
        super().__init__()
        
        if cod_hotel in Hotel.lst:
            if tipoquarto in TiposQuarto.lst:
                
                if codigo == 'None':    
                    codes_quarto_hotel = Hotel.obj[cod_hotel]._lista_quartos
                    codes_andar=[]
                    for code in codes_quarto_hotel:
                        code_separado = code.split(';')
                        if code_separado[0] == andar:
                            codes_andar.append(code_separado[1])
                        
                    if codes_andar == []:
                        codigo_sem_andar = str('01')
                    else:
                        if int(codes_andar[-1]) + 1 >= 10 :
                            codigo_sem_andar =  str(int(codes_andar[-1]) + 1)                        
                        else:
                            codigo_sem_andar = '0' + str(int(codes_andar[-1]) + 1)
                            
                    codigo_no_hotel = str(andar) + codigo_sem_andar 
                    self._codigo = str(f'{cod_hotel}') + '-' + codigo_no_hotel                     
                else:
                    codigo_sem_andar = codigo.split('-')[1].replace(andar,'',1)
                    self._codigo = codigo
                    
                self._cod_hotel = cod_hotel
                self._andar = andar
                self._tipoquarto = tipoquarto
                self._preco_noite = preco_noite
                self._estado_reserva = estado_reserva
            
                Hotel.obj[cod_hotel]._lista_quartos.append(f'{self.andar};{codigo_sem_andar}')
        
                Quarto.obj[self._codigo] = self
                Quarto.lst.append(self._codigo)
            else:
                print('Tipos ', tipoquarto, ' not found')
        else:
            print('Hotel ', cod_hotel, ' not found')
            
    @property 
    def codigo(self):
        return self._codigo
    @property 
    def cod_hotel(self):
        return self._cod_hotel
    @property 
    def andar(self):
        return self._andar
    @property
    def tipoquarto(self):
        return self._tipoquarto
    @property 
    def preco_noite(self):
        return self._preco_noite
    @property 
    def estado_reserva(self):
        return self._estado_reserva
    
    @codigo.setter
    def codigo(self, codigo):
        self._codigo = codigo
    @cod_hotel.setter
    def cod_hotel(self, cod_hotel):
        if cod_hotel in Hotel.lst:
            self._cod_hotel = cod_hotel
        else:
            print('Hotel ', cod_hotel, ' not found')
    @andar.setter
    def andar(self, andar):
        self._andar = andar
    @tipoquarto.setter
    def tipoquarto(self, tipoquarto):
        if tipoquarto in TiposQuarto.lst:
            self._tipoquarto = tipoquarto
        else:
            print('Tipos ', tipoquarto, ' not found')
    @preco_noite.setter 
    def preco_noite(self, preco_noite):
        self._preco_noite = preco_noite  
    @estado_reserva.setter 
    def estado_reserva(self, estado_reserva):
        self._estado_reserva = estado_reserva