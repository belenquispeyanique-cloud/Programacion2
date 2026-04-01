import math

class Punto2D:
    def __init__(self, x=0.0, y=0.0):
        self._x = x
        self._y = y

    def getX(self):
        return self._x

    def getY(self):
        return self._y

    def distanciaOrigen(self):
        return math.hypot(self._x, self._y)

    def distanciaPunto(self, otro):
        return math.hypot(self._x - otro.getX(), self._y - otro.getY())

    def __str__(self):
        return f"({self._x}, {self._y})"


p1 = Punto2D(4, 7)
p2 = Punto2D(-3, 2)

d1 = p1.distanciaOrigen()
d2 = p2.distanciaOrigen()
d3 = p1.distanciaPunto(p2)

print("P1:", p1)
print("P2:", p2)
print("Distancia P1 al origen:", round(d1, 2))
print("Distancia P2 al origen:", round(d2, 2))
print("Distancia entre P1 y P2:", round(d3, 2))