
class Person:

    def __init__(self, name):
        self.name = name


class Alan(Person):

    def __init__(self, name, age):
        print("Alan")

        super().__init__(name)

        self.age = age



class Blan(Alan):

    def __init__(self, name, age, gender):
        print("Blan")

        super().__init__(name, age)

        self.gender = gender


class Test(Blan, Alan):

    def __init__(self, name, age, gender):
        print('TEST')
        super().__init__(name, age, gender)



if __name__ == "__main__":
    test = Test('afsef', 'fwefw', '23r23')




