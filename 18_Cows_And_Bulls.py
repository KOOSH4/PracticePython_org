import random
def random_number():
    random_numbers = []
    i = 1


    while i < 2:
        digit = str(random.randint(0, 9))
        if digit in random_numbers:
            continue
        else:
            random_numbers.append(digit)
            if len(random_numbers) == 4:
                i += 1

    return random_numbers

def is_true(rand_list):
    bulls = 0
    cows = 0
    user_list = []
    user_input = input("enter a 4-Digit number:")
    if user_input == "hint":
        print(rand_list)
    for i in user_input:
        user_list.append(i)
    for item in user_list :
        for t in rand_list:
            if t == item:
                cows += 1
                index_random = rand_list.index(item)
                index_list = user_list.index(t)
                if index_random == index_list:
                    cows -= 1
                    bulls += 1
                    if bulls == 4:
                        return 1


    print(f"\t\t Bulls = {bulls}")
    print(f"\t\t Cows = {cows}")
loop = 1
rand_digit = random_number()
while loop < 2:
    if is_true(rand_list = rand_digit ) == 1:
        print("\t\t\t\t **** Correct Guess! ****")
        print("\t\t\t\t **** You Won! ****")
        break
    else:
        continue

