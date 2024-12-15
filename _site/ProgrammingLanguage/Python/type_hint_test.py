from typing import TypeVar, Generic

T_co = TypeVar("T_co", covariant=True)
T_contra = TypeVar("T_contra", contravariant=True)

class Animal():
    pass

class Cat(Animal):
    pass

class ReadOnlyBox(Generic[T_co]):
    def __init__(self, value: T_co):
        self.value = value

class WriteOnlyBox(Generic[T_contra]):
    def __init__(self):
        self.value = None

    def write(self, value: T_contra) -> None:
        self.value = value

# Covariant Example
cat_box: ReadOnlyBox[Cat] = ReadOnlyBox(Cat())
animal_box: ReadOnlyBox[Animal] = cat_box  # Works: covariance allows this

# Contravariant Example
animal_writer: WriteOnlyBox[Animal] = WriteOnlyBox()
cat_writer: WriteOnlyBox[Cat] = animal_writer  # Works: contravariance allows this


# python ProgrammingLanguage/Python/type_hint_test.py
