import random

while True:
    print(f'worst challenge number is {max_try}')
    answer_number = random.randint(1, 100)
    print(answer_number)

    tries = 0

    while True:
        GetNumber = int(input("set your number:"))
        tries = tries + 1
        if answer_number == GetNumber :
            print('end')
            print(tries)
            if count > max_try:
                max_try = tries

            break
        elif answer_number > GetNumber :
            print('up')
        else :
            print('down')
    will_continue = input()
    if will_continue =='yes':
        continue
    else:
        break