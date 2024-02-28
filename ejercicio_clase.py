from enum import Enum

class TipoContrato(Enum):
    FIJO = "Salario Fijo"
    COMISION = "Por Comision"

class Antiguedad(Enum):
    CAT1 = "Menos de 2 años"
    CAT2 = "Entre 2 y 5 años"
    CAT3 = "Mas de 5 años"

class Empleado:
    SALARIO_MINIMO = 200000
    SUELDO_BASICO = 250000
    MONTO_POR_CLIENTE = 15000
    
    def __init__(self, dni, nombre, apellido, anio_ingreso, tipo_contrato):
        self.dni = dni
        self.nombre = nombre
        self.apellido = apellido
        self.anio_ingreso = anio_ingreso
        self.tipo_contrato = tipo_contrato

    def calcular_salario(self):
        pass
    def mostrar_salario(self):
        salario = self.calcular_salario()
        print(f'{self.nombre} {self.apellido} - Salario: ${salario: .2f}')
        
    def __str__(self):
        return f"{self.nombre} {self.apellido}"

    def obtener_antiguedad(self):
        anios_en_empresa = 2024 - self.anio_ingreso
        if anios_en_empresa < 2:
            return Antiguedad.CAT1
        elif 2 <= anios_en_empresa <= 5:
            return Antiguedad.CAT2
        else:
            return Antiguedad.CAT3


class EmpleadoComision(Empleado):
    def __init__(self, dni, nombre, apellido, anio_ingreso, salario_minimo, clientes_captados):
        super().__init__(dni, nombre, apellido, anio_ingreso, TipoContrato.COMISION)
        self.salario_minimo = salario_minimo
        self.clientes_captados = clientes_captados
        

    def calcular_salario(self):
        salario = self.clientes_captados * self.MONTO_POR_CLIENTE
        if salario < self.SALARIO_MINIMO:
            salario = self.SALARIO_MINIMO
        return salario
    
    @staticmethod
    def empleadoConMasClientes(empleados):
        empleado_max_clientes = None
        max_clientes = -1

        for empleado in empleados:
            if isinstance(empleado, EmpleadoComision):
                if empleado.clientes_captados > max_clientes:
                    max_clientes = empleado.clientes_captados
                    empleado_max_clientes = empleado

        return empleado_max_clientes, max_clientes


class EmpleadoSalarioFijo(Empleado):
    
    def __init__(self, dni, nombre, apellido, anio_ingreso, sueldo_basico):
        super().__init__(dni, nombre, apellido, anio_ingreso, TipoContrato.FIJO)
        self.sueldo_basico = sueldo_basico
        self.antiguedad = self.obtener_antiguedad()

        if self.antiguedad == Antiguedad.CAT2:
            self.porcentaje_adicional = 0.05
        elif self.antiguedad == Antiguedad.CAT3:
            self.porcentaje_adicional = 0.10

    def calcular_salario(self):
        salario = self.SUELDO_BASICO
        if hasattr(self, 'porcentaje_adicional'):
            salario *= (1 + self.porcentaje_adicional)
        return salario
    
# Crear 10 empleados con los DNI especificados
empleados = [
    EmpleadoComision(34567879, "Juan", "Perez", 2019, TipoContrato.COMISION.value, clientes_captados=15),
    EmpleadoComision(35678901, "Maria", "Gomez", 2020, TipoContrato.COMISION.value, clientes_captados=20),
    EmpleadoComision(36789012, "Luis", "Martinez", 2018, TipoContrato.COMISION.value, clientes_captados=10),
    EmpleadoSalarioFijo(37890123, "Ana", "Lopez", 2017, TipoContrato.FIJO.value),
    EmpleadoSalarioFijo(38901234, "Pedro", "Rodriguez", 2015, TipoContrato.FIJO.value),
    EmpleadoComision(39012345, "Laura", "Sanchez", 2021, TipoContrato.COMISION.value, clientes_captados=25),
    EmpleadoSalarioFijo(40123456, "Diego", "Garcia", 2019, TipoContrato.FIJO.value),
    EmpleadoComision(41234567, "Carla", "Fernandez", 2016, TipoContrato.COMISION.value, clientes_captados=0),
    EmpleadoSalarioFijo(42345678, "Sofia", "Diaz", 2014, TipoContrato.FIJO.value),
    EmpleadoComision(42456789, "Pablo", "Alvarez", 2022, TipoContrato.COMISION.value, clientes_captados=18),
]

# Mostrar salarios de los empleados
for empleado in empleados:
    empleado.mostrar_salario()

# Encontrar y mostrar el empleado con más clientes captados y la cantidad de clientes
empleado_max_clientes, cantidad_clientes = EmpleadoComision.empleadoConMasClientes(empleados)
if empleado_max_clientes:
    print(f"Empleado con más clientes captados: {empleado_max_clientes.nombre} {empleado_max_clientes.apellido} ({cantidad_clientes} clientes)")
else:
    print("No hay empleados a comisión.")