import random
def password_generator(a, b, l):
    password = []
    temp_list = []
    for x in range(l):
        rand_number = random.randint(a, b)
        password.append(chr(rand_number))
    password = ''.join(password)
    print(password)




how_strong = input("how strong you want your password to be? (W)eak , (N)ormal, (S)trong? ")
if how_strong.lower() == "w":
    password_generator(a = 97 , b = 122 ,l = 5)
elif how_strong.lower() == "n":
    password_generator(a = 49 , b = 90 ,l = 8)
elif how_strong.lower() == "s":
    len = int(input("how many character? recommended bigger than 10: "))
    password_generator(a = 33 , b = 126 ,l = len)