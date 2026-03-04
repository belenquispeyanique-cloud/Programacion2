import math

class EcuacionCuadratica:
    def __init__(self, a, b, c):
        self.__a = a
        self.__b = b
        self.__c = c
    def getDiscriminante(self):
        discriminante = pow(self.__b, 2)-(4*self.__a*self.__c)
        return discriminante
    def getRaiz1(self):
        if self.getDiscriminante() < 0:
            return 0
        else:
            r1 =  ((- self.__b) + math.sqrt(self.getDiscriminante())) / (2 *self.__a)
            return r1
    def getRaiz2(self):
        if self.getDiscriminante() < 0:
            return 0
        else: 
            r2 = ((- self.__b) - math.sqrt(self.getDiscriminante())) / (2 * self.__a)
            return r2
class Main():
    a= float(input("a: "))
    b= float(input("b: "))
    c= float(input("c: "))
    ecuacion = EcuacionCuadratica   ( a, b, c)
    if(ecuacion.getDiscriminante() > 0):
        print(ecuacion.__str__())
    elif(ecuacion.getDiscriminante() == 0):
        print(f"La ecuacion  tiene una raiz {ecuacion.getRaiz1():.0f}")
    else:
        print("la ecuacion no tiene racices reales")

