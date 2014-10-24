__author__ = 'MAMISHO'
class Empleado:

    def __init__(self, nombre, apellidos, dni, direccion, edad, email, salario):
        self.nombre=nombre
        self.apellidos=apellidos
        self.dni=dni
        self.direccion=direccion
        self.edad=edad
        self.email=email
        self.salario=salario

    def getSalario(self):
        return self.salario

    def getDni(self):
        return self.dni

    def getNombreApellidos(self):
        return self.nombre + " " + self.apellidos

    #nuevos cambios en la rama dev
    def get_edad(self):
        return self.edad

    def get_email(self):
        return self.email

    def get_direccion(self):
        return self.direccion

    def get_salario_mensual(self):
        return self.getSalario()*12

