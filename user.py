class user:
    def _init_(self, name, age, email, address, phone_number, gender):
        self.name = name
        self.age = age
        self.email = email
        self.address = address
        self.phone_number = phone_number
        self.gender = gender

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name

    def get_age(self):
        return self.age

    def set_age(self, age):
        self.age = age

    def get_email(self):
        return self.email

    def set_email(self, email):
        self.email = email

    def get_address(self):
        return self.address

    def set_address(self, address):
        self.address = address

    def get_phone_number(self):
        return self.phone_number

    def set_phone_number(self, phone_number):
        self.phone_number = phone_number

    def get_gender(self):
        return self.gender

    def set_gender(self, gender):
        self.gender = gender

    def salutacion(self):
        print("Name: ", self.name)
        print("Age: ", self.age)
        print("Email: ", self.email)
        print("Address: ", self.address)
        print("Phone Number: ", self.phone_number)
        print("Occupation: ", self.occupation)