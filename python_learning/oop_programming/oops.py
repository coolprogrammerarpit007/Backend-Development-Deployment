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


class Train:
    def __init__(self,trainNo):
        self.trainNo = trainNo


    def book(self,fro,to):
        print(f"Ticket is booked in Train No: {self.trainNo} from {fro} to {to}")

    def getStatus(self):
        print(f"Train No: {self.trainNo} is running on Time!")

    def getFare(self,fro,to):
        print(f"Ticket Fare in Train No: {self.trainNo} from {fro} to {to} is {random.randint(222,5555)}")


train = Train("TKGH4567")