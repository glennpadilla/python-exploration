# Reverse a list
# Given: list1 = [100, 200, 300, 400, 500]
# Expected output: [500, 400, 300, 200, 100]

list1 = [100, 200, 300, 400, 500]
list1.reverse()
print(list1)

# Turn every item of a list into its square
# Given a list of numbers, write a program to turn every item of
# the following list into its square
# Given: numbers = [1, 2, 3, 4, 5, 6, 7]
# Expected output: [1, 4, 9, 16, 25, 36, 49]

numbers = [1, 2, 3, 4, 5, 6, 7]
numbers2 = [i**2 for i in numbers]
print(numbers2)

numbers = [1, 2, 3, 4, 5, 6, 7]
for index in range(0, len(numbers)):
    current = numbers[index]
    numbers[index] = current * current
print(numbers)

numbers = [1, 2, 3, 4, 5, 6, 7]
new_list =[]
for num in numbers:
    new_list.append(num * num)
print(new_list)

# Add new item to a list after a specified item
# Task: Add item 7000 after 6000 in the following list
# Given: list1 = [10, 20, [300, 400, [5000, 6000], 500], 30, 40]
# Expected output: [10, 20, [300, 400, [5000, 6000, 7000], 500], 30, 40]

list1 = [10, 20, [300, 400, [5000, 6000], 500], 30, 40]
outer = list1[2]
inner =outer[2]
inner.append(7000)
# outer[2] = inner
# list1[2] = outer
print(list1)
