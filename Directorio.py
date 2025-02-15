class DirectorioTelefonico:
    def __init__(self):
        pass

    @staticmethod
    def añadir(a,b,c):
            print("DATOS: ")
            print("Nombre: ", a)
            print("Numero: ", b)
            print("Categoria: ", c)
            return a, b, c
    @staticmethod
    def guardar(a, b, c):
            with open("Archivo.txt", "a") as archivo:
                archivo.write("Datos de: ")
                archivo.write(a + ", ")
                archivo.write(b + ", ")
                archivo.write(c + "\n")

    @staticmethod
    def buscar(a):
            with open("Archivo.txt", "r") as archivo:
                lineas = archivo.readlines()
                for linea in lineas:
                    if a in linea:
                        print("Encontrado:", linea)
    def menu(self):
            while True:
                print("Selecciona una opcion")
                print("1. Añadir")
                print("2. Buscar")
                print("3. Cancelar")
                seleccion = input("Selecciona una opcion: ")
                if seleccion == "1":
                    nombre = input("Ingrese su nombre: ")
                    numero = input("Ingrese su numero: ")
                    categoria = input("Ingrese su categoria: ")
                    self.añadir(nombre, numero, categoria)
                    self.guardar(nombre, numero, categoria)
                elif seleccion == "2":
                    busqueda = input("Nombre del contacto: ")
                    self.buscar(busqueda)
                    break
                elif seleccion == "3":
                    break
                else:
                    print("Opcion no valida")

directorio = DirectorioTelefonico()
directorio.menu()