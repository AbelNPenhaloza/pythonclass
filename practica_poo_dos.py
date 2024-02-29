class Animal:
    def __init__(self, cantidad_patas, tipo):
        self.cantidad_patas = cantidad_patas
        self.tipo = tipo
    
    def comer(self):
        return 'Estoy comiendo' 
    
class Perro(Animal):
    
    def __init__(self, cantidad_patas, tipo, nombre, raza):
        super().__init__(cantidad_patas, tipo)  
        self.nombre = nombre
        self.raza = raza
        
    def correr(self):
        return 'Estoy corriendo' 

class Aguila(Animal):
    
    def volar(self):
        return 'Estoy volando...'
  
toto = Perro(4, 'Vertebrado', 'Toto', 'Beagle')
print(f'El perro se llama {toto.nombre} es de raza {toto.raza} es de tipo: {toto.tipo} y tiene: {toto.cantidad_patas} patas')
print(toto.comer())
print(toto.correr())
print('')
aguila1 = Aguila(2, 'Vertebrado')
print(aguila1.tipo)
print(aguila1.volar())
print(aguila1.comer())