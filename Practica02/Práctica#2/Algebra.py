import math

class Vector2D:
    def __init__(self, x=0.0, y=0.0):
        self._x = float(x)
        self._y = float(y)

    def getX(self):
        return self._x

    def getY(self):
        return self._y

    def __add__(self, v):
        return Vector2D(self._x + v.getX(), self._y + v.getY())

    def __sub__(self, v):
        return Vector2D(self._x - v.getX(), self._y - v.getY())

    def __mul__(self, v):
        return self._x * v.getX() + self._y * v.getY()

    def __xor__(self, v):
        return self._x * v.getY() - self._y * v.getX()

    def __abs__(self):
        return math.hypot(self._x, self._y)

    def norma(self):
        return abs(self)

    def __str__(self):
        return f"[{self._x:.1f}, {self._y:.1f}]"


class OperacionesVector:
    def __init__(self, u, v):
        self._u = u
        self._v = v

    def perpendicular(self, modo=1):
        u = self._u
        v = self._v

        if modo == 1:
            return abs(u * v) == 0
        elif modo == 2:
            return abs((u + v).norma()**2 - (u.norma()**2 + v.norma()**2)) == 0
        elif modo == 3:
            return abs((u + v).norma() - (u - v).norma()) == 0

    def paralelo(self, modo=1):
        u = self._u
        v = self._v

        if modo == 1:
            return abs(u ^ v) == 0
        elif modo == 2:
            if v.getX() != 0:
                k = u.getX() / v.getX()
                return abs(u.getY() - k * v.getY()) == 0
            elif v.getY() != 0:
                k = u.getY() / v.getY()
                return abs(u.getX() - k * v.getX()) == 0
            return False

    def proy(self):
        u = self._u
        v = self._v
        k = (u * v) / (abs(v)**2)
        return Vector2D(v.getX() * k, v.getY() * k)

    def comp(self):
        u = self._u
        v = self._v
        return (u * v) / abs(v)


v1 = Vector2D(3, 6)
v2 = Vector2D(1.5, 3)

op = OperacionesVector(v1, v2)

print("v1:", v1)
print("v2:", v2)

print("Perpendicular:", op.perpendicular(1))
print("Paralelo:", op.paralelo(1))
print("Proyección:", op.proy())
print("Componente:", round(op.comp(), 2))