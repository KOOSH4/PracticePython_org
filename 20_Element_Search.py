import random
def list_generator():
    number = 9
    rand_list = []
    for item in range(15):
        rand_list.append(random.randint(1,15))
    sorted_list = set(rand_list)
    print(sorted_list)
    if number in sorted_list:
        return 1
    else:
        return 0


result = list_generator()
if result:
    print("the given number is inside the list!")
else:
    print("the given number is NOT inside the list!")
