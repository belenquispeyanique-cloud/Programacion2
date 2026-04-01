import math

class Vector:
    def __init__(self, x=0.0, y=0.0, z=0.0):
        self._x = float(x)
        self._y = float(y)
        self._z = float(z)

    def getX(self):
        return self._x

    def getY(self):
        return self._y

    def getZ(self):
        return self._z

    def __add__(self, v):
        return Vector(
            self._x + v.getX(),
            self._y + v.getY(),
            self._z + v.getZ()
        )

    def suma(self, v):
        return self + v

    def __mul__(self, v):
        if isinstance(v, (int, float)):
            return Vector(
                self._x * v,
                self._y * v,
                self._z * v
            )
        return (
            self._x * v.getX() +
            self._y * v.getY() +
            self._z * v.getZ()
        )

    def __rmul__(self, v):
        return self * v

    def punto(self, v):
        return self * v

    def __xor__(self, v):
        return Vector(
            self._y * v.getZ() - self._z * v.getY(),
            self._z * v.getX() - self._x * v.getZ(),
            self._x * v.getY() - self._y * v.getX()
        )

    def cruz(self, v):
        return self ^ v

    def escalar(self, k):
        return self * k

    def modulo(self):
        return math.sqrt(self._x**2 + self._y**2 + self._z**2)

    def unitario(self):
        m = self.modulo()
        return Vector(self._x/m, self._y/m, self._z/m)

    def __str__(self):
        return f"[{self._x:.1f}, {self._y:.1f}, {self._z:.1f}]"


v1 = Vector(3, -2, 5)
v2 = Vector(1, 4, -1)

print("v1:", v1)
print("v2:", v2)
print("Suma:", v1.suma(v2))
print("Producto punto:", round(v1.punto(v2), 2))
print("Producto cruz:", v1.cruz(v2))
print("Escalar 3*v1:", v1.escalar(3))
print("Modulo v1:", round(v1.modulo(), 2))
print("Vector unitario v1:", v1.unitario())