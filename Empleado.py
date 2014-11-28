__author__ = 'MAMISHO'


class Empleado:

    def __init__(self, nombre, apellidos, dni, direccion, edad, email, salario):
        """
        Constructor de Empleado

        Este metodo crea un objeto de la clase Empleado que recibe y asigna los siguiente
        parametros

        :param nombre: Nombre del empleado
        :param apellidos: Apellido del empleado
        :param dni: Identificador del empleado, en este caso el DNI
        :param direccion: Direccion del empleado
        :param edad: Edad del empleado
        :param email: Correo electronico del empleado
        :param salario: Salario mensual del empleado
        :return: no devuelve nada
        """
        self.nombre = nombre
        self.apellidos = apellidos
        self.dni = dni
        self.direccion = direccion
        self.edad = edad
        self.email = email
        self.salario = salario

    def get_salario(self):
        """
        Salario del empleado

        Este metodo devuelve el salario anual del empleado

        :return: Salario del empleado con decimales
        """
        return self.salario

    def get_dni(self):
        """
        DNI del empleado

        Este metodo devuelve el identificador del empleado, en este
        caso el DNI del empleado, el id esta definido por 8 numeros
        y una letra mayuscula al final

        :return: String que contiene el identificador del empleado
        """
        return self.dni

    def get_nombre_apellidos(self):
        """
        Nombre y apellidos del empleado

        Este metodo devuelve un String con el nombre y palllido del empleado en
        este orden, tambien se puede invertir el orden, es decir que podemos
        recibir primero el apellido y luego el nombre.

        :return: String con el nombre y apellido del empleado
        """
        return self.nombre + " " + self.apellidos

    #nuevos cambios en la rama dev
    def get_edad(self):
        """
        Edad del empleado

        Este metodo devuelve la edad del empleado

        :return: Edad del empleado
        """
        return self.edad

    def get_email(self):
        """
        Email del empleado

        Este metodo devuelve el correo electronico del empleado

        :return: String que contiene el correo electronico del empleado
        """

        return self.email

    def get_direccion(self):
        """
        Direccion del empleado

        Este metodos devuelve la direccion del empleado

        :return: String con la direccion del empleado
        """

        return self.direccion

    def get_salario_mensual(self):
        """
        Salario mensual

        Este metodo devuelve el salario mensual del empleado, tomndo en cuenta que
        las pagas estan prorrateadas, por eso solo se divide para 12

        :return: Salario mensual del empleado
        """
        return self.get_salario()/12

