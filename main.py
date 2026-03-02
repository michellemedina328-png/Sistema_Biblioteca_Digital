from biblioteca import Biblioteca
from libro import Libro
from usuario import Usuario


def menu():
    print("\n===== BIBLIOTECA DIGITAL =====")
    print("1. Agregar libro")
    print("2. Registrar usuario")
    print("3. Prestar libro")
    print("4. Devolver libro")
    print("5. Buscar libro")
    print("6. Listar libros prestados por usuario")
    print("7. Salir")


def main():
    biblioteca = Biblioteca()

    while True:
        menu()
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            titulo = input("Título: ")
            autor = input("Autor: ")
            categoria = input("Categoría: ")
            isbn = input("ISBN: ")
            libro = Libro(titulo, autor, categoria, isbn)
            biblioteca.agregar_libro(libro)

        elif opcion == "2":
            nombre = input("Nombre usuario: ")
            id_usuario = input("ID usuario: ")
            usuario = Usuario(nombre, id_usuario)
            biblioteca.registrar_usuario(usuario)

        elif opcion == "3":
            isbn = input("ISBN del libro: ")
            id_usuario = input("ID usuario: ")
            biblioteca.prestar_libro(isbn, id_usuario)

        elif opcion == "4":
            isbn = input("ISBN del libro: ")
            id_usuario = input("ID usuario: ")
            biblioteca.devolver_libro(isbn, id_usuario)

        elif opcion == "5":
            criterio = input("Buscar por título, autor o categoría: ")
            biblioteca.buscar_libros(criterio)

        elif opcion == "6":
            id_usuario = input("Ingrese ID del usuario: ")
            biblioteca.listar_libros_usuario(id_usuario)

        elif opcion == "7":
            print("Saliendo del sistema...")
            break

        else:
            print("Opción inválida")


if __name__ == "__main__":
    main()
