# Let's create a class!
class Person:
   origin_country = "USA" # class attributes

   def __init__(self, name, age, gender): #constructor/initializator method
     self.name = name #instance attributes
     self.age = age
     self.gender = gender

   def speak(self, words): # class method
     print(f"{self.name} speaks: {words}")

# Let's create a child class!
class Employee(Person):
   def __init__(self, name, age, gender, salary, job_title):
     super().__init__(name, age, gender) #avoid writing base class name (Person in our case)
     self._salary = salary # protected attribute
     self.__job_title = job_title # private attribute

   def display_info(self):
     print(f"Employee {self.name} works as a {self.__job_title}")

obj = Employee("George", 28, "male", "300$", "joj")
Employee.display_info(obj)

issubclass(Employee, Person) #whether class is derived from another class or it's the same class
isinstance(Person("George", 28, "male"), Person) #whether object is an instance of a class or a subclass

