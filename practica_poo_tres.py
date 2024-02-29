class Persona:
    def __init__(self, nombre, apellido, edad, profesion):
        self.nombre = nombre
        self.apellido = apellido
        self.edad =edad
        self.profesion = profesion
        
    def trabajar(self):
        return 'estoy trabajando'
    
    def caminar(self):
        return 'estoy caminado'
    
    def anadar_en_bicicleta(self, bicicleta):
        return bicicleta.pedalear()
    
class Bicicleta:
    
    def __init__(self, marca, color):
        self.marca = marca
        self.color = color
    
    def pedalear(self):
        return 'Pedaleando'
    
juan= Persona('Juan', 'Lopez', 25, 'abogado')
bici= Bicicleta('Bianchi', 'Amarillo')

print(f'Soy {juan.nombre} {juan.apellido}')
print(f'Tengo {juan.edad}, anios')
print(f'Soy {juan.profesion}.')
print('')
print(f'Ahora mismo {juan.trabajar()}')
print(f'Ahora {juan.caminar()}')
print('')
print(f'Ahora doy vueltas en bicicleta: {juan.anadar_en_bicicleta(bici)}')

    