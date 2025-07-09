# The following program uses a while loop to check if the inout password is correct
guessed = False

while not guessed:
    password = input("Enter a password:  ")
    if password == "idk" :
        guessed = True
        print("access Granted!")
    else:
        print("access Denied!!!!!!!!!!!!! Try again!!!")

        password = input("enter ur interest:  ")
        if password =="kpop" or password == "anime":

            guessed= True
            print("u r my bestie")

