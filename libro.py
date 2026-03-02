"""
Clase Libro
Representa un libro dentro de la biblioteca digital.
Se usa una tupla para almacenar título y autor (datos inmutables).
"""

class Libro:
    def __init__(self, titulo, autor, categoria, isbn):
        self.__datos_principales = (titulo, autor)  # Tupla
        self.__categoria = categoria
        self.__isbn = isbn
        self.__disponible = True

    def get_titulo(self):
        return self.__datos_principales[0]

    def get_autor(self):
        return self.__datos_principales[1]

    def get_categoria(self):
        return self.__categoria

    def get_isbn(self):
        return self.__isbn

    def esta_disponible(self):
        return self.__disponible

    def prestar(self):
        self.__disponible = False

    def devolver(self):
        self.__disponible = True

    def __str__(self):
        estado = "Disponible" if self.__disponible else "Prestado"
        return f"{self.get_titulo()} - {self.get_autor()} | {self.__categoria} | ISBN: {self.__isbn} | {estado}"
