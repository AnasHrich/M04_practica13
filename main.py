from book import book
from user import user
from university import university

book1 = book ("Anas Hirch", "Atomic Habits", 2018, 216, 17, 0.5)
book1.information()
print(book1)

user1 = user ("Anas", 22, "anas.hrich@gmail.com", "Barcelona Spain", 644622273, "homme")
book1.salutacion()
print(user1)

university1 = university ("JaumeBalmes", "Barcelona", "Spain", 2000, "Anas", "CampusSpain")
university1.info()
print(university1)