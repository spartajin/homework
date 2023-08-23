import random

choices = ['rock', 'paper', 'scissors']

answer = input("rock, paper, scissors:")
computer = random.choice(choices)
print(computer)
if answer == computer:
    print('draw')
elif answer == 'rock' and computer == 'scissors':
    print('win')
elif answer == 'paper' and computer == 'rock':
    print('win')
elif answer == 'scissors' and computer == 'paper':
    print('win')
elif answer == 'rock' and computer == 'paper':
    print('win')
else:
    print('lose')