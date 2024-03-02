class Estudiante:
    
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad =edad
        self.calificacion = []
        
    def agregar_calificacion(self, calificacion):
        self.calificacion.append(calificacion)
        
    def promedio_calificaciones(self):
        if self.calificaciones:
            return sum(self)