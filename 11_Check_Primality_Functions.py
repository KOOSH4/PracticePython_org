def is_prime():
    user_input = int(input("Enter a number:"))
    i = 2
    while i <= (user_input/2):
        if user_input % i == 0:
            return 0
        else:
            i+=1
    return 1


if is_prime():
    print("Is prime!")
else:
    print("Is NOT prime!")