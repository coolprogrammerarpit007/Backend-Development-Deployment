# file handling


# writing data into file
# file = open("myfile.txt","w")
# L = ["This is Lagos \n","This is Python \n","This is Fcc \n"]

# file.write("Hello World \n")
# file.writelines(L)
# file.close()

# reading file

file = open("myfile.txt","r")
# data = file.read()
# print(data)
# data = file.readlines()
# print(data)


# with statement in python

with open("example.txt", "r") as file:
    content = file.read()
    print(content)  # File closes automatically