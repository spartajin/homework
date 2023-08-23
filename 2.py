import random

choices = ['rock', 'paper', 'scissors']
count_win = 0
count_draw = 0
count_lose = 0

while True:
    answer = input("rock, paper, scissors:")
    computer = random.choice(choices)
    print(computer)
    if answer == computer:
        print('draw')
        count_draw = count_draw + 1
    elif answer == 'rock' and computer == 'scissors':
        print('win')
        count_win = count_win + 1
    elif answer == 'paper' and computer == 'rock':
        print('win')
        count_win = count_win + 1
    elif answer == 'scissors' and computer == 'paper':
        print('win')
        count_win = count_win + 1
    elif answer == 'rock' and computer == 'paper':
        print('win')
        count_win = count_win + 1
    else:
        print('lose')
        count_dlose = count_lose + 1
    
    will_continue = input()
    if will_continue =='yes':
        continue
    else:
        break

print(f'win:{count_win}draw:{count_draw}lose:{count_lose}')