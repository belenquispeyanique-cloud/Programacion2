class Instrumento():
    def __init__(self, nombre, material, tipo):
        self.nombre = nombre    
        self.__material = material
        opc = ["cuerda","aire"]
        if tipo in opc:
            self.__tipo = tipo
        else:
            self.__tipo = "desconocido"
    
    def toString(self):
        return "Instrumento: Nombre: "+self.nombre+", Material: "+self.__material+", Tipo: "+self.__tipo

    def getNombre(self):
        return self.nombre
    
    def getMaterial(self):
        return self.__material
    
    def getTipo(self):
        return self.__tipo
    
    def setNombre(self, nombre):
        self.nombre = nombre
    
    def setMaterial(self, material):
        self.__material = material

    def setTipo(self, tipo):
        opc = ["cuerda","aire"]
        if tipo in opc:
            self.__tipo = tipo
        else:
            self.__tipo = "desconocido"

class Main():
    ins1 = Instrumento("guitarra","madera","cuerda")
    print(ins1.toString())

    ins2 = Instrumento("trompeta", "laton", "aire")
    print(ins2.toString())
