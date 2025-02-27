<<<<<<< HEAD
import pandas as pd
from sqlalchemy import create_engine
engine = create_engine("sqlite:///Datos")

class DirectorioTelefonico:
    def _init_(self):
        pass

    @staticmethod
    def guardar(a, b, c):
        df = pd.DataFrame({"Nombres": [a], "Numero": [b], "Categoria": [c]})
        df.to_sql("DatosTelefonicos", con=engine, if_exists='append', index=False)
        print(df)

    @staticmethod
    def buscar(a):
        query = f"SELECT * FROM DatosTelefonicos WHERE Nombres = '{a}'"
        resultado = pd.read_sql(query, con=engine)
        if not resultado.empty:
            print(resultado)
        else:
            print("No se encontró ningún resultado.")

    @staticmethod
    def leerpandas():
        df = pd.read_sql("SELECT * FROM DatosTelefonicos", con=engine)
        print(df)
=======
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
>>>>>>> dab677fb58551f2f916d636c731de72c27c458f2

    def menu(self):
        while True:
            print("Selecciona una opcion")
            print("1. Añadir")
            print("2. Buscar")
            print("3. Datos")
            print("4. Cancelar")
            seleccion = input("Selecciona una opcion: ")
            if seleccion == "1":
                nombre = input("Ingrese su nombre: ").lower()
                numero = input("Ingrese su numero: ")
<<<<<<< HEAD
                categoria = input("Ingrese su categoria: ").upper()
=======
                categoria = input("Ingrese su categoria: ").lower()
>>>>>>> dab677fb58551f2f916d636c731de72c27c458f2
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