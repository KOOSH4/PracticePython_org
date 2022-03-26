import random

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
commonNumbers = []


# With this function A is always the longest list!


def is_common(aa, bb):
        for x in aa:
            for y in bb:
                if x == y:
                    commonNumbers.append(y)
                    bb.remove(y)

        print(f"\nCommon numbers are: {commonNumbers}\n")
        aa.clear()
        bb.clear()
        commonNumbers.clear()


def random_list():
    z = []
    list1_length = random.randint(10, 13)

    while list1_length != 0:
        random1 = random.randint(0, 12)
        if not (random1 in z):
            z.append(random1)
            list1_length -= 1
    return z


if len(a) >= len(b):
    is_common(aa=a, bb=b)
else:
    is_common(aa=b, bb=a)

# Extra 1

a = random_list()
b = random_list()

print(f"First randomly generated list is:\n a={a}\n")
print(f"Second randomly generated list is:\n b={b}\n")
if len(a) >= len(b):
    is_common(aa=a, bb=b)
else:
    is_common(aa=b, bb=a)

