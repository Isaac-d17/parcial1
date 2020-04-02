class Estudiante:
    """Clase Estudiante Representa la UIP"""
    nombre = ""
    cedula = ""
    genero = ""
    carrera = ""
    estado = True
    def __init__(self, nom, ced):
        self.nombre = nom
        self.cedula = ced
    def imprimir (self):
            print("Su nombre es: ", self.nombre)
            print("Su cedula es:", self.cedula)


yohan = Estudiante("Yohan", 88888888)
yohan.imprimir()