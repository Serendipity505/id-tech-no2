#casting
#As mentioned, the input() function takes string inputs, including integers. So, suppose the user enters a number through the input() function, like the character's age in the previous example. That number can't be used to perform arithmetic operations because it's considered a string.
number = input("Enter an integer:  ")

#string to int
new_int = int(number)
print(new_int + 50)

#int to string
new_string = str(50)
print(number + new_string)