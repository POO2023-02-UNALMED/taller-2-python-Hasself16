class Asiento:
    def __init__(self, color, precio, registro):
        self.color=color
        self.precio=precio
        self.registo=registro

    def cambiarColor(self, color):
        colores=["rojo", "verde", "amarillo", "negro", "blanco"]
        if color in colores:
            self.color = color

class Motor:
    def __init__(self, numeroCilindros, tipo, registro):
        self.numeroCilindros=numeroCilindros
        self.tipo=tipo
        self.registro=registro
    
    def cambiarRegistro(self, registro):
        self.registro= registro
    
    def asignarTipo(self, tipo):
        tipos=["electrico", "gasolina"]
        if tipo in tipos:
            self.tipo=tipo
            
class Auto:
    cantidadCreados=0
    def __init__(self, modelo, precio, asientos, marca, motor, registro):
        self.modelo=modelo
        self.precio=precio
        self.asientos=asientos
        self.marca=marca
        self.motor=motor
        self.registro=registro
    
    def verificarIntegridad(self):
        if (self.registro == self.motor.registro) and (self.registro==Asiento.registro):
            return("Auto original")
        else:
            return("Las piezas no son originales")
    