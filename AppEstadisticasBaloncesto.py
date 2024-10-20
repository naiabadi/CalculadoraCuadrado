import pandas as pd

class Tiros:
    def __init__(self, **kwargs):
        self.__tiros = {
            "T3": kwargs.get("T3", [0, 0]),
            "Tlibres": kwargs.get("Tlibres", [0, 0]),
            "T2": kwargs.get("T2", [0, 0]),
        }

    @property
    def tiros(self):
        return self.__tiros
    @tiros.setter
    def tiros(self, tipo, valores):
        if tipo not in self.__tiros:
            raise ValueError(f"El tipo de tiro '{tipo}' no es válido. Opciones: {list(self.__tiros.keys())}")
        self.__tiros = {tipo: valores}

    def tirosdecampo(self):
        tiros = [0, 0]
        tiros[0] = self.__tiros["T3"][0] + self.__tiros["T2"][0]
        tiros[1] = self.__tiros["T3"][1] + self.__tiros["T2"][1]
        return tiros

    def puntos(self):
        return 3 * self.__tiros["T3"][1] + 2 * self.__tiros["T2"][1] + self.__tiros["Tlibres"][1]

    def calcular_porcentajes(self,a,b):
        c=0.0
        try:
            c=a/b
        except ZeroDivisionError:
            c=0.0
        return round(c*100,2)

    def porcentajes(self):
        triples = self.calcular_porcentajes(self.__tiros["T3"][1],self.__tiros["T3"][0])
        dedos = self.calcular_porcentajes(self.__tiros["T2"][1],self.__tiros["T2"][0])
        libres = self.calcular_porcentajes(self.__tiros["Tlibres"][1],self.__tiros["Tlibres"][0])
        decampo = self.calcular_porcentajes(self.tirosdecampo()[1],self.tirosdecampo()[0])
        return {
            "Tiros libres": libres,
            "Tiros de dos": dedos,
            "Triples": triples,
            "Tiros de campo": decampo,
        }

    def mostrar_tiros_intentados(self):
        return {
            "Tiros libres": self.__tiros["Tlibres"][0],
            "Triples": self.__tiros["T3"][0],
            "Tiros de dos": self.__tiros["T2"][0],
            "Tiros de campo": self.tirosdecampo()[0]
        }
    def mostrar_tiros_anotados(self):
        return {
            "Tiros libres": self.__tiros["Tlibres"][1],
            "Triples": self.__tiros["T3"][1],
            "Tiros de dos": self.__tiros["T2"][1],
            "Tiros de campo": self.tirosdecampo()[1]
        }


class Defensa:
    def __init__(self, **kwargs):
        self.__defensa = {
            "tapones": kwargs.get("tapones", 0),
            "robos": kwargs.get("robos", 0),
            "rebotes": kwargs.get("rebotes", 0),
        }

    @property
    def defensa(self):
        return self.__defensa

    @defensa.setter
    def defensa(self, tipo, valor):
        if tipo not in self.__defensa:
            raise ValueError(f"El dato '{tipo}' no es válido. Opciones: {list(self.__defensa.keys())}")
        if valor < 0:
            print(f"La cantidad mínima de {tipo} es 0")
            valor = 0
        self.__defensa[tipo] = valor
    def set_defensa(self, tipo, valor):
        self.defensa = {tipo: valor}

    def mostrar_defensa(self):
        return {
            "Tapones": self.__defensa["tapones"],
            "Robos": self.__defensa["robos"],
            "Rebotes": self.__defensa["rebotes"],
        }

