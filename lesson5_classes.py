# Simple Class
class MyClass:
    """A simple example class"""
    i = 12345

    def f(self):
        return 'hello world'


# Class objects with init
class Log:
    """A test log object"""
    def __init__(self, name, errorType):
        self.name = name
        self.errorType = errorType


logError = Log('Null pointer detected', 'Exception')
print(logError.name)
print(logError.errorType)

# Instance Objects
# attribute references: data attributes and methods

# Data attributes (new)
logError.counter = 1
print(logError.counter)
del logError.counter

# Method Objects
x = MyClass()
print(x.f())
xf = x.f
print(xf())


# Class and Instance Variables
# Instance Variables - unique to each instance
# Class Variables - for attributes and method shared by all instances

class Dog:
    kind = 'Canine'

    def __init__(self, name):
        self.name = name

d = Dog('Popoy')
x = Dog('Eloy')

print(d.kind)
print(x.kind)
print(d.name)
print(x.name)

# Correct design of instance variables to not be shared by everyone:
class Dog:

    def __init__(self, name):
        self.name = name
        self.tricks = []    # creates a new empty list for each dog

    def add_trick(self, trick):
        self.tricks.append(trick)

# If it's the same name, the instance class is prioritized


# Inheritance
# class DerivedClassName(BaseClassName):
# class DerivedClassName(modname.BaseClassName):
