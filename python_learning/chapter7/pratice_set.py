# Pratice Programs

# number = int(input("Enter Number: "))

# index = 0

# print(f"Multiplication Table of {number}")
# for index in range(10):
#     print(f"{number} X {index+1} = {number * (index + 1)}")

# print("End of Multiplication Table")


# check prime number

# number = int(input("Enter Number: "))

# for index in range(2,number):
#     if number % index == 0:
#         print("Not Prime Number")
#         break


# else:
#     print("Prime Number")


'''
     
         *                 for n = 3
        ***
       *****

'''


# number = int(input("Enter Number: "))


# for i in range(1,number+1):
#     print(" " * (number - i),end="")
#     print("*" * (2*i-1),end="")
#     print("")



number = int(input("Enter Number: "))


# for i in range(1,number+1):
#     if i == 1 or i == number:
#         print("*" * number , end="")

#     else:
#         print("*",end="")
#         print(" "*(number-2),end="")
#         print("*",end="")
#     print("")


for index in range(10,0,-1):
    print(f"{number} X {index} = {number * index}")
    
