# Object Oriented Programming Methodology
import random
# class Employee:
#     name = "Harry"
#     language = "Py"
#     salary = 1200000


# employee = Employee()



# Problem Sets : Problem 1

# class Programmer:
#     company = "Microsoft"

#     def __init__(self,name,salary,pin):
#         self.name = name
#         self.salary = salary
#         self.pin = pin


# programmer1 = Programmer("Arpit",1250000,"245001")
# # print(programmer1)


# class Train:
#     def __init__(self,trainNo):
#         self.trainNo = trainNo


#     def book(self,fro,to):
#         print(f"Ticket is booked in Train No: {self.trainNo} from {fro} to {to}")

#     def getStatus(self):
#         print(f"Train No: {self.trainNo} is running on Time!")

#     def getFare(self,fro,to):
#         print(f"Ticket Fare in Train No: {self.trainNo} from {fro} to {to} is {random.randint(222,5555)}")


# train = Train("TKGH4567")


# Inheritance


# Property Decorators

class Employee:
    a = 1

    @classmethod
    def show(cls):
        print(f"The class attribute a value is: {cls.a}")


    @property
    def name(self):
        return f"User Name is: {self.ename}"
    
    @name.setter
    def name(self,value):
        self.ename = value


e = Employee()
e.a = 78
e.show()


# e.name = "Arpit Mishra"
# print(e.name)



# Operator Overloading

class Number:
    def __init__(self,n):
        self.n = n


    def __add__(self,num):
        return self.n + num.n

n = Number(1)
m = Number(2)
# print(n+m)



# Getters and Setters
# Getters are method that retrieve or get the value of an Object's attribute while setters are method which set the value of an attribute of object 
# Getters and setters are primarly use to Implement Encapsulation in Object Oriented Programming

class Temperature:
    def __init__(self,celcius):
        self.celcius = celcius


    @property
    def celcius(self):
        print("***** Getting Temperature ******")
        return self._celcius
    

    @celcius.setter
    def celcius(self,value):
        if value < -273.15: # Absolute zero
            raise ValueError("Temperature below absolute zero is not possible.")
        print("Setting Celsius...")
        self._celcius = value


temp = Temperature(25)


class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    # Define the behavior for the '+' operator
    def __add__(self, other):
        # The 'other' parameter is the object on the right side of the operator
        new_x = self.x + other.x
        new_y = self.y + other.y
        return Vector(new_x, new_y)

    # Define the string representation for printing
    def __str__(self):
        return f"Vector({self.x}, {self.y})"

# Create two Vector objects
v1 = Vector(2, 3)
v2 = Vector(5, 7)

# Use the overloaded '+' operator
v3 = v1 + v2

# The __str__ method is called to print the result
print(v3)
