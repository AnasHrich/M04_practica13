class animal:
    def __init__(self, nombre, peso, altura, tipo, color, paisOrigen):
        self.nombre = nombre
        self.peso = peso
        self.altura = altura
        self.tipo = tipo
        self.color = color
        self.paisOrigen = paisOrigen

    def getNombre(self):
        return self.nombre
    def setNombre(self, nombre):
        self.nombre = nombre
    def getPeso(self):
        return self.peso
    def setPeso(self, peso):
        self.peso = peso
    def getAltura(self):
        return self.altura
    def setAltura(self, altura):
        self.altura = altura
    def getTipo(self):
        return self.tipo
    def setTipo(self, tipo):
        self.tipo = tipo
    def getColor(self):
        return self.color
    def setColor(self, color):
        self.color = color
    def getPaisOrigen(self):
        return self.paisOrigen
    def setPaisOrigen(self, paisOrigen):
        self.paisOrigen = paisOrigen

    def Salutacio(self):
        print(f"El nombre del animal es: {self.nombre}")
        print(f"El peso del animal es: {self.peso}")
        print(f"La altura del animal es: {self.altura}")
        print(f"El tipo de animal es: {self.tipo}")
        print(f"El color del animal es: {self.color}")
        print(f"El pais de origen es: {self.paisOrigen}")