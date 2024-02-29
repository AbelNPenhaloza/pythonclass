class Bicicleta:
    
    def __init__(self, marca, color, rodado):
        self.marca = marca
        self.color = color
        self.rodado = rodado
        
    def frenar(self):
        pass
    
    def girar(self):
        pass
    
    def pedalear(self):
        return 'Estoy pedaleando'
    
bici1 = Bicicleta('Vento', 'Verde', 26)
print(f'Color de la Bicicleta: {bici1.color}')
print(f'Pedalear: {bici1.pedalear()}')
print('')
bici2 = Bicicleta('Bianchi', 'Negro', 29)
print(f'Color de la Bicicleta: {bici2.color}')
print(f'Pedalear: {bici2.pedalear()}')
print('')
bici3 = Bicicleta('Electron', 'Rojo', 20)
print(f'Color de la Bicicleta: {bici3.color}')
print(f'Pedalear: {bici3.pedalear()}')

        
    