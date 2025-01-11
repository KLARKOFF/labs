#1

class UserAccount:
    def __init__(self, username, password, email):
        self.username=username
        self.__password=password
        self.email=email

    def set_password(self, new_password):
        self.__password=new_password

    def get_password(self):
        return self.__password

    def check_password(self, input_password):
        if input_password == self.__password:
            return True
        return False

Коля = UserAccount("KOLYAN", "1234", "kolya_polyakov2006@mail.ru")

print("Текущий пароль:", Коля.get_password())
Коля.set_password("s11UpEr*P!%aRo$Il$2040")

if Коля.check_password("1234"):
    print("Успешный вход!")
else:
    print("Неверный пароль!")

if Коля.check_password("s11UpEr*P!%aRo$Il$2040"):
    print("Успешный вход!")
else:
    print("Неверный пароль!")

#2

class Vehicle:
    def __init__(self, make, model):
        self.make=make
        self.model=model

    def get_info(self):
        return "Это машина марки " + self.make + ", модели " + self.model + "."

class Car(Vehicle):
    def __init__(self, mark, model, fuel_type):
        super().__init__(mark, model)
        self.fuel_type=fuel_type

    def get_info(self):
        return "Это машина марки " + self.make + ", модели " + self.model + ". Тип топлива: " + self.fuel_type

my_car = Car("бэмэвэ", "очень крутой", "дизель")
print(my_car.get_info())
