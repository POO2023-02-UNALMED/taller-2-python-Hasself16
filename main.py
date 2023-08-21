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
    
    def cantidadAsientos(self):
        count = 0
        for asiento in self.asientos:
            if isinstance(asiento, Asiento):
                count += 1
        return count 
    
    def verificarIntegridad(self):
        registros = [self.registro]
        for asiento in self.asientos:
            registros.append(asiento.registro)
        registros.append(self.motor.registro)
        
        if all(registro == registros[0] for registro in registros):
            return "Auto original"
        else:
            return "Las piezas no son originales"
    