num1 = int(input("Enter Number: "))
divisors = []
i = num1

while i != 0:

    if num1 % i == 0:
        divisors.append(i)
    i-=1
print(divisors)