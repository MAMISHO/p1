__author__ = 'MAMISHO'
#from Empleado import *
#esta clase se crea en el master de git


class Empresa:

    def __init__(self, nombre, cif, razon):
        """
        Consructor de Empresa

        Este metodo crea un objeto de tipo empresa que recibe y asigan los
        siguiente parametros

        :param nombre: Nombre de la empresa
        :param cif: Identificador de la empresa
        :param razon: Sector al que se dedica la empresa
        :return:
        """

        self.nombre_empresa = nombre
        self.cif = cif
        self.razon_social = razon
        self.lista_dep = []