class Estadisticas(Tiros, Defensa):
    def __init__(self, nombre="",minutos=0.0, partido=0.0, **kwargs):
        Tiros.__init__(self, **kwargs)
        Defensa.__init__(self, **kwargs)
        self.nombre = nombre
        self.partido = partido
        self.minutos = minutos
    @property
    def nombre(self):
        return self.__nombre

    @property
    def partido(self):
        return self.__partido

    @property
    def minutos(self):
        return self.__minutos

    @nombre.setter
    def nombre(self, nombre):
        self.__nombre = nombre

    @partido.setter
    def partido(self, partido):
        self.__partido = partido

    def validar_minutos(self):
        if self.__minutos < 0:
            print("La cantidad de minutos jugados debe ser mayor o igual que 0")
            self.__minutos = float(input("Introduzca los minutos jugados: "))
        elif self.__minutos > self.__partido:
            print("Los minutos jugados deben ser menores que el total de minutos del partido.")
            self.__minutos = float(input("Introduzca los minutos jugados: "))

    @minutos.setter
    def minutos(self, minutos):
        self.__minutos = minutos
        self.validar_minutos()

    def porminuto(self, dato):
        return round(dato / self.__minutos, 2)

    def proyeccion(self, dato):
        return round(self.porminuto(dato) * self.__partido, 2)

    def mostrarporminuto(self):
        tiros = self.mostrar_tiros_anotados()
        estadisticas = {
            "Puntos": self.porminuto(self.puntos()),
            "Tiros libres": self.porminuto(tiros["Tiros libres"]),
            "Tiros de dos": self.porminuto(tiros["Tiros de dos"]),
            "Triples": self.porminuto(tiros["Triples"]),
            "Tiros de campo": self.porminuto(tiros["Tiros de campo"]),
            "Tapones": self.porminuto(self.defensa["tapones"]),
            "Robos": self.porminuto(self.defensa["robos"]),
            "Rebotes": self.porminuto(self.defensa["rebotes"])
        }
        return estadisticas

    def mostrarproyeccion(self):
        tiros = self.mostrar_tiros_anotados()
        estadisticas = {
            "Puntos": self.proyeccion(self.puntos()),
            "Tiros libres": self.proyeccion(tiros["Tiros libres"]),
            "Tiros de dos": self.proyeccion(tiros["Tiros de dos"]),
            "Triples": self.proyeccion(tiros["Triples"]),
            "Tiros de campo": self.proyeccion(tiros["Tiros de campo"]),
            "Tapones": self.proyeccion(self.defensa["tapones"]),
            "Robos": self.proyeccion(self.defensa["robos"]),
            "Rebotes": self.proyeccion(self.defensa["rebotes"])
        }
        return estadisticas

    def mostrar(self):
        estadisticas = {
            "Puntos anotados": self.puntos(),
            "Tiros intentados": self.mostrar_tiros_intentados(),
            "Tiros anotados": self.mostrar_tiros_anotados(),
            "Estadisticas defensivas": self.mostrar_defensa(),
            "Porcentajes de tiro": self.porcentajes(),
            "Estadisticas por minuto": self.mostrarporminuto(),
            "Estadisticas que hubiese conseguido jugando el partido completo": self.mostrarproyeccion(),
        }
        return estadisticas

class Comparar(Estadisticas):
    def __init__(self,jugador1: Estadisticas,jugador2:Estadisticas):
        super().__init__()
        self.jugador1 = jugador1
        self.jugador2 = jugador2

    @property
    def jugador1(self):
        return self.__jugador1
    @jugador1.setter
    def jugador1(self,jugador1):
        self.__jugador1 = jugador1

    @property
    def jugador2(self):
        return self.__jugador2
    @jugador2.setter
    def jugador2(self,jugador2):
        self.__jugador2 = jugador2

    def anotacion(self):
        puntos_j1 = self.__jugador1.puntos()
        puntos_j2 = self.__jugador2.puntos()
        if puntos_j1 > puntos_j2:
            return f"{self.__jugador1.nombre} ha anotado más puntos"
        elif puntos_j1 < puntos_j2:
            return f"{self.__jugador2.nombre} ha anotado más puntos"
        else:
            return "Ambos jugadores han anotado la misma cantidad de puntos."

    def efectividad(self):
        porcentajes_j1 = self.__jugador1.porcentajes()
        porcentajes_j2 = self.__jugador2.porcentajes()
        comparacion = {}
        for tipo in porcentajes_j1.keys():
            if porcentajes_j1[tipo] > porcentajes_j2[tipo]:
                comparacion[tipo] = f"{self.__jugador1.nombre} es más efectivo"
            elif porcentajes_j1[tipo] < porcentajes_j2[tipo]:
                comparacion[tipo] = f"{self.__jugador2.nombre} es más efectivo"
            else:
                comparacion[tipo] = "Ambos son igual de efectivos"
        return comparacion

    def comparar_defensa(self):
        defensa1 = self.__jugador1.defensa
        defensa2 = self.__jugador2.defensa

        comparacion = {
            "tapones": None,
            "robos": None,
            "rebotes": None
        }

        for key in comparacion.keys():
            if defensa1[key] > defensa2[key]:
                comparacion[key] = f"{self.__jugador1.nombre} tiene más {key} que {self.__jugador2.nombre}"
            elif defensa1[key] < defensa2[key]:
                comparacion[key] = f"{self.__jugador2.nombre} tiene más {key} que {self.__jugador1.nombre}"
            else:
                comparacion[key] = f"Ambos tienen el mismo número de {key}"

        return comparacion


