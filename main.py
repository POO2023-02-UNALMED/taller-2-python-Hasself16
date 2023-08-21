class Asiento:
    def __init__(self, color, precio, registro):
        self.color=color
        self.precio=precio
        self.registo=registro

    def cambiarColor(self, color):
        colores=["rojo", "verde", "amarillo", "negro", "blanco"]
        color=input()
        if color not in colores:
            print("No se puede poner este color")
        else:
            self.color = color
            print(f"El color ha cambiado a {self.color}")

class Motor:
    def __init__(self, numeroCilindros, tipo, registro):
        self.numeroCilindros=numeroCilindros
        self.tipo=tipo
        self.registro=registro
    
    def cambiarRegistro(self, registro):
        registro=int(input())
        self.registro= registro
    
    def asignarTipo(self, tipo):
        tipos=["electrico", "gasolina"]
        tipo=input()
        if tipo not in tipos:
            print("No se puede cambiar a este tipo.")
        else:
            self.tipo=tipo

class Auto:
    cantidadCreados=3
    def __init__(self, modelo, precio, asientos, marca, motor, registro, cantidadCreados):
        self.modelo=modelo
        self.precio=precio
        self.asientos=Asiento
        self.marca=marca
        self.motor=motor
        self.registro=registro
        self.cantidadCreados= cantidadCreados
