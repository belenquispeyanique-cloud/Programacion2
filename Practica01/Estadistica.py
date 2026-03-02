import math
def promedio(datos):
    suma = 0
    for i in range (len(datos)):
        suma +=datos[i]
    return suma / len(datos)

def desviacion(datos):
    prom = promedio(datos)
    suma=0
    for i in range(len(datos)):
        suma +=(datos[i]- prom)**2
    return math.sqrt(suma / (len(datos) -1))

def main():
    numeros =[]
    for i in range(10):
        numero = float(input("x_" + str(i+1)+ ":"))
        numeros.append(numero)
    prom = promedio(numeros)
    desv = desviacion(numeros)
    print("el promedio es {:.2}".format(prom))
    print("la desviacion estandar es {:.5f}".format(desv))

main()