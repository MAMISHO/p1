__author__ = 'MAMISHO'
#from Empleado import *


class Departamento:

    def __init__(self, nombre_depto, id_depto):
        """
        Constructor de Departamento

        Este metodo construye un objeto de la clase Departamento

        :param nombre_depto: Nombre del departamento
        :param id_depto: Identificador del departamento
        :return: lista de empleados que preteneceran al departamento
        """

        self.nombre_dep = nombre_depto
        self.id_dep = id_depto
        self.lista_emp = []

    def aniadir_empleado(self, empleado):
        """
        Agregar un empleado nuevo

        este metodo permite agregar un empleado a la lista de empleados
        del departamento

        :param empleado: Objeto del tipo Empleado
        :return: No revuelve nada
        """
        self.lista_emp.append(empleado)

    def get_salariot_total(self):
        """
        Salario total del departamento

        Este metodo suma el salario de todos los empleados del departamento
        y los devuelve.

        :return: Salario total
        """
        tot = 0
        for emp in self.lista_emp:
            tot += emp.getSalario()
        return tot

    #Cambios hechos en la rama dev
    def get_nombre_departamento(self):
        """
        Nombre del departamento

        Este metodo devuleve una cadena String que contienen el
        nombre del departamento

        :return: Nombre del departamento
        """
        return self.nombre_dep

    def get_salario_total_mensual(self):
        """
        Salario total mensual

        Este metodo calcula el salario total mensual de todos los
        empleados del departamento y los devuelve

        :return: salario total mensual
        """
        tot = 0
        for emp in self.lista_emp:
            tot += emp.get_salario_mensual()
        return tot