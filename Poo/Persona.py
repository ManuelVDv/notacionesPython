class Persona:
    compania = "xyz"

    def __init__(self, id, nombre, apellido, correo, contrasena):  # Debes usar doble guión bajo al principio y al final (__init__)
        self.id = id
        self.nombre = nombre
        self.apellido = apellido
        self.correo = correo
        self.contrasena = contrasena

    def verPersona(self):
        print(f"Id: {self.id} \n",
              f"Nombre: {self.nombre} \n",
              f"Correo: {self.correo} \n",
              f"Compañia: {self.compania}")  # Corregí "Corre" a "Correo"

maria = Persona(1, "Maria", "Gomez", "maria@gmail.com", "admin123")  # Corregí el apellido y la contraseña
maria.verPersona()
maria.correo = "Correo@gmail.com"  # Corregí el valor del correo