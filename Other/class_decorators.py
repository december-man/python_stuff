#class method implementation vs static method

class Person: 
    origin_country = "USA" 
 
    def init(self, name, age, gender): 
        self.name = name 
        self.age = age 
        self.gender = gender 
 
    @classmethod 
    def change_origin_country(cls, new_country): 
        cls.origin_country = new_country 
        print(cls.origin_country) 
 
    @staticmethod 
    def is_adult(age):
        return age > 18


# property implementation
class Person: 
    def init(self, first_name, last_name): 
        self.first_name = first_name 
        self.last_name = last_name 
 
    @property 
    def email(self): 
        return f"{self.first_name}.{self.last_name}@email.com"
    
# abstract method implementation

from abc import ABC, abstractmethod 
 
class Animal(ABC): 
    @abstractmethod 
    def eat(self): 
        raise NotImplementedError("You have to implement eat() method") 
 
class Dog(Animal):
    def __init__(self):
        pass 
    def suck(self):
        pass
    
obj = Dog()
