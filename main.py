from biblioteca import Biblioteca
from libro import Libro
from usuario import Usuario


def menu():
    print("\n===== BIBLIOTECA DIGITAL =====")
    print("1. Agregar libro")
    print("2. Eliminar libro")
    print("3. Registrar usuario")
    print("4. Eliminar usuario")
    print("5. Prestar libro")
    print("6. Devolver libro")
    print("7. Buscar libro")
    print("8. Listar libros prestados por usuario")
    print("9. Salir")


def main():
    biblioteca = Biblioteca()

    while True:
        menu()
        opcion = input("Seleccione una opción: ")

        # ==============================
        # LIBROS
        # ==============================

        if opcion == "1":
            titulo = input("Título: ")
            autor = input("Autor: ")
            categoria = input("Categoría: ")
            isbn = input("ISBN: ")
            libro = Libro(titulo, autor, categoria, isbn)
            biblioteca.agregar_libro(libro)

        elif opcion == "2":
            isbn = input("Ingrese ISBN del libro a eliminar: ")
            biblioteca.eliminar_libro(isbn)

        # ==============================
        # USUARIOS
        # ==============================

        elif opcion == "3":
            nombre = input("Nombre usuario: ")
            id_usuario = input("ID usuario: ")
            usuario = Usuario(nombre, id_usuario)
            biblioteca.registrar_usuario(usuario)

        elif opcion == "4":
            id_usuario = input("Ingrese ID del usuario a eliminar: ")
            biblioteca.eliminar_usuario(id_usuario)

        # ==============================
        # PRÉSTAMOS
        # ==============================

        elif opcion == "5":
            isbn = input("ISBN del libro: ")
            id_usuario = input("ID usuario: ")
            biblioteca.prestar_libro(isbn, id_usuario)

        elif opcion == "6":
            isbn = input("ISBN del libro: ")
            id_usuario = input("ID usuario: ")
            biblioteca.devolver_libro(isbn, id_usuario)

        # ==============================
        # BÚSQUEDA Y CONSULTA
        # ==============================

        elif opcion == "7":
            criterio = input("Buscar por título, autor o categoría: ")
            biblioteca.buscar_libros(criterio)

        elif opcion == "8":
            id_usuario = input("Ingrese ID del usuario: ")
            biblioteca.listar_libros_usuario(id_usuario)

        # ==============================

        elif opcion == "9":
            print("Saliendo del sistema...")
            break

        else:
            print("Opción inválida")


if __name__ == "__main__":
    main()
