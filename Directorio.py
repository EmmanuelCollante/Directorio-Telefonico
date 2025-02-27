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
                categoria = input("Ingrese su categoria: ").upper()
                self.guardar(nombre, numero, categoria)
            elif seleccion == "2":
                busqueda = input("Nombre del contacto: ")
                self.buscar(busqueda)
            elif seleccion == "3":
                self.leerpandas()
            elif seleccion == "4":
                break
            else:
                print("Opcion no valida")

directorio = DirectorioTelefonico()
directorio.menu()