import math

class Estadistica:
    def __init__(self, x):
        self.__datos = x

    def promedio(self):
        n = len(self.__datos)
        suma = 0
        for i in range(n):
            suma = suma + self.__datos[i]
        return(suma)/(n)
    def desviacion(self):
        n = len(self.__datos)
        suma = 0 
        promedio = self.promedio()
        for i in range(n):
            suma = suma +pow ((self.__datos[i] - promedio), 2)
            return math.sqrt(suma / (n-1))

    def __str__(self):
        return f"El promedio es {self.promedio():.2f} \nLa desviacio estandar es {self.desviacion():.5f}"
class Main():
    num = []
    for i in range(10):
        x = float(input("x_"+str(i+1)+":"))
        num.append(x)
    calculo = Estadistica(num)
    print(calculo.__str__()) 