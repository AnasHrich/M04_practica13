class vehicle:
    def __init__(self, motor, peso, largo, color, marca, modelo):
        self.motor = motor
        self.peso = peso
        self.largo = largo
        self.color = color
        self.marca = marca
        self.modelo = modelo

    def getMotor(self):
        return self.motor

    def setMotor(self, motor):
        self.motor = motor
    def getPeso(self):
        return self.peso

    def setPeso(self, peso):
        self.peso = peso
    def getLargo(self):
        return self.largo

    def setLargo(self, largo):
        self.largo = largo
    def getColor(self):
        return self.color

    def setColor(self, color):
        self.color = color
    def getMarca(self):
        return self.marca

    def setMarca(self, marca):
        self.marca = marca
    def getModelo(self):
        return self.modelo

    def setModelo(self, modelo):
        self.modelo = modelo

    def Salutacio2(self):
        print(f"El motor es de la marca: {self.motor}")
        print(f"El peso del coche es de {self.peso}")
        print(f"El largo del coche es de {self.largo}")
        print(f"El color del coche es: {self.color}")
        print(f"La marca del coche es: {self.marca}")
        print(f"El modelo del coche es: {self.modelo}")