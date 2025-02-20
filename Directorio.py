import pandas as pd
import os

class DirectorioTelefonico:
    def __init__(self):
        pass

    @staticmethod
    def guardar(a, b, c):
        archivo_existe = os.path.exists("Archivo.csv")
        df = pd.DataFrame({"Nombres": [a], "Numero": [b], "Categoria": [c]})
        if archivo_existe:
            df.to_csv("Archivo.csv", mode='a', header=False, index=False)
        else:
            df.to_csv("Archivo.csv", mode='w', header=True, index=False)
        print(df)

    @staticmethod
    def buscar(a):
        with open("Archivo.csv", "r") as archivo:
            lineas = archivo.readlines()
            for linea in lineas:
                if a in linea:
                    print("Encontrado:", linea)

    @staticmethod
    def leerpandas():
        data = pd.read_csv("Archivo.csv", delimiter='[,]', engine='python')
        print(data)

    def menu(self):
        while True:
            print("Selecciona una opcion")
            print("1. Añadir")
            print("2. Buscar")
            print("3. Datos")
            print("4. Cancelar")
            seleccion = input("Selecciona una opcion: ")
            if seleccion == "1":
                nombre = input("Ingrese su nombre: ")
                numero = input("Ingrese su numero: ")
                categoria = input("Ingrese su categoria: ")
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
