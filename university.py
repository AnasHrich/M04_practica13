class university:
    def __init__(self, name, city, country, established_year, student_population, campus_area):
        self.__name = name
        self.__city = city
        self.__country = country
        self.__established_year = established_year
        self.__student_population = student_population
        self.__campus_area = campus_area

    # Getters
    def get_name(self):
        return self.__name

    def get_city(self):
        return self.__city

    def get_country(self):
        return self.__country

    def get_established_year(self):
        return self.__established_year

    def get_student_population(self):
        return self.__student_population

    def get_campus_area(self):
        return self.__campus_area

    # Setters
    def set_name(self, name):
        self.__name = name

    def set_city(self, city):
        self.__city = city

    def set_country(self, country):
        self.__country = country

    def set_established_year(self, established_year):
        self.__established_year = established_year

    def set_student_population(self, student_population):
        self.__student_population = student_population

    def set_campus_area(self, campus_area):
        self.__campus_area = campus_area

    def info(self):
        print("Name:", self.__name)
        print("City:", self.__city)
        print("Country:", self.__country)
        print("Established Year:", self.__established_year)
        print("Student Population:", self.__student_population)
        print("Campus Area:", self.__campus_area, "square meters")
