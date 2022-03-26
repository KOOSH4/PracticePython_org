def fibonnaci_generator(x):
    fibonacci = []
    i = 1
    if x == 0:
        fibonacci = []
    elif x == 1:
        fibonacci = [1]
    elif x == 2:
        fibonacci = [1, 1]
    elif x > 2:
        fibonacci = [1, 1]
        while i < (x - 1):
            fibonacci.append(fibonacci[i] + fibonacci[i - 1])
            i += 1
    return fibonacci


user_Input = int(input("How many Fibonnaci numbers do you want to be generated? "))
fibonnaci_generator(user_Input)
print(fibonnaci_generator(x=user_Input))
