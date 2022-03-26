num1 = int(input("Enter Number: "))


result = num1 % 2

if result:
    print(f"{num1} is an Odd number!\n")
else:
    print(f"{num1} is an Even number!\n")
# Extra 1
if num1 % 4 == 0:
    print(f"{num1} is also divisible by 4!\n")

# Extra 2
num = int(input("Enter Number: "))
check = int(input("Enter Number: "))
if num % check == 0:
    print(f"{num} is divisible by {check}!")
else:
    print(f"{num} is NOT divisible by {check}!")
