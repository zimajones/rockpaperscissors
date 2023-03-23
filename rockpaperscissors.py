import random

#this is a simple game of rock paper scissors

#recieve user input
print('select rock, paper, or scissors')
rock_dict = {'rock':'tie', 'paper':'lose', 'scissors':'win', 'lizard':'win', 'spock':'lose'}
paper_dict = {'rock':'win', 'paper':'tie', 'scissors':'lose', 'lizard':'lose', 'spock':'win'}
scissors_dict = {'rock':'lose', 'paper':'win', 'scissors':'tie', 'lizard':'win', 'spock':'lose'}
lizard_dict = {'rock':'lose', 'paper':'win', 'scissors':'lose', 'lizard':'tie', 'spock': 'win'}
spock_dict = {'rock':'win', 'paper':'lose', 'scissors':'win', 'lizard':'lose', 'spock':'tie'}

while True:
    user_choices = input("Enter your selection: ").lower()
    if user_choices == "rock":
        current_dict = rock_dict  
        break
    elif user_choices == "paper":
        current_dict = paper_dict
        break
    elif user_choices == "scissors":
        current_dict = scissors_dict
        break
    elif user_choices == "lizard":
        current_dict = lizard_dict
        break
    elif user_choices == "spock":
        current_dict = spock_dict
        break


#receive computer input 
computer_choices = ["rock", "paper", "scissors", "lizard", "spock"]
computer_choice = random.choice(computer_choices)
print('computer selects: ' + computer_choice)



#calculate winners
if user_choices == computer_choice:
    outcome = 'tie'
else:
    outcome = current_dict[computer_choice] if current_dict[computer_choice] == 'lose' else 'win'


print(f'you {outcome}!')






