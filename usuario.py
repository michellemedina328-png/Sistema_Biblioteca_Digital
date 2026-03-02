"""
Clase Usuario
Representa un usuario registrado en la biblioteca.
Utiliza una lista para almacenar libros prestados.
"""

class Usuario:
    def __init__(self, nombre, id_usuario):
        self.__nombre = nombre
        self.__id_usuario = id_usuario
        self.__libros_prestados = []  # Lista

    def get_id(self):
        return self.__id_usuario

    def get_nombre(self):
        return self.__nombre

    def prestar_libro(self, libro):
        self.__libros_prestados.append(libro)

    def devolver_libro(self, libro):
        if libro in self.__libros_prestados:
            self.__libros_prestados.remove(libro)

    # 🔎 Método para validar si el usuario tiene el libro
    def tiene_libro(self, libro):
        return libro in self.__libros_prestados

    def listar_libros(self):
        if not self.__libros_prestados:
            print("No tiene libros prestados.")
        else:
            for libro in self.__libros_prestados:
                print(libro)
