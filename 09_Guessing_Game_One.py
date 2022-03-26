import random
i = 1
rand_number = random.randint(1, 9)
while i < 2:
    user_input = input("Enter your guess:(1-9)\n or type exit to end the game >>")
    if user_input == "exit" :
        print("Bye!")
        break
    elif rand_number == int(user_input):
        print("Correct!")
        break
    elif rand_number < int(user_input):
        print("your guess is high!")
    elif rand_number > int(user_input):
        print("your guess is low!")

