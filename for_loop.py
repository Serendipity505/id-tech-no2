# 1)
# the following program will use a for loop to count all the
number_of_leaves= 14
for x in range( 0, number_of_leaves):
    print("A leaf fell to the ground " + str(x) + " leaves have fallen")
print("all the leaves fell. The for loop is complete")


#2)
password_attempts= 5
guessed = False
while not guessed and password_attempts > 0 :
    password = input("enter password: ")
    if password == "password":
        guessed = True
        print("access granted")
    else:
        password_attempts -=1
        print("incorrect, you have " + str(password_attempts) + " more attempts " )

