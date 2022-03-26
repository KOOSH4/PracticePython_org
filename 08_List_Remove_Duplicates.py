import random
def duplicate_remover():
    list = []
    for x in range(10):
        list.append(random.randint(0, 10))
    print(list)
    print(f"list after removing duplicate elements:\n {set(list)}")

duplicate_remover()