# program to check if poem includes twinkle

# with open("poem.txt","r") as f_hand:
#     data = f_hand.read()
#     if "Twinkle" in data or "twinkle" in data:
#         print("This Poem Includes Twinkle")
#     else:
#         print("Not Includes Twinkle") 
    

# Problem 2

# import random

# def play_game():
#     return random.randint(1,100)

# result = play_game()
# print(f"Your Game Score Is: {result}")


# with open("hi_score.txt","r") as f_hand:
#      high_score = f_hand.read()


# if high_score == "" or int(high_score) < result:
#     with open("hi_score.txt","w") as f_hand:
#         f_hand.write(str(result))

# else:
#     print(f"Previous High Score Still Stands: {high_score}")



# Problem 3

# def generateTable(num):
#     table = ""
#     for i in range(1,11):
#         table += f"{num} X {i} = {num*i}\n"
#     with open(f"tables/table_{num}.txt","w") as f_hand:
#         f_hand.write(table)


# for i in range(2,21):
#     generateTable(i)


# Problem 4

# word = "Lion"

# with open("animal.txt","r") as f:
#     content = f.read()

# contentNew = content.replace("Lion","####")
# with open("animal.txt","w") as f:
#     f.write(contentNew)