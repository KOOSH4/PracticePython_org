name = input("enter your word: ")
lengh = len(name)
Minus = -(lengh)
palindrome_String = []
x = -1
while x != (Minus-1):
    palindrome_String.append(name[x])
    x -= 1
new_name = ''.join(palindrome_String)
if name == new_name:
    print(f"{name} is palindrome!")
else:
    print(f"{name} is not palindrome!")