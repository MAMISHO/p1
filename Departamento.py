__author__ = 'MAMISHO'
from Empleado import *
class Departamento:

    def __init__(self, nombre_depto, id_depto):
        self.nombre_dep=nombre_depto
        self.id_dep=id_depto
        self.lista_emp = []


    def aniadirEmpleado(self,empleado):
        self.lista_emp.append(empleado)

    def getSalarioTotal(self):
        tot = 0
        for emp in self.lista_emp:
            tot+=emp.getSalario()
        return tot

    #Cambios hechos en la rama dev
    def get_nombre_departamento(self):
        return self.nombre_dep

    def get_salario_total_mensual(self):
        tot=0
        for emp in self.lista_emp:
            tot+=emp.get_salario_mensual()
        return tot
