from unittest import TestCase
from Departamento import *
from mockito import *


__author__ = 'MAMISHO'


class TestDepartamento(TestCase):
    """
    Test de la clase Empresa
    """
    def test_get_salario_total(self):
        """
        Test get_salario_total

        Este es un test del metodo para ver si cumple con la funcionalidad,
        se realizan crean 3 empleados haciendo uso de mcks para no completar datos
        y se les asigna solo el salario porque es el parametro que necesitamos para
        hacer el test

        :return: no devuelve nada
        """
        empleado1 = mock(Empleado)
        when(empleado1).get_salario().thenReturn(100)

        empleado2 = mock()
        when(empleado2).get_Salario().thenReturn(100)

        empleado3 = mock()
        when(empleado3).get_salario().thenReturn(100)

        dept = Departamento('microsoft', 1)

        dept.aniadir_empleado(empleado1)
        dept.aniadir_empleado(empleado2)
        dept.aniadir_empleado(empleado3)

        self.assertEqual(dept.get_salario_total(), 400)

#prueba hecha en la rama dev


class TestDepartamento(TestCase):
    """
    Test de la clase Departamento
    """
    def test_get_salario_total_mensual(self):
        """
        test_get_salario_total_mencual

        Este test del metodo crea 3 empleados haciendo uso de mock, solo
        se asigna el parametro salario mensual para poder realizar las
        pruebas. Luego agregamos a un departamento y realizamos la prueba
        para ver si cumple con la funcionalidad de calcula el salario
        total mensual de un departamento.

        :return: No devuelve nada
        """
        empleado1 = mock(Empleado)
        when(empleado1).get_salario_mensual().thenReturn(1200)

        empleado2 = mock()
        when(empleado2).get_salario_mensual().thenReturn(1200)

        empleado3 = mock()
        when(empleado3).get_salario_mensual().thenReturn(1200)

        dept = Departamento('apple-watch', 2)

        dept.aniadirEmpleado(empleado1)
        dept.aniadirEmpleado(empleado2)
        dept.aniadirEmpleado(empleado3)


        self.assertEqual(dept.get_salario_total_mensual(), 3600)