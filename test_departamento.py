from unittest import TestCase
from Departamento import *
from mockito import *


__author__ = 'MAMISHO'


class TestDepartamento(TestCase):
    def test_getSalarioTotal(self):
        empleado1 = mock(Empleado)
        when(empleado1).getSalario().thenReturn(100)

        empleado2 = mock()
        when(empleado2).getSalario().thenReturn(100)

        empleado3 = mock()
        when(empleado3).getSalario().thenReturn(100)

        dept = Departamento('microsoft', 1)

        dept.aniadirEmpleado(empleado1)
        dept.aniadirEmpleado(empleado2)
        dept.aniadirEmpleado(empleado3)

        self.assertEqual(dept.getSalarioTotal(), 400)

#prueba hecha en la rama dev
class TestDepartamento(TestCase):
    def test_get_salario_total_mensual(self):
        empleado1 = mock(Empleado)
        when(empleado1).get_salario_mensual().thenReturn(200)

        empleado2 = mock()
        when(empleado2).get_salario_mensual().thenReturn(200)

        empleado3 = mock()
        when(empleado3).get_salario_mensual().thenReturn(200)

        dept = Departamento('apple-watch', 2)

        dept.aniadirEmpleado(empleado1)
        dept.aniadirEmpleado(empleado2)
        dept.aniadirEmpleado(empleado3)

        self.assertEqual(dept.get_salario_total_mensual(), 600)