import pandas as pd
from sqlalchemy import create_engine
engine = create_engine("sqlite:///Datos")

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
        df = pd.DataFrame({"Nombres": [a], "Numero": [b], "Categoria": [c]})
        df.to_sql("DatosTelefonicos", con=engine, if_exists='append', index=False)
        nuevo = Contacto(a, b, c)
        self.contactos.append(nuevo)
        print(f"Contacto guardado: Nombre: {a}, Telefono: {b}, Categoria: {c}")
        print(df)

    def buscar(self, nombre):
        # Buscar en la base de datos
        query = f"SELECT * FROM DatosTelefonicos WHERE Nombres = '{nombre}'"
        resultado = pd.read_sql(query, con=engine)
        if not resultado.empty:
            print(resultado)
        else:
            # Buscar en la lista de contactos
            for c in self.contactos:
                if c.nombre.lower() == nombre.lower():
                    print(f"Nombre: {c.nombre}, Telefono: {c.numero}, Categoria: {c.categoria}")
                    return
            print("Contacto no encontrado.")

