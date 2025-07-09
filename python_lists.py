# the following program demonstrates how to use lists
list_of_numbers = [0, 4, 5, 9, 7, 8, 1, 2, 6, 3]
print(list_of_numbers)

#append elements
list_of_numbers.append(7)
print(list_of_numbers)

list_of_numbers.insert(0, 10)
print(list_of_numbers)

list_of_numbers.pop()
print(list_of_numbers)

list_of_numbers.pop(2)
print(list_of_numbers)

list_of_numbers.remove(9)
print(list_of_numbers)

list_of_numbers.sort()
print(list_of_numbers)

#sort o strings
list_of_colors = ["yellow", "blue", "purple", "red", "green","orange"]
list_of_colors.sort()
print(list_of_colors)
