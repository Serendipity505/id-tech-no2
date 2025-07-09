# the following program generates a fortune-telling game
narrator = "Welcome,traveler, to the fortune telling game. Here, you will explore your endless possibilities for your future using this 10 faced dice. When you are ready, tell me: roll"
print(narrator)

ready= input("Are you ready?:  ")

import random
print("rolling your fortune dice......")
ran_dum = random.randint (a = 0, b = 7)
fortune = ran_dum
print("I have read your fortune number. It is: ", + fortune)
if fortune == 0:
    print("Beware traveler, you have grave danger ahead of you. Do not wander alone outside at night, and stay away from spiders.")
elif fortune == 1:
    print("Be careful on full moon nights, seek shelter frequently")
elif fortune == 2:
    print("Do not make rash decisions especially on your finance.")
elif fortune == 3:
    print("Do not run away from your problems. If you do, you might have to face a difficult decision between losing two things that you love.")
elif fortune == 4:
    print("Your future is bright, keep on the hard work and one day, your dreams will come true.")
elif fortune == 5:
    print("One thing that you desire the most will come true! But if you crow or vaunt, you will lose it.")
elif fortune == 6:
    print("Congrats! You will have a huge opportunity in either your business or schoolwork. Do not miss out!")
elif fortune == 7:
    print("You will find passion in something and pursue it. It will lead to great success and improve your life style in many ways!")


