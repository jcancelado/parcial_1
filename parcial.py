
class Biblioteca:
    def __init__(self):
        self._libros = []
        self._usuarios = []
    def agregar_libro(self, libro):
        self._libros.append(libro)
    def agregar_usuario(self, usuario):
        self._usuarios.append(usuario)
    @property
    def libros(self):
        return self._libros
    @property
    def usuarios(self):
        return self._usuarios


class Libros(Biblioteca):
    def __init__(self, nombre, autor, categoria):
        self.nombre = nombre
        self.autor = autor
        self.categoria = categoria
    @property
    def info(self):
        return f"'{self.nombre}' de {self.autor} - {self.categoria}"

class Usuario(Biblioteca):
    def __init__(self, nombre, correo, contrasena):
        self.nombre = nombre
        self.correo = correo
        self.__contrasena = contrasena
        self.libros_prestados = []
    def pedir_libro(self, libro):
        if libro in self.libros_prestados:
            print("Ya has pedido este libro.")
        else:
            self.libros_prestados.append(libro)
            print("Has pedido el libro:", libro)
    @property
    def info(self):
        return f"Usuario: {self.nombre}, Correo: {self.correo}"

def main():
    biblioteca = Biblioteca()
    categorias = ["Terror", "Ciencia Ficción", "Romance"]
    x = True
    while x == True:
        opcion = input("Si desea registrar un libro ingrese 1, si desea registrar un usuario ingrese 2, si desea ver las categorias ingrese 3, si desea ver los libros digite 4, si desea ver a los usuarios 5 y para salir 6: ")
        if opcion == "1":
            nombre_libro = input("Ingrese el nombre del libro: ")
            autor_libro = input("Ingrese el autor del libro: ")
            categoriaopcion = input("Ingrese la categoría del libro (1 para Terror, 2 para Ciencia Ficción, 3 para Romance): ")

            if categoriaopcion == 1:
                    categoria_libro = ("Terror")
            elif categoriaopcion == 2:
                    categoria_libro = ("Ciencia Ficción")
            elif categoriaopcion == 3:
                    categoria_libro = ("Romance")
            else:
                    print("esa categoria no existe")
                    continue
            
            
            libro = Libros(nombre_libro, autor_libro, categoria_libro)
            biblioteca.agregar_libro(libro)
        elif opcion == "2":
            nombreusuario = input("Ingrese el nombre del usuario: ")
            correo_usuario = input("Ingrese el correo del usuario: ")
            contrasena_usuario = input("Ingrese la contraseña del usuario: ")
            usuario = Usuario(nombreusuario, correo_usuario, contrasena_usuario)
            biblioteca.agregar_usuario(usuario)
        elif opcion == "3":
            print("Categorías disponibles:")
            for categoria in categorias:
                print(categoria)
        elif opcion == "4":
            for libro in biblioteca.libros:
                print(libro.info)
        elif opcion == "5":
            for usuario in biblioteca.usuarios:
                print(usuario.info)
        elif opcion == "6":
            x = False
        else:
            print("Opción no válida. Por favor, ingrese '1', '2' o '3'.")

   
    
if __name__ == "__main__":
    main()