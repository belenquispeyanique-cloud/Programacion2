class EcuacionLineal:
    def __init__(self,a,b,c,d,e,f):
        self.__a=a
        self.__b=b
        self.__c=c
        self.__d=d
        self.__e=e
        self.__f=f
    def tieneSolucion(self):
        x=(self.__a * self.__d) -(self.__b * self.__c)
        if x != 0.0:
            return True
        else:
            return False
    def getX(self):
        if self.tieneSolucion():
            x = ((self.__e*self.__d5)-(self.__b*self.__f))/((self.__a*self.__d)-(self.__b*self.__c))
            return x
    def getY(self):
        if self.tieneSolucion():
            y = ((self.__a*self.__f)-( self.__e*self.__c))/((self.__a*self.__d)-(self.__b*self.__c))
            return y
        else:
            return False
class Main ():
    a = int(input("a:"))
    b = int(input("b:"))
    c = int(input("c:"))
    d = int(input("d:"))
    e = int(input("e:"))
    f = int(input("f:"))
    ecuacion = EcuacionLineal( a, b, c, d, e, f)
    if(ecuacion.tieneSolucion()):
        print("x: ",ecuacion.getX(), end=", ")
        print("y: ",ecuacion.getY(), end=", ")
    else:
        print("la ecuacion no tiene solucion")
