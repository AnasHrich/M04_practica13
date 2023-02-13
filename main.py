from animal import animal
from vehicle import vehicle
from school import school

animal1 = animal("Tigre", 100, 1.2, "felino", "naranja", "España")
animal1.Salutacio()
print(animal1)
animal1.setPaisOrigen("India")
print(animal1)

vehicle1 = vehicle("Renault", 1500, 3.4, "Negro", "Mercedes-Benz", "CLA 200d")
vehicle1.Salutacio2()
print(vehicle1)
vehicle1.setMotor("Mercedez")
vehicle1.Salutacio2()
print(vehicle1)

school1 = school("Jaume Balmes", "Miguel", 820, "Pau Claris", "Barcelona", 195)
school1.Salutacio3()
print(school1)
school1.setNomDirector("Jaume")
print(school1)