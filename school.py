class school:
    def __init__(self, nombreCentro, nomDirector, alumnos, nombreCalle, nomCiudad, año):
        self.nombreCentro = nombreCentro
        self.nomDirector = nomDirector
        self.alumnos = alumnos
        self.nombreCalle = nombreCalle
        self.nomCiudad = nomCiudad
        self.año = año

    def getnombreCentro(self):
        return self.nombreCentro

    def setNombreCentro(self, nombreCentro):
        self.nombreCentro = nombreCentro
    def getNomDirector(self):
        return self.nomDirector

    def setNomDirector(self, nomDirector):
        self.nomDirector = nomDirector
    def getAlumnos(self):
        return self.alumnos

    def setAlumnos(self, alumnos):
        self.alumnos = alumnos
    def getNombreCalle(self):
        return self.nombreCalle

    def setNombreCalle(self, nombreCalle):
        self.nombreCalle = nombreCalle
    def getNomCiudad(self):
        return self.nomCiudad

    def setNomCiudad(self, nomCiudad):
        self.nomCiudad = nomCiudad
    def getAño(self):
        return self.año

    def setAño(self, año):
        self.año = año

    def Salutacio3(self):
        print(f"El nombre del centro es: {self.nombreCentro}")
        print(f"El nombre del director es: {self.nomDirector}")
        print(f"En el centro hay {self.alumnos} alumnos")
        print(f"El nombre de calle es: {self.nombreCalle}")
        print(f"El centro está en la ciudad de {self.nomCiudad}")
        print(f"El centro tiene {self.año} años")