class Inicializador(Estadisticas):
    def __init__(self,df=None):
        super().__init__()
        self.df=df

    @property
    def df(self):
        return self.__df

    @df.setter
    def df(self, value):
        if value is None:
            raise ValueError("El dataframe no puede ser None.")
        if not isinstance(value, pd.DataFrame):
            raise TypeError("El valor asignado debe ser un pandas DataFrame.")
        self.__df = value

    def inicializar_jugador(self):
        while True:
            nombre = str(input("Introduze el nombre del jugador: "))
            try:
                jugador_fila = self.__df[self.__df['nombre'] == nombre]
                if jugador_fila.empty:
                    raise ValueError("Jugador no encontrado.")

                triples = [
                    int(jugador_fila["Triples intentados"].values[0]),
                    int(jugador_fila["Triples anotados"].values[0])
                ]

                libres = [
                    int(jugador_fila["Tiros libres intentados"].values[0]),
                    int(jugador_fila["Tiros libres anotados"].values[0])
                ]

                dedos = [
                    int(jugador_fila["Tiros de dos intentados"].values[0]),
                    int(jugador_fila["Tiros de dos anotados"].values[0])
                ]
                if triples[0]<triples[1]:
                    raise ValueError("Los triples intentados deben ser más que los triples anotados")
                if libres[0]<libres[1]:
                    raise ValueError("Los tiros libres intentados deben de ser más que los anotados")
                if dedos[0]<dedos[1]:
                    raise ValueError("Los tiros de dos intentados deben de ser más que los anotados")

                tap = int(jugador_fila["Tapones"].values[0])
                rob = int(jugador_fila["Robos"].values[0])
                reb = int(jugador_fila["Rebotes"].values[0])
                min = int(jugador_fila["Minutos"].values[0])
                prorrogas = int(jugador_fila["Prorrogas"].values[0])
                part = 40.0 + (5 * float(prorrogas))
                jugador = Estadisticas(nombre=nombre, minutos=min, partido=part, T3=triples, Tlibres=libres, T2=dedos,
                                    tapones=tap, robos=rob, rebotes=reb)
                return jugador
            except ValueError as e:
                print(f"Error: {e}. Intenta de nuevo.")
                continue

if __name__ == "__main__":
    print("Para utilizar esta aplicación tienes que proporcionar un fichero que contenga los datos de los jugadores de un equipo de baloncesto. Podras conseguir sus estadisticas y podras realizar la comparación entre dos jugadores.")
    print("Esta es la estructura que debe tener ese fichero:")
    print("nombre,Triples intentados,Triples anotados,Tiros libres intentados,Tiros libres anotados,Tiros de dos intentados,Tiros de dos anotados,Tapones,Robos,Rebotes,Minutos,Prorrogas")
    print("Jugador1,10,5,8,6,15,10,2,3,4,30,1")
    while True:
        archivo = str(input("Introduze el nombre de tu fichero (escribe su ruta e incluye la extensión .csv): "))
        try:
            df = pd.read_csv(archivo, sep=',')
            columnas_esperadas = ['nombre', 'triples intentados', 'triples anotados',
                                  'tiros libres intentados', 'tiros libres anotados',
                                  'tiros de dos intentados', 'tiros de dos anotados',
                                  'tapones', 'robos', 'rebotes', 'minutos', 'prorrogas']
            columnas_df = [col.lower().strip() for col in df.columns]
            if set(columnas_df) != set(columnas_esperadas):
                raise ValueError("Las columnas de tu fichero no son adecuadas.")
            break
        except ValueError as e:
            print(f"Error: {e}")
        except FileNotFoundError:
            print("El fichero no existe")
        except pd.errors.EmptyDataError:
            print("El fichero está vacío")
        except pd.errors.ParserError:
            print("Asegúrate de que esté en formato CSV correcto.")

    inicializador=Inicializador(df)
    while True:
        try:
            x=int(input("Si quieres conocer las estadisticas de un jugador escribe 1, si quieres comparar las estadisticas entre dos jugadores escribe 2, y para terminar escribe 3:"))
        except ValueError:
            print("Debes introduzir 1, 2 o 3:")
            continue

        if x == 1:
            jugador = inicializador.inicializar_jugador()
            for key in jugador.mostrar():
                print(f"{key}:")
                print(jugador.mostrar()[key])
        elif x == 2:
            try:
                jugador1 = inicializador.inicializar_jugador()
                while True:
                    try:
                        jugador2 = inicializador.inicializar_jugador()
                        if jugador1.nombre==jugador2.nombre:
                            raise ValueError("Has introduzido el mismo jugador, para comparar dos jugadores es necesario que sean distintos")
                        break
                    except ValueError as e:
                        print(f"Error: {e}")

                comparacion = Comparar(jugador1, jugador2)
                print("Comparación de ambos jugadores:")
                print(comparacion.anotacion())
                print("Efectividad en los tiros:",comparacion.efectividad())
                print(comparacion.comparar_defensa())
            except ValueError as e:
                print(f"Error: {e}")
                continue
        elif x == 3:
            break
