
def reverse_word():
    user_input = input("Enter your text: ")
    list1 = user_input.split()
    list2 = []
    length = -(len(list1))

    i = -1
    while i != length-1:
        list2.append(list1[i])
        i -= 1
    list2 = ' '.join(list2)

    print(list2)


reverse_word()