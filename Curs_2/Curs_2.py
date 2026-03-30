# # # Python OOP

# class ex1
class Dog:
    def __init__(self, name, age, breed): 
        self.name = name
        self.age = age
        self.breed = breed

    def bark(self):
        return f"{self.name} is a {self.breed} and says woof!"
    
# Creating a dog object
dog1 = Dog("Buddy", 3, "Golden Retriever")
print(dog1.bark())

# # class ex2
class Dog:
    def __init__(self, name, age, breed): 
        self.name = name
        self.age = age
        self.breed = breed

    def bark(self):
        return f"{self.name} says woof!"
    
    def get_age(self):
        return f"{self.name} is {self.age} years old."
    
    def get_breed(self):
        return f"{self.name} is the breed {self.breed}."

    def set_breed(self, breed):
        self.breed = breed
    
# # Creating a Dog object 
dog2 = Dog("Max", 5, "Labrador") 
print(dog2.get_age())
print(dog2.get_breed())
print(dog2.set_breed("German Shepherd"))
print(dog2.get_breed())

# inheritance ex1
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        raise NotImplementedError("Subclass must implement abstract method")

class Dog(Animal):
    def speak(self):
        return f"{self.name} says woof!"
    
class Cat(Animal):
    def speak(self):
        return f"{self.name} says meow!"
    
# Creating objects
dog = Dog("Buddy")
cat = Cat("Whiskers")
print(dog.speak())
print(cat.speak())

# inheritance ex2
class Animal:
    def __init__(self, name, species, color):
        self.name = name
        self.species = species
        self.color = color

    # Method to get animal info
    def get_info(self):
        return f"{self.name} is a {self.color} {self.species}"
    
class Dog(Animal):
    def __init__(self, name, breed, color):
        super().__init__(name, "Dog", color)
        self.breed = breed

    def get_info(self):
        return f"{self.name} is a {self.breed} {self.color}"
    
# Creating an object
dog = Dog("Buddy", "Golden Retriever", "White")
print(dog.get_info())

# polymorphism ex1
class Animal:
    def speak(self):
        raise NotImplementedError("Subclass must implement abstract method")
    
class Dog(Animal):
    def speak(self):
        return "Woof!"

class Cat(Animal):
    def speak(self):
        return "Meow!"
    
class Cow(Animal):
    def speak(self):
        return "WOO!"
    
def animal_sound(animal):
    print(animal.speak())

# Using polymorphism 
animals = [Dog(), Cat(), Cow()] 
for animal in animals:
    animal_sound(animal)

# encapsulation ex1
class Person:
    def __init__(self, name, age): 
        self.name = name
        self.__age = age # Private attribute
    
    def get_age(self):
        return self.__age
    
    def set_age(self, age): 
        if age > 0:
            self.__age = age
    
# Creating an object
person = Person("Alice", 30)
print(person.get_age())
person.set_age(35)
print(person.get_age())

print("--------------------------------")
# abstraction ex1
from abc import ABC, abstractmethod
class Shape(ABC): 
    @abstractmethod 
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height
    
    def perimeter(self):
        return 2 * (self.width + self.height)
    
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2

    def perimeter(self):
        return 2 * 3.14 * self.radius

# Creating an object
rect = Rectangle(10, 20)
print("Area:", rect.area())
print("Perimeter:", rect.perimeter())

circle = Circle(5)
print("Area:", circle.area())
print("Perimeter:", circle.perimeter())

print("--------------------------------")
# abstraction ex2
from abc import ABC, abstractmethod
class PaymentProcessor (ABC): 
    @abstractmethod
    def process_payment(self, amount):
        pass

class CreditCardProcessor(PaymentProcessor):
    def process_payment(self, amount):
        return f"Processing credit card payment of {amount}"
    
class PayPalProcessor(PaymentProcessor):
    def process_payment(self, amount):
        return f"Processing PayPal payment of {amount}"
    
class PaySafeCard(PaymentProcessor):
    def process_payment(self, amount):
        return f"Processing PaySafeCard payment of {amount}"
    
# Creating objects
processors = [CreditCardProcessor(), PayPalProcessor(), PaySafeCard()] 
for processor in processors:
    print (processor.process_payment (100))

print("--------------------------------")  

#library example
class Book:
    def __init__(self, title, author): 
        self.title = title
        self.author = author

class Library:
    def __init__(self): 
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def remove_book(self, title):
        self.books = [book for book in self.books if book.title != title]

    def list_books(self):
        for book in self.books:
            print(f"Title: {book.title}, Author: {book.author}")

# Creating objects and using the Library class 
library = Library()
book1 = Book("1984", "George Orwell")
book2 = Book("To Kill a Mockingbird", "Harper Lee")
book3 = Book("test", "test1")
library.add_book(book1)
library.add_book(book2)
library.add_book(book3)
library.list_books()
library.remove_book("1984")
library.list_books()
print("------------------------")