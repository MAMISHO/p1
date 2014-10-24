__author__ = 'MAMISHO'
from Empleado import *
#esta clase se crea en el master de git
class Empresa:

    def __init__(self, nombre, cif, razon):
        self.nombre_empresa=nombre
        self.cif=cif
        self.razon_social=razon
        self.lista_dep = []

    