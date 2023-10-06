from Poo.Persona import Persona

class Estudiante(Persona):  # Cambié "Estuadiante" a "Estudiante"

    def __init__(self, id, nombre, correo, contrasena, programa, semestre):  # Debes usar doble guión bajo al principio y al final (__init__)
        super().__init__(id, nombre, correo, contrasena)  # Cambié "_init_" a "__init__"
        self.programa = programa
        self.semestre = semestre

    def verPersona(self):
        print(f"Id: {self.id} \n",
              f"Nombre: {self.nombre} \n",
              f"Correo: {self.correo} \n",
              f"Compañia: {self.compania} \n",
              f"Programa: {self.programa} \n",
              f"Semestre: {self.semestre}")  # Corregí la impresión de "Programa" y "Semestre"

estudiante1 = Estudiante(1, "Maria", "Maria@gmail.com", "admin123", "Software", "Semestre01")  # Cambié "Estuadiante" a "Estudiante"