"""
Clase Biblioteca
Gestiona libros, usuarios y préstamos.

Utiliza:
- Diccionario para libros (ISBN como clave)
- Diccionario para usuarios
- Conjunto para garantizar IDs únicos
"""

from libro import Libro
from usuario import Usuario


class Biblioteca:
    def __init__(self):
        self.libros = {}        # ISBN -> Libro
        self.usuarios = {}      # ID -> Usuario
        self.ids_usuarios = set()  # Conjunto para IDs únicos

    # ==============================
    # Gestión de libros
    # ==============================

    def agregar_libro(self, libro):
        if libro.get_isbn() in self.libros:
            print("ISBN ya existe.")
            return
        self.libros[libro.get_isbn()] = libro
        print("Libro agregado correctamente.")

    def eliminar_libro(self, isbn):
        if isbn in self.libros:
            del self.libros[isbn]
            print("Libro eliminado.")
        else:
            print("Libro no encontrado.")

    # ==============================
    # Gestión de usuarios
    # ==============================

    def registrar_usuario(self, usuario):
        if usuario.get_id() in self.ids_usuarios:
            print("ID de usuario ya registrado.")
            return
        self.usuarios[usuario.get_id()] = usuario
        self.ids_usuarios.add(usuario.get_id())
        print("Usuario registrado correctamente.")

    def eliminar_usuario(self, id_usuario):
        if id_usuario in self.usuarios:
            del self.usuarios[id_usuario]
            self.ids_usuarios.remove(id_usuario)
            print("Usuario eliminado.")
        else:
            print("Usuario no encontrado.")

    # ==============================
    # Préstamos
    # ==============================

    def prestar_libro(self, isbn, id_usuario):

        if isbn not in self.libros:
            print("Libro no encontrado.")
            return

        if id_usuario not in self.usuarios:
            print("Usuario no encontrado.")
            return

        libro = self.libros[isbn]
        usuario = self.usuarios[id_usuario]

        if libro.esta_disponible():
            libro.prestar()
            usuario.prestar_libro(libro)
            print("Libro prestado correctamente.")
        else:
            print("El libro no está disponible.")

    # 🔒 MÉTODO CORREGIDO Y ROBUSTO
    def devolver_libro(self, isbn, id_usuario):

        if isbn not in self.libros:
            print("Libro no encontrado.")
            return

        if id_usuario not in self.usuarios:
            print("Usuario no encontrado.")
            return

        libro = self.libros[isbn]
        usuario = self.usuarios[id_usuario]

        if usuario.tiene_libro(libro):
            usuario.devolver_libro(libro)
            libro.devolver()
            print("Libro devuelto correctamente.")
        else:
            print("Este usuario no tiene prestado ese libro.")

    # ==============================
    # Búsqueda
    # ==============================

    def buscar_libros(self, criterio):
        resultados = [
            libro for libro in self.libros.values()
            if criterio.lower() in libro.get_titulo().lower()
            or criterio.lower() in libro.get_autor().lower()
            or criterio.lower() in libro.get_categoria().lower()
        ]

        if resultados:
            for libro in resultados:
                print(libro)
        else:
            print("No se encontraron resultados.")

    # ==============================
    # Listar libros por usuario
    # ==============================

    def listar_libros_usuario(self, id_usuario):

        if id_usuario not in self.usuarios:
            print("Usuario no encontrado.")
            return

        usuario = self.usuarios[id_usuario]
        print(f"\nLibros prestados por {usuario.get_nombre()}:")
        usuario.listar_libros()
