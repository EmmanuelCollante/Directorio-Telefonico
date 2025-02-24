class Contacto:
    def __init__(self, nombre, numero, categoria):
        self.nombre = nombre
        self.numero = numero
        self.categoria = categoria

    def __str__(self):
        return f"Nombre: {self.nombre}, Telefono: {self.numero}, Categoria: {self.categoria}"

class DirectorioTelefonico:
    def __init__(self):
        self.contactos = []  # Inicializar la lista de contactos

    def guardar(self, a, b, c):
        nuevo = Contacto(a, b, c)
        self.contactos.append(nuevo)
        print(f"Contacto guardado: Nombre: {a}, Telefono: {b}, Categoria: {c}")

    def buscar(self, nombre):
        for c in self.contactos:
            if c.nombre.lower() == nombre.lower():
                print(f"Nombre: {c.nombre}, Telefono: {c.numero}, Categoria: {c.categoria}")
                return
        print("Contacto no encontrado.")

    def leerdatos(self):
        if self.contactos:
            print("Contactos guardados:")
            for c in self.contactos:
                print(c)  # Utiliza el método __str__ para imprimir el objeto
        else:
            print("No hay contactos guardados.")

    def menu(self):
        while True:
            print("Selecciona una opcion")
            print("1. Añadir")
            print("2. Buscar")
            print("3. Datos")
            print("4. Cancelar")
            seleccion = input("Selecciona una opcion: ")
            if seleccion == "1":
                nombre = input("Ingrese su nombre: ").lower()
                numero = input("Ingrese su numero: ")
                categoria = input("Ingrese su categoria: ").lower()
                self.guardar(nombre, numero, categoria)
            elif seleccion == "2":
                busqueda = input("Nombre del contacto: ").lower()
                self.buscar(busqueda)
            elif seleccion == "3":
                self.leerdatos()
            elif seleccion == "4":
                break
            else:
                print("Opcion no valida")

# Crear una instancia de DirectorioTelefonico
directorio = DirectorioTelefonico()
directorio.menu()
