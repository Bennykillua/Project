
#defining a class
class Car:
    pass

#this creates a car class with no artibutes or methods
Car()

#a = Car()
#b = Car()
#print (a == b) #this will return False

#using the .__doc__ this give you details about your class.
class Car:
    """This is my docstring, it explains mbrief about my class. 
      This class is about car who have 4 wheels"""
    wheels = "four"

print(Car.__doc__)

class Car:
    wheels = "four"
    def __init__(self, model, colour):
         self.model = model
         self.colour = colour

Toyota = Car("Toyota", "yellow")
kia = Car ("Kia", "black")
Ford = Car("ford", "blue")
Honda = Car("Honda", "brown")

#instance attributes
Toyota.model
print(Toyota.model)

kia.colour
print(kia.colour)

#class attributes
Toyota.wheels
print(Toyota.wheels)

kia.wheels
print (kia.wheels)

#modifying our attributes
Toyota.colour = "red" #previously yellow
#Toyota.colour
print (Toyota.colour)

kia.wheels = "two" #previously four
#kia.wheels
print (kia.wheels) 

class Car:
    wheels = "four"
    def __init__(self, model, colour):
         self.model = model
         self.colour = colour

    # Instance method
    def details(self):
        return f"this {self.model} is {self.colour}"

    # Another instance method
    def speed(self, speed):
        return f"This {self.model} is {speed} at top speed"

Toyota = Car("Toyota","yellow")
#Toyota.details()
print (Toyota.details())

#Toyota.speed(280)
print (Toyota.speed(280))

#you can use the .__str__(): if you can't see your ouput if you use the print()
#Methods like .__init__() and .__str__() are called dunder methods.

class Hybrid_engine(Car):
    pass

class Gas_engine(Car):
    pass

Toyota = Gas_engine("Toyota", "yellow")
kia = Gas_engine("kia", "black")
Honda = Gas_engine("Honda", "brown")
Ford = Hybrid_engine("Ford", "blue")

print(type(Toyota))
print(isinstance(Toyota, Car))
print(type(Ford))
print (isinstance (Ford, Gas_engine))
#Toyota, Kia, Honda and Ford are all instance of Car but Ford wouldn’t be in the Hypdrid engine class instance.

#Let’s give it the parent’s functionality specific to it

class Hybrid_engine(Car):
    def speed(self, speed="210"):
        return f"{self.model} Speed; {speed}"

Ford = Hybrid_engine("Ford", "blue")
print (Ford.speed())

class Car:
    wheels = "four"
    def __init__(self, model, colour):
         self.model = model
         self.colour = colour

    # Instance method
    def details(self):
        return f"this {self.model} is {self.colour}"

    # Another instance method
    def speed(self, speed):
        return f"This {self.model} is {speed} at top speed"

Toyota = Gas_engine("Toyota","yellow")
print (Toyota.speed(367))

#however ford wouldn’t get the change since we define his child class

Ford = Hybrid_engine ("Ford", "blue")
print (Ford.speed(467))

#however if we didn’t want that, we use .super for the child class

class Hybrid_engine (Car):
    def speed(self, speed="210"):
        return super().speed(speed)

Ford = Hybrid_engine ("Ford", "blue")
print (Ford.speed())


