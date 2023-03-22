import random

#this is a simple game of rock paper scissors

#recieve user input
print('select rock, paper, or scissors')

while True:
    user_choices = input("Enter your selection: ").lower()
    if user_choices == "rock" or user_choices == "paper" or user_choices == "scissors":  
        break  


#receive computer input 
computer_choices = ["rock", "paper", "scissors"]
computer_choice = random.choice(computer_choices)
print('computer selects: ' + computer_choice)


#calculate the winners
if computer_choice == 'rock' and user_choices == 'scissors':
    print('computer wins!')
elif computer_choice == 'paper' and user_choices == 'rock':
    print('computer wins!')
elif computer_choice == 'scissors' and user_choices == 'paper':
    print('computer wins!')
elif computer_choice == user_choices:
    print('Tie!')
else:
    print('user wins!')




