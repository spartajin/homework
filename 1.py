import random
random_number = random.randint(1, 100)

print(random_number)
tries = 0

while True:
    GetNumber = int(input("set your number:"))
    tries += 1
    if random_number == GetNumber :
        print('end')
        print(tries)
        break
    elif random_number > GetNumber :
        print('up')
    else :
        print('down')
