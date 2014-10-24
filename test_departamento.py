from unittest import TestCase
from Departamento import *
from mockito import *


__author__ = 'MAMISHO'


class TestDepartamento(TestCase):
    def test_getSalarioTotal(self):

        empleado1=mock(Empleado)
        when(empleado1).getSalario().thenReturn(100)

        empleado2=mock()
        when(empleado2).getSalario().thenReturn(100)

        empleado3=mock()
        when(empleado3).getSalario().thenReturn(100)

        dept= Departamento('microsoft', 1)

        dept.aniadirEmpleado(empleado1)
        dept.aniadirEmpleado(empleado2)
        dept.aniadirEmpleado(empleado3)

        self.assertEqual(dept.getSalarioTotal(),400)