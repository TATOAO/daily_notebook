from pydantic import BaseModel

class Person(BaseModel):
    name: str
    age: int
    
class Teacher(Person):
    school: str

    @property
    def the_name(self):
        return self.name

def main():
    teacher = Teacher(name='alan', age='11', school='aaa')

    import ipdb;ipdb.set_trace()
    


if __name__ == "__main__":
    main()


