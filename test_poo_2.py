from enum import Enum

class TipoInstrumento(Enum):
    CAT1 = 'Viento'
    CAT2 = 'Cuerdas'
    CAT3 = 'Percusion' 
      
class Fabrica:
    
    def __init__(self):
        self.sucursal = []
    def listarInstrumentos(self):
        pass
    
    def borrarInstrumento(self):
        pass
    
class Sucursal:
    def __init__(self, nombre, instrumentos):
        self.nombre = nombre
        self.instrumentos = []

    def crear_instrumento(self):
        pass
    
class Instrumento:
    def __init__(self, id, precio, tipo_instrumento):
        self.id = id
        self.precio = precio
        self.tipo_instrumento = tipo_instrumento 
        
