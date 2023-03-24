import random

# this is a simple game of rock paper scissors

# receive user input
print('select rock, paper, or scissors')
rock_dict = {'rock': 'tie', 'paper': 'lose', 'scissors': 'win', 'lizard': 'win', 'spock': 'lose'}
paper_dict = {'rock': 'win', 'paper': 'tie', 'scissors': 'lose', 'lizard': 'lose', 'spock': 'win'}
scissors_dict = {'rock': 'lose', 'paper': 'win', 'scissors': 'tie', 'lizard': 'win', 'spock': 'lose'}
lizard_dict = {'rock': 'lose', 'paper': 'win', 'scissors': 'lose', 'lizard': 'tie', 'spock': 'win'}
spock_dict = {'rock': 'win', 'paper': 'lose', 'scissors': 'win', 'lizard': 'lose', 'spock': 'tie'}

user_wins = 0
computer_wins = 0
total_games = user_wins + computer_wins

for i in range(5):
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

        # receive computer input
    computer_choices = ["rock", "paper", "scissors", "lizard", "spock"]
    computer_choice = random.choice(computer_choices)
    print('computer selects: ' + computer_choice)

    # calculate winners
    user_wins = 0
    computer_wins = 0
    total_games = user_wins + computer_wins
    if user_choices == computer_choice:
        outcome = 'tie'

    else:
        outcome = current_dict[computer_choice] if current_dict[computer_choice] == 'lose' else 'win'
    #add to the scoring column
    if outcome == 'lose':
        computer_wins += 1
        total_games += 1
        print('you lose!')
    elif outcome == 'win':
        user_wins += 1
        total_games += 1
        print('you win!')
    elif outcome == 'tie':
        total_games += 1
        print("it's a tie!")

#calculate whole winner
if user_wins > computer_wins:
    full_outcome = 'win'
elif user_wins < computer_wins:
    full_outcome = 'lose'
else:
    full_outcome = 'tie'



print(f"you {outcome} the score is {user_wins} to {computer_wins}!")






