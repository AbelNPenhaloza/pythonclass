from enum import Enum

class TipoContrato(Enum):
    FIJO = "Salario Fijo"
    COMI = "Por Comision"

class Antiguedad(Enum):
    CAT1 = "Menos de 2 años"
    CAT2 = "Entre 2 y 5 años"
    CAT3 = "Mas de 5 años"

class Empleado:
    def __init__(self, dni, nombre, apellido, anio_ingreso, tipo_contrato):
        self.dni = dni
        self.nombre = nombre
        self.apellido = apellido
        self.anio_ingreso = anio_ingreso
        self.tipo_contrato = tipo_contrato

    def calcular_salario(self):
        pass

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
    def __init__(self, dni, nombre, apellido, anio_ingreso, salario_minimo, clientes_captados, monto_por_cliente):
        super().__init__(dni, nombre, apellido, anio_ingreso, TipoContrato.COMI)
        self.salario_minimo = salario_minimo
        self.clientes_captados = clientes_captados
        self.monto_por_cliente = monto_por_cliente

    def calcular_salario(self):
        salario = self.clientes_captados * self.monto_por_cliente
        return max(salario, self.salario_minimo)


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
        salario = self.sueldo_basico
        if hasattr(self, 'porcentaje_adicional'):
            salario *= (1 + self.porcentaje_adicional)
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


def mostrar_salarios(empleados):
    for empleado in empleados:
        salario = empleado.calcular_salario()
        print(f"{empleado} - Salario: ${salario:.2f}")

# Crear 10 empleados con los DNI especificados
empleados = [
    EmpleadoComision(34567879, "Juan", "Perez", 2019, 1000, 15, 50),
    EmpleadoComision(35678901, "Maria", "Gomez", 2020, 1200, 20, 60),
    EmpleadoComision(36789012, "Luis", "Martinez", 2018, 800, 10, 40),
    EmpleadoSalarioFijo(37890123, "Ana", "Lopez", 2017, 2000),
    EmpleadoSalarioFijo(38901234, "Pedro", "Rodriguez", 2015, 1800),
    EmpleadoComision(39012345, "Laura", "Sanchez", 2021, 1500, 25, 70),
    EmpleadoSalarioFijo(40123456, "Diego", "Garcia", 2019, 2200),
    EmpleadoComision(41234567, "Carla", "Fernandez", 2016, 1000, 12, 45),
    EmpleadoSalarioFijo(42345678, "Sofia", "Diaz", 2014, 1900),
    EmpleadoComision(42456789, "Pablo", "Alvarez", 2022, 1300, 18, 55),
]

# Mostrar salarios de los empleados
mostrar_salarios(empleados)

# Encontrar y mostrar el empleado con más clientes captados y la cantidad de clientes
empleado_max_clientes, cantidad_clientes = EmpleadoSalarioFijo.empleadoConMasClientes(empleados)
if empleado_max_clientes:
    print(f"Empleado con más clientes captados: {empleado_max_clientes.nombre} {empleado_max_clientes.apellido} ({cantidad_clientes} clientes)")
else:
    print("No hay empleados a comisión.")