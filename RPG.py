# The following program create a text adventure game.
    #Introduction
print("\n")
print("                                        I Accidentally Conquered the Final Boss of the Royal Family Game")
print("                                                               RPG Game By Emily")
print("\n       Welcome host, to the game world: “Fantasia”. I am your Game Threading System, Q. "
          "\nIn order to travel back to your universe, you must finish all the missions as the main character: Sir Charles,and defeat the finale boss. "
          "\nIt is my job to accompany you. Any OOC or OTP may lead to xp loss and eventually ending the game."
          "\nGood luck accommodation and may the odds ever be in your favor. (lol)")

print("\n     You wonder wth that was about. As you look around, you find yourself by a Palace, and it seems like you are lying in front of the Palace’s main entrance."
          "\nBy your side, there is a badge with your face and name imprinted on it."
      "\n"
      "\n   You look down and found yourself in a white dress shirt with tall collars and frilly long sleeves. "
      "\nThe blue ribbon you are wearing looks especially striking on top of the silk like fit."
      "\nA silver eagle crest pinned on your right chest glimmering in the sunlight."
      "\nYou move your legs and discovered a navy blue top coat with round silver buttons fixed on the sleeves."
      "\nThe sleek black,waist length pants seems like it's made out of fibers that spiders weaved. Light and smooth."
          "\nYou then found a book in your pocket. “Fantasia Game Plot” is its title. You wondered huh so this is the game I traveled into."
      "\n"
      "\nThe system gave you a few action choices......:")

#player choices
print("\nAction Choices:"
      "\n")
print("1)Run away! There’s no F-ing way this is all real!")
print("2)Pick up the badge and opens the Palace doors. The system said if I want to escape, I must complete the missions!")
print("3)Nap. Zzzzzzzzzzzz……")
player_choices = int(input("\nPlease choose wisely my host(enter number):  "))


#incorrect answer no1
if player_choices == 1:
    print("\nYou chose 1......"
          "\n"
          "\nYou scrambles to get up and start sprinting towards the other direction. Sadly, you got sapped by lighting before you got far."
          "\n You the found yourself in front of the Palace again.")

elif player_choices == 3:
    print("\n You chose 3....."
          "\n"
          "\n BrO GeT OuT!!!!!! Ur NoT sKiBiDi!!!!!!!! U nOt ThE AlPhA bROoOOoooo!!!!!!")






#correct answer:
elif player_choices == 2:
    print("\n You chose 2......     "
          "\n"
          "\n You gathered up your courage and steps into the hollow hall. "
          "\nEvery thing seems so grand and luxurious. Walls covered in Gold, mystical paintings on the ceiling.... "
          "\nThe hallway seems to go on forever....")

    # riddle
    print("\n       As you strode through the empty hall, a guard jumped in your way...."
          "\n'Ugh great! A NPC' you though"
          "\n'Who are you? You dare intrude the royal palace?'"
          "\n 'No my bro, you got it wrong' you replied, but then a warning flashed before your eyes:"
          "\n'OOC warning! OOC warning! 3 more warnings and -100 xp!' the system buzzed. You stumbled back,  surprised from the sudden commotion."
          "\n'Yeah, you definitely look shady.... If you want to get past me, you must answer a riddle every person in the royal family should know, even the servants and the chefs.'"
          "\n'What walks on four legs in the morning, two legs at noon, and three in the evening?' The guard asked"
          "\n")

    player_attempts = 5
    guessed = False
    while not guessed and player_attempts >0:
        password = input("\nPlease think wisely my host.(type your answer here. All in lower case):  ")

        if password == "human":
            guessed = True
            print("\n'That is ..... correct. Please, do excuse my rudeness your highness'")

            # first mission
            print("\nThe guard stepped aside and let you passed."
                    "\n'congratulations host, you finished your first mission. Guard's riddle! You now have 100xp in your balance!"
                    "\nTo access the gadget shop, please say yes!"
                    "\nif not simply say no!'"
                    "\n"
                    "\n'Huh, a gadget shop, that'll probably help me with my mission!'you thought.....")
            action_attempts=input("Access the gadget shop?:  ")
            if action_attempts == "yes":
                gadgets = {"xp boost": 500, "wig": 1000, "anti ooc system(locked) " + "easy mode": 700}
                print(gadgets)



            else:
                print("You can access the gadget shop everytime you complete a mission.")







        else:
            player_attempts-=1
            print("'That is not the right answer....' Suddenly, you feel a cold and sharp pain in your chest. "
            "\nYou looked down and found out that you have been stabbed through the chest with a spear."
            "\n your vision starts swaying and soon the whole world went dark......\n"
            "\n                                          GAME OVER!"
            "\n                    You have " + str(player_attempts) + " more attempts to answer the guard's riddle....")








