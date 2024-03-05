from enum import Enum

class TipoInstrumento(Enum):
    PERCUSION = 'Percusion'
    VIENTO = 'Viento'
    CUERDA = 'Cuerda' 

class Instrumento:
    def __init__(self, instrumento_id, precio, tipo):
        self.instrumento_id = instrumento_id
        self.precio = precio
        self.tipo = tipo
class Sucursal:
    def __init__(self, nombre):
        self.nombre = nombre
        self.instrumentos = []

    def agregarInstrumento(self, instrumento):
        self.instrumentos.append(instrumento)
                  
class Fabrica:
    
    def __init__(self):
        self.sucursales = []
    
    def listarInstrumentos(self):
        for sucursal in self.sucursales: # por cada sucursal de la lista sucursales}
            for instrumento in sucursal.instrumentos:
                print (f"Sucursal: {sucursal.nombre}, ID: {instrumento.instrumento_id}, Precio: {instrumento.precio}, Tipo: {instrumento.tipo.value}")
    
    def borrarInstrumento(self, instrumento_id):
        for sucursal in self.sucursales:
            sucursal.instrumentos = [inst for inst in sucursal.instrumentos if inst.instrumento_id != instrumento_id]
        
    def instrumentoPorTipo(self, tipo):
        instrumentos_filtrados = []
        for sucursal in self.sucursales:
            for instrumento in sucursal.instrumentos:
                if instrumento.tipo == tipo:
                    instrumentos_filtrados.append(instrumento)
        return instrumentos_filtrados
    
    def porcentajeInstrumentoPorTipo(self, nombre_sucursal):
        sucursal_encontrada = None
        for sucursal in self.sucursales:
            if sucursal.nombre == nombre_sucursal:
                sucursal_encontrada = sucursal
                break
        if sucursal_encontrada:
            total_instrumentos = len(sucursal_encontrada.instrumentos)
            porcentajes = {
                TipoInstrumento.PERCUSION: sum(1 for inst in sucursal_encontrada.instrumentos 
                                          if inst.tipo == TipoInstrumento.PERCUSION) / total_instrumentos * 100,
                TipoInstrumento.VIENTO: sum(1 for inst in sucursal_encontrada.instrumentos 
                                          if inst.tipo == TipoInstrumento.VIENTO) / total_instrumentos * 100,
                TipoInstrumento.CUERDA: sum(1 for inst in sucursal_encontrada.instrumentos 
                                          if inst.tipo == TipoInstrumento.CUERDA) / total_instrumentos * 100,
            }
            return porcentajes
        else:
            return None
            
    


#Ejemplo de uso:
fabrica = Fabrica()

sucursal1 = Sucursal("Sucursal A")
sucursal1.agregarInstrumento(Instrumento('1', 5000, TipoInstrumento.PERCUSION))
sucursal1.agregarInstrumento(Instrumento('2', 4000, TipoInstrumento.PERCUSION))
sucursal1.agregarInstrumento(Instrumento('3', 7000, TipoInstrumento.PERCUSION))
sucursal1.agregarInstrumento(Instrumento('4', 8000, TipoInstrumento.VIENTO))

sucursal2 = Sucursal("Sucursal B")
sucursal2.agregarInstrumento(Instrumento('5', 5400, TipoInstrumento.CUERDA))
sucursal2.agregarInstrumento(Instrumento('6', 7000, TipoInstrumento.PERCUSION))
sucursal2.agregarInstrumento(Instrumento('7', 6000, TipoInstrumento.CUERDA))
sucursal2.agregarInstrumento(Instrumento('8', 8000, TipoInstrumento.VIENTO))
sucursal2.agregarInstrumento(Instrumento('9', 8500, TipoInstrumento.VIENTO))

fabrica.sucursales.append(sucursal1)
fabrica.sucursales.append(sucursal2)

print("A - Listar Instrumentos: ")
fabrica.listarInstrumentos()
fabrica.borrarInstrumento("4")
print("A - Listar Instrumentos: ")
fabrica.listarInstrumentos()
print('----------------------------')

print('B - Listar Instrumento por Tipo: ')
instrumentos_por_tipo = fabrica.instrumentoPorTipo(TipoInstrumento.PERCUSION)
for inst in instrumentos_por_tipo:
    print(f'ID: {inst.instrumento_id}, Precio: {inst.precio}, Tipo: {inst.tipo.value}')

print('------------------------------------------')
print('Pruebo el porcentaje de Instrumentos por tipo en la Sucursal B')
porcentajes_sucursal_b = fabrica.porcentajeInstrumentoPorTipo('Sucursal B')
if porcentajes_sucursal_b:
    for tipo, porcentaje in porcentajes_sucursal_b.items():
        print(f'{tipo.value}: {porcentaje} %')
        
else:
    print('Sucursal no Encontrada.')


    