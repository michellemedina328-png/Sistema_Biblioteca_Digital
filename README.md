## MAYRA MICHELLE MORAN MEDINA
## TECNOLOGIAS DE LA INFORMACION 
## SEGUNDO SEMESTRE 
## mm.moranm@uea.edu.ec

# Sistema de Gestión de Biblioteca Digital

El presente proyecto consiste en el desarrollo de un Sistema de Gestión de Biblioteca Digital implementado en Python, aplicando los principios de la Programación Orientada a Objetos (POO) y el uso de colecciones como listas, diccionarios, conjuntos y tuplas.

El sistema permite administrar libros, usuarios y préstamos mediante una estructura organizada y eficiente, simulando el funcionamiento básico de una biblioteca digital.

---

## Objetivo

Desarrollar un sistema funcional que permita:

- Gestionar libros dentro del catálogo.
- Registrar y administrar usuarios.
- Realizar préstamos y devoluciones de libros.
- Buscar libros por título, autor o categoría.
- Aplicar correctamente colecciones en Python dentro de un entorno orientado a objetos.

---

## Diseño del Sistema

El sistema está compuesto por tres clases principales:

### Clase `Libro`
- Utiliza una **tupla** para almacenar el título y el autor (datos inmutables).
- Gestiona el estado del libro (disponible o prestado).
- Contiene métodos para préstamo y devolución.

### Clase `Usuario`
- Representa a un usuario registrado.
- Utiliza una **lista** para almacenar los libros prestados.
- Incluye métodos para prestar, devolver, verificar y listar libros.

### Clase `Biblioteca`
- Gestiona el catálogo de libros y los usuarios.
- Utiliza:
  - **Diccionario** para almacenar libros usando el ISBN como clave.
  - **Diccionario** para almacenar usuarios registrados.
  - **Conjunto** para garantizar la unicidad de los IDs de usuarios.
- Implementa funcionalidades de:
  - Registro y eliminación de usuarios.
  - Agregar y eliminar libros.
  - Préstamo y devolución con validaciones robustas.
  - Búsqueda por diferentes criterios.
  - Listado de libros prestados por usuario.

---

## ⚙️ Funcionalidades Implementadas

- Agregar libros    
- Registrar usuarios 
- Prestar libros  
- Devolver libros con validación de posesión  
- Buscar libros por título, autor o categoría  

---

## 📚 Colecciones Utilizadas

- **Tupla** → Almacena título y autor del libro como datos inmutables.  
- **Lista** → Gestiona los libros prestados por cada usuario.  
- **Diccionario** → Permite almacenar libros por ISBN para búsqueda eficiente.  
- **Conjunto** → Garantiza IDs únicos de usuarios registrados.  

---

## Conclusión

El desarrollo de este sistema permitió aplicar de manera práctica los conceptos de Programación Orientada a Objetos y el uso eficiente de colecciones en Python. Se logró diseñar un sistema modular, organizado y funcional, reforzando habilidades en estructuración de código y control de datos.
