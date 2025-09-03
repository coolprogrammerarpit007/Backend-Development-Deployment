# Recursion in Python

# A recursive function is a function which call itself and the technique is called Recursion


# def countdown(n):
#     if n == 0:
#         return
    
#     print(n)
#     countdown(n-1)

# countdown(50)


# The Paradigm of Recursive Function is:
# The base case occurs when n is zero, at which point recursion stops.
# In the recursive call, the argument is one less than the current value of n, so each recursion moves closer to the base case.


#  Factorial Using Recursion

# def factorial(n):
#     if n == 0 or n == 1:
#         return 1
    
#     result = n * factorial(n-1)
#     return result


# factorial_result = factorial(4)
# print(f"Factorial: {factorial_result}")



# Count Leaf Items

# def count_leaf_items(item_list):
#     """
#         Recursively Calling list and count Items Inside It
#     """

#     count = 0
#     for item in item_list:
#         if isinstance(item,list):
#             count += count_leaf_items(item)

#         else:
#             count += 1

#     return count

# result_count = count_leaf_items(['Adam', ['Bob', ['Chet', 'Cat'], 'Barb', 'Bert'], 'Alex', ['Bea', 'Bill'], 'Ann'])
# print(result_count)


# Recursive Function to calculate sum of N natural numbers

# def recursive_sum(n):
#     if n == 0:
#         return 0
    
#     total = n + recursive_sum(n-1)
#     return total


# result = recursive_sum(5)
# print("Recursive Sum: ",result)

