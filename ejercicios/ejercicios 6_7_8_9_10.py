#6-Cree una clase Carta que contenga dos propiedades valor y pinta, las cuales son asignadas solo al momento de la construcción del objeto (se pasan como parámetros en el constructor). Defina 4 constantes que representan los nombres de las 4 pintas que puede tener una carta.
class Carta:
    def __init__(self, valor, pinta):
        self.valor = valor
        self.pinta = pinta

class Pinta:
    CORAZON = "Corazón"
    DIAMANTE = "Diamante"
    TREBOL = "Trébol"
    ESPADA = "Espada"


carta1 = Carta(7, Pinta.CORAZON)
carta2 = Carta(10, Pinta.ESPADA)

print("Carta 1 - Valor:", carta1.valor, "- Pinta:", carta1.pinta)
print("Carta 2 - Valor:", carta2.valor, "- Pinta:", carta2.pinta)


#7-Cree una clase CuentaBancaria que contenga los siguientes atributos: numero_cuenta, propietarios y balance. Los tres atributos se deben inicializar en el constructor con valores recibidos como parámetros.
class CuentaBancaria:
    def __init__(self, numero_cuenta , propietarios , balance ):
        self.numero_cuenta = numero_cuenta
        self.propietarios = propietarios
        self.balance = balance

cuenta = CuentaBancaria("123456789", ["Juan", "María"], 5000.0)

print("Número de cuenta:", cuenta.numero_cuenta)
print("Propietarios:", cuenta.propietarios)
print("Balance:", cuenta.balance)

#8-Para la clase CuentaBancaria, cree un método depositar que maneje las acciones de depósito en la cuenta.
class CuentaBancaria:
    def __init__(self, numero_cuenta, propietarios, balance):
        self.numero_cuenta = numero_cuenta
        self.propietarios = propietarios
        self.balance = balance

    def depositar(self, monto):
        if monto > 0:
            self.balance += monto
            print(f"Se depositó ${monto} en la cuenta. Nuevo balance: ${self.balance}")
        else:
            print("El monto de depósito debe ser mayor que cero.")


cuenta = CuentaBancaria("123456789", ["Juan", "María"], 5000.0)

print("Balance antes del depósito:", cuenta.balance)
cuenta.depositar(1000.0)
print("Balance después del depósito:", cuenta.balance)

#9-Para la clase CuentaBancaria, cree un método retirar que maneje las acciones de retiro de la cuenta.
class CuentaBancaria:
    def __init__(self, numero_cuenta, propietarios, balance):
        self.numero_cuenta = numero_cuenta
        self.propietarios = propietarios
        self.balance = balance

    def depositar(self, monto):
        if monto > 0:
            self.balance += monto
            print(f"Se depositó ${monto} en la cuenta. Nuevo balance: ${self.balance}")
        else:
            print("El monto de depósito debe ser mayor que cero.")

    def retirar(self, monto):
        if 0 < monto <= self.balance:
            self.balance -= monto
            print(f"Se retiró ${monto} de la cuenta. Nuevo balance: ${self.balance}")
        else:
            print("El monto de retiro es inválido o excede el balance.")



cuenta = CuentaBancaria("123456789", ["Juan", "María"], 5000.0)

print("Balance antes del retiro:", cuenta.balance)
cuenta.retirar(2000.0)
print("Balance después del retiro:", cuenta.balance)
