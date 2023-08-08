#1-Cree una clase Vehículo que contenga los atributos de instancia velocidad_maxima y kilometraje.
class Vehículo:
    def __init__(self, velocidad_maxima, kilometraje):
        self.velocidad_maxima = velocidad_maxima
        self.kilometraje = kilometraje


mi_auto = Vehículo(200, 50000)
print("Velocidad máxima:", mi_auto.velocidad_maxima)
print("Kilometraje:", mi_auto.kilometraje)

#2-Cree una clase Punto que represente un punto en el plano cartesiano.
class Punto:
    def __init__(self, x, y):
        self.x = x
        self.y = y


punto1 = Punto(3, 5)
punto2 = Punto(-2, 7)

print("Punto 1 - Coordenadas:", punto1.x, punto1.y)
print("Punto 2 - Coordenadas:", punto2.x, punto2.y)
#3-A la clase del punto anterior, defínale los siguientes métodos:
#- Un método mostrar que imprima por consola las coordenadas del punto
#- Un método mover que cambie las coordenadas del punto
#- Un método calcular_distancia que calcule la distancia de la instancia actual con otro punto.
import math


class Punto:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def mostrar(self):
        print(f"Coordenadas: ({self.x}, {self.y})")

    def mover(self, nueva_x, nueva_y):
        self.x = nueva_x
        self.y = nueva_y

    def calcular_distancia(self, otro_punto):
        distancia = math.sqrt((self.x - otro_punto.x) ** 2 + (self.y - otro_punto.y) ** 2)
        return distancia


punto1 = Punto(3, 5)
punto2 = Punto(-2, 7)

punto1.mostrar()
punto2.mostrar()

punto1.mover(1, 1)
punto1.mostrar()

distancia = punto1.calcular_distancia(punto2)
print("Distancia entre punto1 y punto2:", distancia)

#4-Cree una clase Rectángulo la cual contiene dos atributos de instancia que representan los puntos que definen sus esquinas. Agregue métodos a la clase Rectángulo para calcular su perímetro, calcular su área e indicar si el rectángulo es un cuadrado.
class Punto:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Rectángulo:
    def __init__(self, esquina_sup_izq, esquina_inf_der):
        self.esquina_sup_izq = esquina_sup_izq
        self.esquina_inf_der = esquina_inf_der

    def calcular_perímetro(self):
        base = abs(self.esquina_inf_der.x - self.esquina_sup_izq.x)
        altura = abs(self.esquina_inf_der.y - self.esquina_sup_izq.y)
        return 2 * (base + altura)

    def calcular_area(self):
        base = abs(self.esquina_inf_der.x - self.esquina_sup_izq.x)
        altura = abs(self.esquina_inf_der.y - self.esquina_sup_izq.y)
        return base * altura

    def es_cuadrado(self):
        base = abs(self.esquina_inf_der.x - self.esquina_sup_izq.x)
        altura = abs(self.esquina_inf_der.y - self.esquina_sup_izq.y)
        return base == altura


esquina_sup_izq = Punto(1, 4)
esquina_inf_der = Punto(6, 1)
rectangulo = Rectángulo(esquina_sup_izq, esquina_inf_der)

print("Perímetro:", rectangulo.calcular_perímetro())
print("Área:", rectangulo.calcular_area())
print("¿Es cuadrado?", rectangulo.es_cuadrado())

#5-Cree una clase Circulo que tenga las propiedades centro y radio, las cuales se inicializan con parámetros en el constructor. Defina métodos en la clase para calcular el área, el perímetro e indicar si un punto pertenece al círculo o no.
import math


class Punto:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Circulo:
    def __init__(self, centro, radio):
        self.centro = centro
        self.radio = radio

    def calcular_area(self):
        return math.pi * self.radio ** 2

    def calcular_perimetro(self):
        return 2 * math.pi * self.radio

    def punto_pertenece(self, punto):
        distancia_centro_punto = math.sqrt((punto.x - self.centro.x) ** 2 + (punto.y - self.centro.y) ** 2)
        return distancia_centro_punto <= self.radio


centro = Punto(0, 0)
circulo = Circulo(centro, 5)

print("Área:", circulo.calcular_area())
print("Perímetro:", circulo.calcular_perimetro())

punto1 = Punto(3, 4)
punto2 = Punto(7, 2)

print("¿Punto 1 pertenece al círculo?", circulo.punto_pertenece(punto1))
print("¿Punto 2 pertenece al círculo?", circulo.punto_pertenece(punto2))
